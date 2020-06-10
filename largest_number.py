#Uses python3

import sys

def IsGreaterOrEqual(digit, maxnum):

    l1 = len(str(digit))
    l2 = len(str(maxnum))

    if l1 < l2:
        val_digit = str(digit) + abs(l2 - l1) * str(digit)
        val_maxnum = str(maxnum)
    elif l1 > l2:
        val_maxnum = str(maxnum) + abs(l2 - l1) * str(maxnum)
        val_digit = str(digit)
    else:
        val_digit = str(digit)
        val_maxnum = str(maxnum)

    if int(val_digit) >= int(val_maxnum):
        return True

    return False





def largest_number(a):

    l = len(a)
    maxnum, i = -1, 0
    A = ""

    while i < l:
        maxdigit = -1
        for digit in a:
            #if str(digit) >= str(maxdigit):
            if IsGreaterOrEqual(digit, maxdigit):
                maxdigit = digit
        A += maxdigit
        a.remove(maxdigit)

        i += 1

    return A





   

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
