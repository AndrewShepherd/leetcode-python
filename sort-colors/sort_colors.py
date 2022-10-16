class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pLeft = 0
        pRight = len(nums) - 1
        
        while pLeft < len(nums) and nums[pLeft] == 0:
            pLeft += 1
            if pLeft == len(nums):
                return
        while pRight >= 0 and nums[pRight] == 2:
            pRight -= 1
            if pRight < 0:
                return
        i = pLeft
        while i <= pRight:
            if nums[i] == 2:
                nums[pRight], nums[i] = nums[i], nums[pRight]
                while pRight > 0 and nums[pRight] == 2:
                    pRight -= 1
            if i <= pRight and nums[i] == 0:
                nums[pLeft], nums[i] = nums[i], nums[pLeft]
                pLeft += 1
            i += 1

