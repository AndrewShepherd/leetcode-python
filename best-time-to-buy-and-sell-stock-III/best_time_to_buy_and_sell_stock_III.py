
# Kadane's algorithm, copied and pasted from wikipedia
def max_subarray(numbers):
    """Find a contiguous subarray with the largest sum."""
    best_sum = 0  # or: float('-inf')
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' match Python's slice convention (endpoint excluded)

    return best_sum, best_start, best_end

class Solution(object):
    def maxProfit(self, prices): 
        deltas = [p2-p1 for (p1, p2) in zip(prices[:-1], prices[1:])]
        
        best_run, best_start, best_end = max_subarray(deltas)
        best_before = max_subarray(deltas[:best_start])[0]
        best_after = max_subarray(deltas[best_end:])[0]
        biggest_downcycle = max_subarray([0-d for d in deltas[best_start:best_end]])[0]

        return best_run + max((
            best_before,
            best_after,
            biggest_downcycle
        ))
