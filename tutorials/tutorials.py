import numpy as np
from math import sin
from src import functions as fn

# 1. Linear function
# Finding the root of f(x)=x-2 (expected root is x=2)

f1 = lambda x: x - 2
root1 = fn.bisection_function(f1, 0, 3)
print(f"Root of f(x)=x-2 is approximately: {root1}")

# 2. Quadratic function
# Finding the root of f(x) = x^2- 4 (expected root is -2 or 2 depending on initial interval)

f2 = lambda x: x**2 - 4
root2 = fn.bisection_function(f2,-3, 1)
print(f"Root of f(x)= x^2 -2 is approximately: {root2}")

# 3. Trigonometric function
# Find the root fo f(x)=sin(x)

f3 = lambda x: sin(x)
root3 = fn.bisection_function(f3, 1, 4) # in the interval [1, 4] expected root is pi=3.14159
print(f"Root of f(x)=sin(x) is aproximately: {root3}")

# 4. Mechanics example 1
# Find the equilibrium position of as mass-spring system that balances in the vertical direction
# From equation of balance we have that f(x) = kx - mg, where k=10 N/m is the spring constant, m=1 Kg is the mass, and g=9.81 m/s^2 is the acceleration of gravity
k, m, g = 10, 1, 9.81
f4 = lambda x: k*x - m*g
root4 = fn.bisection_function(f4, 0, 3)
print(f"The equilibrium position of the spring-mass system is approximately {root4}")

# 5. Mechanics example 2
# Find the angle theta for which the distance covered by a projectile is maximum.
# The equation that describes the distance covered is x  = (v0^2*sin(2θ))/g where v0 is the initial speed, g the acceleration of gravity and θ the angle
# To maximize that, take the derivative f(θ) = (2*v0^2*cos(2θ))/g

v0=1
f5 = lambda theta: (v0**2 * np.cos(2*theta))/g
root5 =fn.bisection_function(f5, 0, np.pi/2)
print(f"The optimum projectile angle is: {root5}")
