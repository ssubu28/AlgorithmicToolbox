# Uses python3
#import sys
import random

"""
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
"""


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous % 10 + current % 10) % 10

    return current



if __name__ == '__main__':
    #input = sys.stdin.read()
    
    n = int(input("Enter a number n: "))

    """
    # Stress test with random num gen
    for i in range(10):
        n = random.randint(0, 10000000)

        #print(f"Iteration {i} where n = {n}")
        #print(f"Output with Algorithm 1: {get_fibonacci_last_digit_naive(n)}")
        #print(f"Output with Algorithm 2: {get_fibonacci_last_digit_fast(n)}")
    """

    print(f"Output with Algorithm 2: {get_fibonacci_last_digit_fast(n)}")
