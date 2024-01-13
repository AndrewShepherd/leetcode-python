# pick numbers in the following order:

# From the array with the smallest number of distinct values that are not in the other set
# From the array with the highest number of distinct values that are not in the higher set
# From the array with the smallest number of distinct values
# From the array with the highest 

class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)

        result = set()
        if len(s2) < len(s1):
            s1,s2 = s2,s1
        
        discards = set()
        for n in s1:
            if n in result:
                continue
            elif n in s2:
                discards.add(n)
            else:
                result.add(n)
                if len(result) == len(nums1) // 2:
                    break

        for n in discards:
            if len(result) == len(nums1) // 2:
                break
            result.add(n)

        
        items_taken = 0
        for n in s2:
            if n in result:
                continue
            else:
                result.add(n)
                items_taken += 1
                if items_taken == len(nums1) // 2:
                    break
        return len(result)