import math
import pytest
from day14.finders import bisect, secant

# print([e[:2] for e in [examples+aoc_examples1+aoc_examples2]])
# @pytest.mark.parametrize("test_input,expected", )


def fx_x(x): return x
def fx_3x(x): return 3*x
def fx_sqrtx(x): return math.sqrt(x)


test_input = [(fx_x, 5, (1, 100), 5),
              (fx_3x, 5, (1, 10), 1),
              (fx_sqrtx, 5, (1, 100), 25)]


@pytest.mark.parametrize("function,target,interval,expected", test_input)
def test_bisect(function, target, interval, expected):
    result, _ = bisect(function, target, interval)
    assert result == expected


@pytest.mark.parametrize("function,target,interval,expected", test_input)
def test_secant(function, target, interval, expected):
    result, _ = secant(function, target, interval)
    assert result == expected
