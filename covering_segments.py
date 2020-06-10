# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points_old(segments):
    points = []
    #write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

# Will only yeild number of intersections but cannot yeild the intersection point.
def optimal_points_only(segments):
    segments.sort(key=lambda x: x[0], reverse=False)
    l = len(segments)
    i = 0
    m = 0
    a1 = segments[i][0]
    b1 = segments[i][1]

    while i < l-1:

        if (segments[i+1])[0] >= a1 and (segments[i+1])[0] <= b1:
            i += 1

        else:
            m += 1
            i += 1 # move cursor to next point in list as counter is incremented
            a1 = segments[i][0]
            b1 = segments[i][1]

    print(".... Exited while loop ....")
    print (m+1)



    points = []
    #write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points


def optimal_points(segments):

    k = 0
    i = 1
    points = list()

    segments.sort(key=lambda x: x[1], reverse=False)
    l = len(segments)


    while k < l and i < l:

        if segments[i][0] <= segments[k][1] <= segments[i][1]:
            i += 1

        else:
            points.append(segments[k][1])
            k = i
            i = k + 1

    # cond to check after if passes but next while (i+1) breaks
    if i == l and k < l:
        points.append(segments[k][1])

    return points




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))

    points = optimal_points(segments)
    print(len(points))
    print(*points)
