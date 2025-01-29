def bisection_function(f, a, b, tol=1e-6, max_iter=1000):


    # Input validation
    if a >= b:
        raise ValueError("Invalid interval: a must be less that b")
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    
    # Bisection algorithm
    i = 0
    while (b-a)/2 >tol and i<max_iter:
        c = (a + b)/2 # Calculate midpoint
        if f(c)==0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i+=1
    return (a+b)/2