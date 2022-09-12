import math

def binarySearch(l, val, start, end):
    if start >= end:
        return start
    tryThisIndex = (start+end)//2
    tryThisVal = l[tryThisIndex][0]
    if tryThisVal == val:
        return tryThisIndex
    elif tryThisVal > val:
        return binarySearch(l, val, start, tryThisIndex)
    else:
        return binarySearch(l, val, tryThisIndex+1, end)

def doesOverride(higherEntry, lowerEntry):
    higher_value, higher_score = higherEntry
    lower_value, lower_score = lowerEntry
    higher_possible_score = lower_score + higher_value - lower_value
    return higher_possible_score < higher_score

class Solution:
    def lengthOfLIS(self, nums, k: int) -> int:
        if not nums:
            return 0
        l = []
        for n in nums:
            i = binarySearch(l, n-k, 0, len(l))
            max_before = 0
            while True:
                if i >= len(l):
                    new_entry = (n, max_before+1)
                    l.append(new_entry)
                    break
                elif l[i][0] > n:
                    new_entry = (n, max_before+1)
                    if not doesOverride(l[i], new_entry):
                        l.insert(i, new_entry)
                    else:
                        new_entry = None
                    break
                elif l[i][0] == n:
                    new_entry = (n, max(l[i][1], max_before+1))
                    l[i] = new_entry
                    break
                elif (n-l[i][0] <= k):
                    max_before = max(max_before, l[i][1])
                    i += 1
                else:
                    i += 1
            # Now go backwards, removing the ones that we know are not relevant
            if new_entry:
                j = i-1
                while (j>=0):
                    if (doesOverride(new_entry, l[j])):
                        del l[j]
                        j -= 1
                    else:
                        break
        return max(a[1] for a in l)
