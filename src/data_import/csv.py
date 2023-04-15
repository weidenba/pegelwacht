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
from pathlib import Path


from helper.file_system import get_log_files


class CsvImportModule:

    def __init__(self, measureing_point, config):
        self.measureing_point = measureing_point
        self.measureing_point.set_csv_options(
            Path(config[measureing_point.config_section_name]['log_file_directory']),
            config[measureing_point.config_section_name].getboolean('header_line'),
            int(config[measureing_point.config_section_name]['date_field']),
            int(config[measureing_point.config_section_name]['time_field']),
            int(config[measureing_point.config_section_name]['level_field'])
        )

    def import_csv_log(self, log):
        pass

    def import_data(self):
        log_files = get_log_files(self.measureing_point.log_file_directory)
        for log in log_files:
            self.import_csv_log(log)
