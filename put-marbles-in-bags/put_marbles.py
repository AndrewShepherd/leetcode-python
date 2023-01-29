import heapq

class Solution:
    # How many discretionary numbers can you pick
    def calc_q_length(k):
        if k == 1:  #[n-n]
            return 0
        elif k == 2: #[n,0][1,n]
            return 2
        elif k == 3:
            return 4 
    
    def putMarbles(self, weights: list[int], k: int) -> int:
        

        queue_length = (k-1)*2
        min_q = []
        max_q = []
        for w in weights:
            if len(min_q) < queue_length:
                heapq.heappush(min_q, w)
                heapq.heappush(max_q, w)
            else:
                heapq.heappushpop(min_q, 0-w)
                heapq.heappushpop(max_q, w)
        return abs(sum(min_q) - sum(max_q))
