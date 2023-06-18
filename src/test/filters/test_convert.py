from filters.convert import unix_to_hr_time


def test_unix_to_hr_time():
    assert unix_to_hr_time(1626285600) == "14.07.2021 - 20:00:00"
