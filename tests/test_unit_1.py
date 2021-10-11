import pytest
from ..pattern_code import function_sum


def test_function_sum():
    otp = function_sum(1,2)
    assert otp == 3