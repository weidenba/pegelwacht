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

    def __init__(self, config_section_name, name, coordinate_n, coordinate_e, critical_level, import_plugin, database_class):
        self.config_section_name = config_section_name
        self.name = name
        self.coordinate_n = coordinate_n
        self.coordinate_e = coordinate_e
        self.critical_level = critical_level
        self.import_plugin = import_plugin
        self.database_class = database_class

    def set_csv_options(self, log_file_directory, header_line, date_field, time_field, level_field, separator):
        self.log_file_directory = log_file_directory
        self.header_line = header_line
        self.date_field = date_field
        self.time_field = time_field
        self.level_field = level_field
        self.separator = separator

    def set_level_data(self, timestamps, levels):
        self.timestamps = timestamps
        self.levels = levels

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'MeasuringPoint(name="{}", coordinates="N:{} E:{}", import_plugin="{}")'.format(self.name, self.coordinate_n, self.coordinate_e, self.import_plugin)
