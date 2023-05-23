from helper.time import get_unix_time_stamp


def test_get_unix_time_stamp():
    date = '05.04.2023'
    time = '01:30'
    assert get_unix_time_stamp(date, time) == 1680651000
