import bisect

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # Must first find a number that doesn't equal the first number
        leftMinimum, leftKnownMax = 0, 0
        rightMax, rightKnownMin = len(nums)-1, len(nums)-1

        sampleRanges = [(0, len(nums))]
        while(True):
            (l, r) = sampleRanges.pop(0)
            if (r <= l):
                return False
            midPoint = (l + r)//2
            midValue = nums[midPoint]
            if midValue == target:
                return True
            if (midValue == nums[0]):
                sampleRanges.extend([(l, midPoint), (midPoint, r)])
            elif (midValue > nums[0]):
                leftKnownMax = midPoint
                break
            else:
                rightKnownMin = midPoint
                break

        while(True):
            leftMinValue = nums[leftMinimum]
            leftKnownMaxValue = nums[leftKnownMax]
            rightKnownMinValue = nums[rightKnownMin]
            rightMaxValue = nums[rightMax]
            if leftMinValue <= target <= leftKnownMaxValue:
                return nums[bisect.bisect_left(nums, target, leftMinimum, leftKnownMax+1)] == target
            if rightKnownMinValue <= target <= rightMaxValue:
                return nums[bisect.bisect_left(nums, target, rightKnownMin, rightMax+1)] == target
            if (rightKnownMin - leftKnownMax) <= 1:
                return False
            midPoint = (rightKnownMin + leftKnownMax + 1)//2
            midValue = nums[midPoint]
            if midValue == target:
                return True
            if midValue >= leftKnownMaxValue:
                leftKnownMax = midPoint
            if midValue <= rightKnownMinValue:
                rightKnownMin = midPoint

        return (leftMinimum, leftKnownMax, rightKnownMin, rightMax)
