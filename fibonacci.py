# Uses python3

"""
def calc_fib_slow(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    # we are storing the entire array
    if n <= 1:
        return n
    f = [0,1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
"""

def calc_fib_best(n):
    # No array
    if n <= 1:
        return n
    p1 = 0
    p2 = 1
    for i in range(2, n+1):
        p1, p2 = p2, (p1 + p2)
    return p2




n = int(input())

#print(calc_fib_slow(n))
#print(calc_fib_fast(n))

print(calc_fib_best(n))