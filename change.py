# Uses python3
#import sys

def get_change(m):
    #write your code here
    count = 0
    denominations = [10,5,1]
    i = 0

    while m > 0:
        if i < len(denominations) and m >= denominations[i]:
            x = m // denominations[i]
            count += x
            m -= (x * denominations[i])   # m here is smaller than denomination[i] max value of i (remainder is less than divisor). start with max
            i += 1
        elif m < denominations[i]:
            i += 1

    return count






if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))