import pytest
from configparser import ConfigParser
from helper.database import get_database_uri


TEST_CONFIG_SQLITE = ConfigParser()
TEST_CONFIG_SQLITE['database'] = {'provider': 'sqlite', 'database': '/tmp/sqlite.db'}
TEST_CONFIG_MYSQL = ConfigParser()
TEST_CONFIG_MYSQL['database'] = {'provider': 'mysql',
                                 'database': 'testDB',
                                 'host': 'localhost',
                                 'port': '3306',
                                 'user': 'test_user',
                                 'password': 'secret001'}


@pytest.mark.parametrize('input_data, expected', [
    (TEST_CONFIG_SQLITE, 'sqlite:////tmp/sqlite.db'),
    (TEST_CONFIG_MYSQL, 'mysql://test_user:secret001@localhost:3306/testDB'),
])
def test_get_database_uri(input_data, expected):
    result = get_database_uri(input_data)
    assert result == expected
