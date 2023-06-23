from configparser import ConfigParser
from pathlib import Path

from helper.config import get_measuring_points, get_config


def test_get_measuring_points():
    test_config = ConfigParser()
    test_config['measuring_point_0'] = {'name': 'test_0', 'critical_level': '1,0', 'coordinate_n': '50.510229', 'coordinate_e': '6.967724', 'import_module': 'csv'}
    test_config['measuring_point_1'] = {'name': 'test_1', 'critical_level': '2,0', 'coordinate_n': '50.510000', 'coordinate_e': '6.967777', 'import_module': 'web_crawler'}

    result = get_measuring_points(test_config)
    assert len(result) == 2
    assert str(result[0]) == 'test_0'
    assert result[1].__repr__() == 'MeasuringPoint(name="test_1", coordinates="N:50.510000 E:6.967777", import_plugin="web_crawler")'


def test_get_config():
    current_folder = Path(__file__).parent.absolute()
    test_config_file_path = current_folder.parent / 'test_data' / 'test.cfg'

    config = get_config(test_config_file_path)
    measuring_points = get_measuring_points(config)
    assert len(measuring_points) == 2
    assert str(measuring_points[0]) == 'test creek'
