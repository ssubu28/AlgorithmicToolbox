# python3
import sys


def compute_min_refills(distance, tank, stops):

    lastrefill_distance = -1
    curpos = -1
    minstops = 0
    dt = 0


    while dt < distance:

        while curpos < len(stops) and dt < distance:

            if lastrefill_distance == -1 and curpos == -1:
                if stops[curpos+1] > tank:
                    return -1 # impossible
                else:
                    curpos += 1  # increment to 0
                    dt = stops[curpos]
                    lastrefill_distance = 0
                    lastrefill_index = -1
                    
            else:
                if stops[curpos + 1] - lastrefill_distance > tank: # and lastrefill_index != curpos ? 
                    if lastrefill_index == curpos: # impossible as in-between dist is > m
                        return -1
                    lastrefill_distance = stops[curpos]
                    lastrefill_index = curpos
                    minstops += 1 # Updating number of stops
                    dt = stops[curpos]
                else:
                    curpos += 1
                    dt = stops[curpos]
                       
            # Can also increment minstops where lastrefill_index is getting updated
            
            #if curpos == lastrefill_index: 
                #minstops += 1
            

    return minstops






if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    stops.append(d)
    print(compute_min_refills(d, m, stops))