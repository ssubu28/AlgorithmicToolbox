#Uses python3

import sys

def max_dot_product_notmax(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


def max_dot_product(a, b):
    total = 0
    l = len(a)

    a.sort(reverse = True)
    b.sort(reverse = True)

    for i in range(l):
        total += a[i] * b[i]

    return total


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    #print(max_dot_product_notmax(a, b))
    print(max_dot_product(a, b))
    
