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
import logging
import sys

from helper.file_system import get_log_files, get_default_config_path


PROGRAM_NAME = 'PegelWacht CSV Log Import'
PROGRAM_VERSION = '0.1'
PROGRAM_DESCRIPTION = 'import log files'


def _setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    parser.add_argument('-e', '--delete', action='store_true', default=False, help='delete processed log file')
    parser.add_argument('-c', '--config', default=get_default_config_path(), help='config file path')
    parser.add_argument('input_dir', help='input directory')
    return parser.parse_args()


def _setup_logging(args):
    log_format = logging.Formatter(fmt='[%(asctime)s][%(module)s][%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger('')
    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    console_logger = logging.StreamHandler()
    console_logger.setFormatter(log_format)
    logger.addHandler(console_logger)


if __name__ == '__main__':
    args = _setup_argparser()
    _setup_logging(args)
    
    logging.debug('config used: {}'.format(args.config))
    
    log_files = get_log_files(args.input_dir)
    
    logging.info('{} log files found'.format(len(log_files)))
    
    sys.exit(0)