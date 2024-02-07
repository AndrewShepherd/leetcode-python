from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        counter = Counter(nums)
        used = set()
        best_so_far = 0
        for n,c in sorted(counter.items()):
            if n in used:
                break
            elif c == 1:
                best_so_far = max(best_so_far, 1)
            elif n == 1:
                best_so_far = c - 1 if c%2 == 0 else c
            else:
                length = 1
                while True:
                    n = n * n
                    if n in counter:
                        length += 1 # for going down again
                        used.add(n)
                        length += 1 # for this one
                        if counter[n] == 1:
                            break
                    else:
                        break
                best_so_far = max(best_so_far, length)
        return best_so_far