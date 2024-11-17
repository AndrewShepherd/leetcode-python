class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        def is_valid(index, direction):

            if nums[index] != 0:
                return False
            nums_copy = nums[:]
            while True:
                index += direction
                if not (0 <= index < len(nums_copy)):
                    break
                if nums_copy[index] == 0:
                    None
                else:
                    nums_copy[index] -= 1
                    direction = direction * (-1)
            return all([n == 0 for n in nums_copy])
        
        
        valid_count = 0
        for i in range(len(nums)):
            if is_valid(i, 1):
                valid_count += 1
            if is_valid(i, -1):
                valid_count += 1
        return valid_count
