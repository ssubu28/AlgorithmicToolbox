# Uses python3
#import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10



def fibonacci_sum_prev(n):
    if n <= 1:
        return n
    
    prev, cur = 0, 1
    result = 1
    f = [0,1]

    for i in range(2, n+1):
        prev, cur = cur, (prev + cur)
        result += cur % 10
        f.append(result)
    print(f)

    return result % 10

     

def fibonacci_sum_fast(n):
    prev, cur = 0, 1
    f = [0,1]
    # Using m=10 and sum(4th) term is == f(6th) term. so n+2 instead of n. And instead of adding values, just compute pisano period of n+2th term and subtract 1.

    """
    Logic:
    Fn = 0 1 1 2 3 5 8 13 21 ...
    Sn =     0 1 2 4 7 12 20 ...
    Here, Sn is (n+2)th term of Fn and one value less so subtract 1.
    We have F0 + F1 + … + Fn = F(n+2) — 1

    """

    for i in range(100):
        prev, cur = cur, (prev + cur) % 10
        f.append(cur)
        if prev == 0 and cur == 1:
            break

    length = i+1
    r = (n) % length
    # without % 10, the result is -1.
    return (f[r+2] - 1) % 10



if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    #print(fibonacci_sum_naive(n))
    #print(fibonacci_sum_prev(n))
    print(fibonacci_sum_fast(n))