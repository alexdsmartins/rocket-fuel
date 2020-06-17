import math


def bisect(f, target, interval, args=()):
    """Finds target intersection with f within an interval using the bisect method"""
    iterations = 0
    low, high = interval
    while low <= high:
        iterations += 1
        mid = low + (high-low)//2
        f_mid = f(mid, *args)
        if f_mid == target:
            return (mid, iterations)
        if f_mid < target:
            low = mid + 1
        else:
            high = mid - 1
    return low-1, iterations


def secant(f, target, interval, args=()):
    """Finds target intersection with f within an interval using the secant method"""
    x0, x1 = interval
    iterations = 0
    while(x0 != x1):
        iterations += 1
        fx0 = f(x0, *args)
        fx1 = f(x1, *args)
        m = (fx1-fx0) / (x1-x0)
        x2 = math.floor((target - fx1 + m*x1)/m)
        x0, x1 = x1, x2
    return x0, iterations
