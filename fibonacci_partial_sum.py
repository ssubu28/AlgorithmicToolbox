# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_prev(from_, to):
    if to <= 1:
        return to
    prev, cur = 0, 1
    result = 0

    for i in range(2, to+1):
        prev, cur = cur, (prev + cur) % 10
        if i >= from_:
            result += cur % 10
    
    return result % 10


def fibonacci_partial_sum_fast(from_, to):
    if to <= 1:
        return to
    prev, cur = 0, 1
    result = 0
    f = [0,1]

    for i in range(100):
        prev, cur = cur, (prev+cur) % 10
        f.append(cur)
        if prev == 0 and cur == 1:
            break

    length = i + 1
    # we don't need to add 2. We don't need the sum of r1+2 and r2+2 but just need sum between r1 and r2
    r1 = (from_) % length
    r2 = (to) % length

    if r2 < r1: # If end is less than start because of 0 remainder after modulus
        r2 = r2 + 60

    for k in range(r1, r2+1):
        result += f[k % length]      # % by length to prevent list overflow

    return (result % 10)





if __name__ == '__main__':
    #input = sys.stdin.read();
    from_, to = map(int, input().split())
    #print(fibonacci_partial_sum_naive(from_, to))
    #print(fibonacci_partial_sum_prev(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))