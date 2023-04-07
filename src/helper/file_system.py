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


def get_log_files(log_dir, file_extension='.csv'):
    log_dir = Path(log_dir)
    return list(log_dir.glob('*' + file_extension))


def get_default_config_path():
    current_folder = Path(__file__).parent.absolute()
    main_folder = current_folder.parent.parent
    return (main_folder / 'pegelwacht.cfg').__str__()
