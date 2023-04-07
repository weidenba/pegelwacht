from pathlib import Path
from helper.file_system import get_log_files, get_default_config_path


CURRENT_FOLDER = Path(__file__).parent.absolute()
TEST_DATA_FOLDER = CURRENT_FOLDER.parent / 'test_data'


def test_get_log_files():
    log_file_test_folder = TEST_DATA_FOLDER / 'logs'
    result = get_log_files(log_file_test_folder)
    assert len(result) > 0
    assert '.csv' in result[0].__repr__()


def test_get_default_config_path():
    config_path = get_default_config_path()
    assert isinstance(config_path, str)
    assert Path(config_path).exists()
