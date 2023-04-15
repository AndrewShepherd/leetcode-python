def get_ranges(l):
    start = None
    counter = 0
    for index, is_start in l:
        if is_start:
            if counter == 0:
                start = index
            counter += 1
        else:
            counter -= 1
            if counter == 0:
                yield range(start, index, 2)
                start = None

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: list[int], k: int) -> list[int]:

        result = [0 if i == p else -1 for i in range(n)]
        available = [True] * n
        for b in banned:
            available[b] = False
        jumps = 0
        items_with_jumps = [p]
        while items_with_jumps:
            for index in items_with_jumps:
                result[index] = jumps
                available[index] = False
            next_items = []
            odd_starts, even_starts = list(), list()
            for index in items_with_jumps:
                start = max(0, index-k+1)
                end = min(index, n-k)
                first = 2 * start + k - 1 - index
                last = 2 * end + k - 1 - index
                l = odd_starts if (first % 1) else even_starts
                l.append((first, True))
                l.append((last + 2, False))
            for l in odd_starts, even_starts:
                l.sort()
                for r in get_ranges(l):
                    for new_index in r:
                        if available[new_index]:
                            next_items.append(new_index) 
            jumps += 1
            items_with_jumps = next_items
        return result
        
