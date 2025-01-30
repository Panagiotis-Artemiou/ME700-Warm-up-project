import numpy as np

def midpoint(a:float, b:float):
    c = (a + b) / 2
    return c


def check_interval(a:float, b:float):
    if a >= b:
        raise ValueError("Invalid interval: a must be less that b.")


def check_signs(a:float, b:float, fa:float, fb:float):
    if fa * fb > 0:
        raise ValueError("There is 0 or even number of roots in interval [a, b]. Valid interval must contain only 1 root.")
    

def bisection_function(f, a, b, tol=1e-6, max_iter=1000):

    # Input validation
    check_interval(a, b)
    fa, fb = f(a), f(b)
    check_signs(a, b, fa, fb)
    
    # Save values for plots
    a_list = []
    b_list = []
    fa_list = []
    fb_list = []
    # Add initial values
    a_list.append(a)
    fa_list.append(f(a))
    b_list.append(b)
    fb_list.append(f(b))
    
    # Bisection algorithm
    i = 0
    while (b - a) / 2 > tol and i < max_iter:
        c = midpoint(a, b) # Calculate midpoint
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
            b_list.append(b)
            fb_list.append(f(b))
        else:
            a = c
            a_list.append(a)
            fa_list.append(f(a))
        i+=1
        root = (a + b) / 2
    return {root, i, a_list, fa_list, b_list, fb_list}