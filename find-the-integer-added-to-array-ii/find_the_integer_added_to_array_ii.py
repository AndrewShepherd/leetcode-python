class Solution:
    def minimumAddedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()
        # Dont remove 0
        diff1 = nums2[0] - nums1[0]
        # remove 0, keep 1
        diff2 = nums2[0] - nums1[1]
        #remove 0 and 1
        diff3 = nums2[0] - nums1[2]

        def test_diff(d):
            left_index = 0
            right_index = 0
            skips = 0
            while(right_index < len(nums2)):
                if nums2[right_index] - nums1[left_index] == d:
                    left_index += 1
                    right_index += 1
                else:
                    skips += 1
                    if skips > 2:
                        return False
                    left_index += 1
            return True

        possibilities= [d for d in (diff1, diff2, diff3) if test_diff(d)]
        return min(possibilities)
