class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_length = len(nums1) + len(nums2)
        t_index_1 = (total_length-1)//2
        t_index_2 = (total_length)//2
        if len(nums1) == 0:
            return (nums2[t_index_1] + nums2[t_index_2]) / 2
        if len(nums2) == 0:
            return (nums1[t_index_1] + nums1[t_index_2]) / 2
        
        i1 = -1
        i2 = -1
        
        while(True):
            v = None
            if (i1 == len(nums1)-1):
                i2 += 1
                v = nums2[i2]
            elif (i2 == len(nums2)-1):
                i1 += 1
                v = nums1[i1]
            elif nums1[i1+1] <= nums2[i2+1]:
                i1 += 1
                v = nums1[i1]
            else:
                i2 += 1
                v = nums2[i2]
            combined_index = i1 + i2 + 1
            if combined_index == t_index_1:
                m1 = v
            if combined_index == t_index_2:
                m2 = v
                break
        return (m1 + m2) / 2
