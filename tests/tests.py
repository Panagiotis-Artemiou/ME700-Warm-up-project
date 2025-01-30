import pytest
from math import sin
from src import functions as fn
import numpy as np

def test_midpoint():
    a = 10.1
    b = 20
    c = fn.midpoint(a, b)
    assert np.isclose(20.1, c)


def test_check_interval_valid():
    fn.check_interval(1, 2) # This should not raise an error

def test_check_interval_invalid():
    with pytest.raises(ValueError, match="Invalid interval: a must be less that b."):
        fn.check_interval(2, 2)
    with pytest.raises(ValueError, match="Invalid interval: a must be less that b."):
        fn.check_interval(3, 1)


def test_check_signs_valid():
    fn.check_signs(1, 2, -1, 1) # No error should be raised

def test_check_signs_invalid():
    with pytest.raises(ValueError, match="There is 0 or even number of roots in interval [a, b]. Valid interval must contain only 1 root."):
        fn.check_signs(1, 2, 1, 1)


# Test the main function 
def f(x):
    return x**2 - 4 # Define a simple quadratic continuus function

def test_bisection_function_valid():
    # Test case where the root is within the interval [a, b]
    result = fn.bisection_function(f, 1, 3)  # Root is at x = 2
    assert abs(result[0] - 2) < 1e-6, f"Expected root close to 2, but got {result[0]}"
    assert result[1] < 1000, f"Expected number of iterations to be less than 1000, but got {result[1]}"
    assert len(result[2]) > 1, "Expected more than one midpoint value"

def test_bisection_function_convergence():
    # Test for function that doesn't converge in the given number of iterations
    result = fn.bisection_function(f, 1, 3, max_iter=5)  # Force the maximum number of iterations
    assert result[1] == 5, f"Expected 5 iterations, but got {result[1]}"

def test_bisection_function_root_found_at_midpoint():
    # Test case where the root is found at the midpoint of the interval
    result = fn.bisection_function(f, 0, 3)  # Root is at x = 2
    assert abs(result[0] - 2) < 1e-6, f"Expected root close to 2, but got {result[0]}"
    assert result[1] == 1, f"Expected 1 iteration, but got {result[1]}"