class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        s = sum(nums)

        if target == s:
            return len(nums)
        
        add_amount = (target // s) * len(nums)
        target %= s

        if target == 0:
            return add_amount

        nums = nums + nums
        best_result = None
        d = dict()
        accumulation = 0
        d[0] = [0]
        for i,n in enumerate(nums):
            accumulation += n
            this_result = None
            if accumulation == target:
                this_result = i + 1
            elif accumulation > target:
                diff = accumulation - target
                if diff in d:
                    this_result = i + 1 - d[diff] # Possible off-by-one
            if this_result != None:
                best_result = this_result if best_result == None else min(this_result, best_result)
            d[accumulation] = i + 1
        return -1 if best_result == None else best_result + add_amount

