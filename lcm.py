# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


def lcm_fast(a, b):
    result = gcd(a, b)
    return a*b//result



if __name__ == '__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    #print(lcm_naive(a, b))
    print(lcm_fast(a, b))

