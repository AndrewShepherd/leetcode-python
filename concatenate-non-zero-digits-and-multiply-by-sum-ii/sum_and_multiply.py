MODULO = 10**9 + 7

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        concatenations = [None] * len(s)
        sums = [None] * len(s)
        non_zero_counts = [None] * len(s)
        agg_sum = 0
        agg_cat = 0
        non_zero_count = 0
        for i,d in enumerate([ord(c) - ord('0') for c in s]):
            agg_sum = (agg_sum + d) % MODULO
            if (d != 0):
                agg_cat = (agg_cat * 10 + d) % MODULO
                non_zero_count += 1
            concatenations[i] = agg_cat
            sums[i] = agg_sum
            non_zero_counts[i] = non_zero_count
        result = []
        for l,r in queries:
            this_result = 0
            right_sum = sums[r]
            right_concatenation = concatenations[r]
            right_length = non_zero_counts[r]
            if (l != 0):
                left_sum = sums[l-1]
                left_contatenation = concatenations[l-1]
                left_length = non_zero_counts[l-1]
            else:
                left_sum, left_contatenation, left_length = (0, 0, 0)
                
            
            sum_result = (right_sum - left_sum) % MODULO
            length_result = right_length - left_length
            concat_result = (right_concatenation - left_contatenation * pow(10, length_result, MODULO)) % MODULO
            this_result = (sum_result * concat_result) % MODULO
            result.append(this_result)

        return result
