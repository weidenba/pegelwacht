from helper.time import get_unix_time_stamp, get_time_period


def test_get_unix_time_stamp():
    date = '05.04.2023'
    time = '01:30'
    assert get_unix_time_stamp(date, time) == 1680651000


def test_get_time_period():
    begin_time, end_time = get_time_period(2)
    assert type(begin_time) == int
    assert type(end_time) == int
    assert end_time == begin_time + 172800
