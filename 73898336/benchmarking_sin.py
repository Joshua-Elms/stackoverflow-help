from math import sin
from time import perf_counter as pf

def slower(xvals):
    a = []
    for val in xvals:
        a.append(sin(val))
    return a

def faster(xvals, f = sin):
    a = []
    for val in xvals:
        a.append(f(val))
    return a



if __name__=="__main__":
    vals = [i for i in range(10_000_000)]
    start = pf()
    slower(vals)
    stop = pf()
    slow = stop - start

    start = pf()
    faster(vals)
    stop = pf()
    fast = stop - start

    f = sin
    start = pf()
    a = []
    for val in vals:
        a.append(f(val))
    stop = pf()
    fastest = stop - start

    start = pf()
    a = [sin(val) for val in vals]
    stop = pf()
    fastest = stop - start


    print(f"Global Version: {slow} s\nLocal Version: {fast} s\nAhmed: {fastest} s")