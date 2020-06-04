# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_fast(n):

    if n <= 1:
        return n
    
    prev, cur = 0, 1
    f = [0,1]
    # m = 100 since we need last digit
    for i in range(100):
        prev, cur = cur, (prev + cur) % 10
        f.append(cur%10) # If this line is added after if statement, f will only contain 61 items and not 62.

        if prev == 0 and cur ==1:
            break
    # Length of pisano period for m=10 is 60 but list f will contain 61 or 62 elements. 
    length = i + 1
    r = n % length
    result = (f[r] * f[r+1]) % 10
    
    return result




if __name__ == '__main__':
    #n = int(stdin.read())
    n = int(input())
    #print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares_fast(n))
