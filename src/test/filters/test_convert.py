from filters.convert import unix_to_hr_time, separator_conversion


def test_unix_to_hr_time():
    assert unix_to_hr_time(1626285600) == "14.07.2021 - 20:00:00"


def test_separator_conversion():
    assert separator_conversion('1.0') == '1,0'
