import math

# Rounding is necessary 
# because of floating-point innaccuracies
# eg math.log(5**9, 9) == 4.99999999999999
def rounded_floor(n):
    return math.floor(round(n, 13))

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        if multiplier == 1:
            return nums
        
        q = sorted([(math.log(n, multiplier), i) for i,n in enumerate(nums)])
        exponents = [0] * len(nums)

        cumulative_floor_sums = [rounded_floor(n) for n, i in q]
        for i in range(1, len(cumulative_floor_sums)):
            cumulative_floor_sums[i] += cumulative_floor_sums[i-1]
        
        # Now we try and level it so that they all have the same floor values
        last_failed_index = None
        for index in range(len(cumulative_floor_sums)-1, 0, -1):
            this_floor = rounded_floor(q[index][0])
            len_before = index 
            required_sum_before = this_floor * len_before
            actual_sum_before = cumulative_floor_sums[index-1]
            required_increments = required_sum_before - actual_sum_before
            if required_increments <= k:
                for j in range(0, index):
                    n,i = q[j]
                    delta = this_floor - rounded_floor(n)
                    q[j] = (n + delta, i)
                    exponents[i] += delta
                    k -= delta
                break
            last_failed_index = index

        if last_failed_index != None:
            amount_to_add_to_each = k//last_failed_index
            for index in range(last_failed_index):
                existing_amount, item_index = q[index]
                exponents[item_index] += amount_to_add_to_each
                q[index] = (existing_amount + amount_to_add_to_each, item_index)
            k %= last_failed_index
        else:
            #Assign the rest of k evenly
            if k >= len(nums):
                for_everyone = k // len(nums)
                exponents = [n + for_everyone for n in exponents]
                q = [(n + for_everyone, i) for n,i in q]
            k %= len(nums)

        #Assign what's left of k
        if k:
            q.sort()
            for index in range(k):
                n,i = q[index]
                exponents[i] += 1
        
        MODULO = 10**9 + 7
        return [n * pow(multiplier, exponents[i], MODULO) % MODULO for i,n in enumerate(nums)]
