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


class MeasuringPoint:

    def __init__(self, config_section_name, name, coordinate_n, coordinate_e, import_plugin):
        self.config_section_name = config_section_name
        self.name = name
        self.coordinate_n = coordinate_n
        self.coordinate_e = coordinate_e
        self.import_plugin = import_plugin

    def set_csv_options(self, log_file_directory, header_line, date_field, time_field, level_field):
        self.log_file_directory = log_file_directory
        self.header_line = header_line
        self.date_field = date_field
        self.time_field = time_field
        self.level_field = level_field

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'MeasuringPoint(name="{}", coordinates="N:{} E:{}", import_plugin="{}"'.format(self.name, self.coordinate_n, self.coordinate_e, self.import_plugin)
