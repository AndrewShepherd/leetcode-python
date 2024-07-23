import heapq

class Solution:
    def clearStars(self, s: str) -> str:

        h = []
        indexes_to_delete = []
        for i,c in enumerate(s):
            if c == '*':
                if (h):
                    character, negative_index = heapq.heappop(h)
                    indexes_to_delete.append(0 - negative_index)
                indexes_to_delete.append(i)
            else:
                heapq.heappush(h, (c, 0 - i))
        last_index = 0
        indexes_to_delete.sort()
        result = ''
        for n in indexes_to_delete:
            result += s[last_index:n]
            last_index = n+1
        result += s[last_index:]
        return result
