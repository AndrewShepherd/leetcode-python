
# start_ptr has to be a positive
# and has to be preceeded by a negative
def can_be_start_ptr(d, index):
    prev = index - 1
    return d[prev][1] <= 0 and d[index][1] > 0

def get_start_indexes(d):
    return [i for i in range(len(d)) if can_be_start_ptr(d, i)]

def get_ranges(d):
    si = get_start_indexes(d)
    return [(si[i], si[0 if i == len(si)-1 else i+1]) for i in range(len(si))]

def summarise_range(d, r):
    if r[0] == r[1]:
        return (d[r[0]][0], sum([n for _,n in d]))
    i = r[0]
    t = 0
    while(i != r[1]):
        t += d[i][1]
        i = (i + 1) % len(d)
    return (r[0], t)


def reduce(d):
    ranges = get_ranges(d)
    return [summarise_range(d, r) for r in ranges]

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        deltas = [g-c for c,g in zip(cost, gas)]

        d = list(enumerate([g-c for c,g in zip(cost, gas)]))

        while (True):
            if len([1 for index, delta in d if delta >= 0]) == 0:
                return -1
            if len(d) == 1:
                return d[0][0]
            d = reduce(d)
