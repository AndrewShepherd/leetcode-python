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
        
        q = []
        s = [(prime_index_lookups[0], 0)]
        for i in range(1, len(prime_index_lookups)):
            while s and s[-1][0] < prime_index_lookups[i]:
                earlier_score, middle_index = s.pop()
                first_index = 0 if not s else s[-1][1] + 1
                power = (i - middle_index) * (middle_index - first_index + 1)
                q.append((0 - nums[middle_index], power))
            s.append((prime_index_lookups[i], i))
        while s:
            prime_score, index = s.pop()
            first_index = 0 if not s else s[-1][1] + 1
            power = (len(nums) - index) * (index - first_index + 1)
            q.append((0 - nums[index], power))

        heapq.heapify(q)
        result = 1
        while k:
            n_negative, available = heapq.heappop(q)
            power = min(available, k)
            result = result * pow(0 - n_negative, power, MODULO) % MODULO
            k -= power
        return result

        return 0

        
