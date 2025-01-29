import pytest
from math import sin
import functions as fn

def test_linear_function():
    f = lambda x: x - 2 # Test simple linear function
    root = fn.bisection_function(f, 0, 3)
    assert round(root, 6) == 2

def test_quadratic_function():
    f = lambda x: x**2 - 4 # Test a quadratic function
    root = fn.bisection_function(f, 1, 3)
    assert round(root, 6) == 2

def test_trigonometric_function():
    f = lambda x: sin(x) # Test a sin function
    root = fn.bisection_function(f, 2, 4)
    assert round(root, 6) == 3.141593

def test_error_handling_interval():
    f = lambda x: x - 2 # Test a linear function
    with pytest.raises(ValueError):
        fn.bisection_function(f, 4, 3) # it should raise an error, since a>b

def test_error_handling():
    f = lambda x: x**2 + 1 # Test a quadratic function that does not have a root in (any) interval [a,b]
    with pytest.raises(ValueError):  # Expecting a ValueError
        fn.bisection_function(f, 0, 2) # it shoulf raise an error since f(a) and f(b) are both positive

def test_mechanics_example():
    # Example: Find the equilibrium position of a spring-mass system:  f(x) = kx - mg, where k = 10 N/m, m = 1 kg, g = 9.81 m/s²
    k, m, g = 10, 1, 9.81
    f = lambda x: k * x - m * g
    root = fn.bisection_function(f, 0, 2)
    assert round(root, 5) == round(m * g / k, 5)


