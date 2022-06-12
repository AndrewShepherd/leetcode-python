from heapq import heappop, heappush

def solveUsingHeap(cookies, k: int) -> int:
    cookies.sort()

    recipients = [0]*k
        
    for c in reversed(cookies):
        r = heappop(recipients)
        r += c
        heappush(recipients, r)

    return max(recipients)


class Solution:
    def distributeCookies(self, cookies, k: int) -> int:
        cookies.sort()

        recipients = [0]*k
        
        for c in reversed(cookies):
            r = heappop(recipients)
            r += c
            heappush(recipients, r)

        return max(recipients)