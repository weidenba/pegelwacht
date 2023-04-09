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


def get_measuring_points(config):
    measruing_points = list()
    measuring_point_count = 0
    while 'measuring_point_' + str(measuring_point_count) in config:
        point_index = 'measuring_point_' + str(measuring_point_count)
        mp = MeasuringPoint(
            config[point_index]['name'],
            config[point_index]['coordinate_n'],
            config[point_index]['coordinate_e'],
            config[point_index]['import_module'])
        measruing_points.append(mp)
        measuring_point_count += 1
    return measruing_points


def get_config(config_file):
    logging.debug('config used: {}'.format(config_file))
    config = ConfigParser()
    config.read(config_file)
    return config
