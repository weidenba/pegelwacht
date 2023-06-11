import pytest

from helper.data_conversion import string_to_float


@pytest.mark.parametrize('input_data, separator, expected', [
    ('1', ',', 1),
    ('1,2', ',', 1.2),
    (' 1.5 ', ',', 1.5)
])
def test_string_to_float(input_data, separator, expected):
    assert string_to_float(input_data, float_separator=separator) == expected
