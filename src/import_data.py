#! /usr/bin/env python3
'''
    PegelWacht
    Copyright (C) 2023 Peter Weidenbach

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse
import sys
import logging

from helper.config import get_config, get_measuring_points
from helper.file_system import get_default_config_path
from helper.logging import setup_logging
from data_import.csv import CsvImportModule

PROGRAM_NAME = 'PegelWacht Data Import'
PROGRAM_VERSION = '0.1'
PROGRAM_DESCRIPTION = 'import log data of measuring points'


def _setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    parser.add_argument('-e', '--delete', action='store_true', default=False, help='delete processed log files')
    parser.add_argument('-c', '--config_file', default=get_default_config_path(), help='config file path')
    return parser.parse_args()


if __name__ == '__main__':
    args = _setup_argparser()
    setup_logging(args)

    config = get_config(args.config_file)

    measuring_points = get_measuring_points(config)
    for mp in measuring_points:
        if mp.import_plugin == 'csv':
            logging.debug(mp.__repr__())
            import_module = CsvImportModule(mp, config)
            logging.debug(import_module.__repr__())
            import_module.import_data()

    sys.exit(0)
