# python3
import time

def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = 0
    index2 = 0

    for i in range(n):
        if numbers[i] >= numbers[index1]:
            index1 = i

    if index1 == 0:
        index2 = index1 + 1

    for j in range(n):
        if numbers[j] >= numbers[index2] and j != index1:
            index2 = j

    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
    print(time.process_time())