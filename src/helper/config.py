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
import logging

from configparser import ConfigParser


from objects.measuring_point import MeasuringPoint
from helper.database import MeasuringPoint_1, MeasuringPoint_2, MeasuringPoint_3, MeasuringPoint_4


def get_measuring_points(config):
    MP_DATABASE_CLASSES = [MeasuringPoint_1, MeasuringPoint_2, MeasuringPoint_3, MeasuringPoint_4]
    measruing_points = list()
    measuring_point_count = 0
    while 'measuring_point_' + str(measuring_point_count) in config:
        config_section_name = 'measuring_point_' + str(measuring_point_count)
        mp = MeasuringPoint(
            config_section_name,
            config[config_section_name]['name'],
            config[config_section_name]['coordinate_n'],
            config[config_section_name]['coordinate_e'],
            config[config_section_name]['import_module'],
            MP_DATABASE_CLASSES.pop(0))
        measruing_points.append(mp)
        measuring_point_count += 1
    return measruing_points


def get_config(config_file):
    logging.debug('config used: {}'.format(config_file))
    config = ConfigParser()
    config.read(config_file)
    return config
