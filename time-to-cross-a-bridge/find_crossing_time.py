import heapq
import math

MOVING_LEFT = 0
MOVING_RIGHT = 1

class Solution:
    def findCrossingTime(self, n: int, k: int, time: list[list[int]]) -> int:
        # Work out the efficiency (as a negative), and the index
        efficiencies = [(0 - leftToRight - rightToLeft, -i) for i, (leftToRight, pickOld, rightToLeft, putNew) in enumerate(time)]
        #print(f"**** Workers ****")
        #for e in sorted(efficiencies):
        #    print(f"{e}")
        #print("*********************")
        waiting_on_left = [e for e in efficiencies]
        heapq.heapify(waiting_on_left)
        waiting_on_right = []
        crossing_bridge = None  # (time_it_finishes, index)
        picking_old = [] # (time_it_finishes, index)
        putting_new = [] # (time_if_finishes_index)

        t = 0
        while(True):
            if n == 0 and not crossing_bridge and not picking_old and not waiting_on_right:
                #print(f"t = {t}: finished")
                return t
            elif crossing_bridge and crossing_bridge[0] == t:
                time_it_finishes, i, direction = crossing_bridge
                leftToRight, pickOld, rightToLeft, putNew = time[i]
                if direction == MOVING_LEFT:
                    #print(f"t = {t}: worker {i} leaves bridge, now putting new")
                    heapq.heappush(putting_new, (t + putNew, i))
                else:
                    #print(f"From {t} to {t + pickOld}: worker {i} picks up a box from the old warehouse")
                    heapq.heappush(picking_old, (t + pickOld, i))
                crossing_bridge = None
            elif picking_old and picking_old[0][0] == t: # picking old
                time_it_finishes, i = heapq.heappop(picking_old)
                leftToRight, pickOld, rightToLeft, putNew = time[i]
                #print(f"t = {t}: worker {i} queues up to cross the bridge to the left bank")
                heapq.heappush(waiting_on_right, efficiencies[i])
            elif putting_new and putting_new[0][0] == t and n:
                time_it_finishes, i = heapq.heappop(putting_new)
                leftToRight, pickOld, rightToLeft, putNew = time[i]
                #print(f"t = {t}: worker {i} queues up to cross the bridge to the right bank")
                heapq.heappush(waiting_on_left, efficiencies[i])
            elif not crossing_bridge and waiting_on_right:
                e, iNeg = heapq.heappop(waiting_on_right)
                i = 0 - iNeg
                leftToRight, pickOld, rightToLeft, putNew = time[i]
                #print(f"From {t} to {t + rightToLeft}: worker {i} crosses the bridge from the right bank to the left bank")
                crossing_bridge = (t + rightToLeft, i, MOVING_LEFT)
            elif not crossing_bridge and waiting_on_left and n:
                e, iNeg = heapq.heappop(waiting_on_left)
                i = 0 - iNeg
                leftToRight, pickOld, rightToLeft, putNew = time[i]
                n -= 1
                #print(f"From {t} to {t + leftToRight}: worker {i} crosses the brodge from the left bank to the right bank")
                crossing_bridge = (t + leftToRight, i, MOVING_RIGHT)
            else:
                t = math.inf
                if crossing_bridge:
                    t = min(t, crossing_bridge[0])
                if picking_old:
                    t = min(t, picking_old[0][0])
                if n and putting_new:
                    t = min(t, putting_new[0][0])
