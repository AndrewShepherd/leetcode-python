import heapq

MODULO = 10**9 + 7

prime_scores = [0] * 100002
for i in range(2, len(prime_scores)):
    if prime_scores[i] == 0:
        prime_scores[i] = 1
        for j in range(i*2, len(prime_scores), i):
            prime_scores[j] += 1

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:

        prime_index_lookups = [prime_scores[n] for n in nums]
        max_prime_score = max(prime_index_lookups)
        forward_lookups = [[-1] * len(nums) for _ in range(max_prime_score+1)]
        for i,p in enumerate(prime_index_lookups):
            for j in range(p+1):
                forward_lookups[j][i] = i
            if i > 0:
                for j in range(p+1, len(forward_lookups)):
                    forward_lookups[j][i] = forward_lookups[j][i-1]
        result = 1

        backward_lookups = [[len(nums)] * len(nums) for _ in range(max_prime_score+2)]
        for i in range(len(prime_index_lookups)-1, -1, -1):
            p = prime_index_lookups[i]
            for j in range(p+1):
                backward_lookups[j][i] = i 
            if i < len(prime_index_lookups) - 1:
                for j in range(p+1, len(backward_lookups)):
                    backward_lookups[j][i] = backward_lookups[j][i+1]

        nums_and_indexes = [(0-n, i) for i,n in enumerate(nums)]
        heapq.heapify(nums_and_indexes)
        while k:
            nNegative, index = heapq.heappop(nums_and_indexes)
            n = 0 - nNegative
            n_prime_score = prime_scores[n]
            right_most_index = len(nums) - 1 if index == len(nums) - 1 else backward_lookups[n_prime_score+1][index+1] - 1            
            left_most_index = 0 if index==0 else (forward_lookups[n_prime_score][index-1] + 1)
            power = (right_most_index - index + 1) * (index - left_most_index + 1)
            power = min(power, k)
            k -= power
            result = result * pow(n, power, MODULO) % MODULO
        return result
        
