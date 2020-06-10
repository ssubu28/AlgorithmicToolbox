# Uses python3
import sys

def optimal_summands(n):
    summands = []
    k = 1
    total = 0

    while total < n and k < n:
        total += k
        summands.append(k)
        k += 1

    if total > n:
        diff = total - n
        summands.remove(diff)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    #print(len(summands))
    print(summands[-1])
    for x in summands:
        print(x, end=' ')
