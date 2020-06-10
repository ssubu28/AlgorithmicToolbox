# Uses python3
import sys

"""
sys.stdin.read() → For multi line. Press Ctrl d to end entering inputs.
sys. stdin. readline() → For single line. Press Enter to end the input.

"""

# O(n^2)
def get_optimal_value_slow(capacity, weights, values):
    value = 0.0000
    a = []
    l = len(values)

    for i in range(l):
        a.append(values[i]/weights[i])

    while capacity > 0:
        ind = a.index(max(a))

        if capacity > weights[ind]:
            value += a[ind] * (weights[ind])
            capacity -= weights[ind]
        else:
            value += a[ind] * capacity
            capacity = 0
            
        weights[ind], values[ind], a[ind] = -1, -1, -1

    return value


# O(nlogn)
def get_optimal_value(capacity, weights, v):
    total_value = 0.0000
    b = []
    k = 0
    l = len(values)

    for i in range(l):
        b.append(values[i]/weights[i])

    new_list = list(zip(b, values, weights))
    new_list.sort(key= lambda x: x[0], reverse=True)

    while capacity > 0 and k < l:
        if capacity > (new_list[k])[2]:
            total_value += (new_list[k])[0] * (new_list[k])[2]
            capacity = capacity - (new_list[k])[2]
        else:
            total_value += (new_list[k])[0] * capacity
            capacity = 0
        k += 1

    return total_value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    #opt_value_slow = get_optimal_value_slow(capacity, weights, values)
    #print("{:.4f}".format(opt_value_slow))

    opt_value_fast = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value_fast))