def gcd(smaller, larger):
    if smaller > larger:
        smaller, larger = larger, smaller
    if larger%smaller == 0:
        return smaller
    else:
        return gcd(larger%smaller, smaller)

class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        running_count = 0
        for i,n in enumerate(nums):
            running_gcd = n
            sub_array_end = i
            while(running_gcd % k == 0):
                if running_gcd == k:
                    running_count += 1
                sub_array_end += 1
                if sub_array_end == len(nums):
                    break
                running_gcd = gcd(running_gcd, nums[sub_array_end])
        return running_count


