import pytest
from filters.tendency import get_tendency, ARROW_RIGHT, ARROW_UP, ARROW_DOWN,\
    ARROW_UP_RIGHT, ARROW_DOWN_RIGHT


@pytest.mark.parametrize('input_data, expected', [
    ([1, 100], ARROW_RIGHT),
    ([1, 1, 100], ARROW_UP),
    ([100, 100, 1], ARROW_DOWN),
    ([0, 3, 6], ARROW_UP_RIGHT),
    ([6, 3, 0], ARROW_DOWN_RIGHT),
    ([1, 1, 2], ARROW_RIGHT)
])
def test_tendency(input_data, expected):
    assert get_tendency(input_data) == expected
