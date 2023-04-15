from pathlib import Path
from data_import.csv import CsvImportModule
from helper.config import get_config, get_measuring_points


CURRENT_FOLDER = Path(__file__).parent.absolute()
TEST_CONFIG_PATH = CURRENT_FOLDER.parent / 'test_data' / 'test.cfg'
TEST_LOG_FOLDER_PATH = CURRENT_FOLDER.parent / 'test_data' / 'logs'


def test_initgration_init_module():
    config = get_config(TEST_CONFIG_PATH)
    mp = get_measuring_points(config)
    test_module = CsvImportModule(mp[0], config)

    assert test_module.measureing_point.name == 'test creek'
    assert test_module.measureing_point.header_line
    assert test_module.measureing_point.level_field == 2
