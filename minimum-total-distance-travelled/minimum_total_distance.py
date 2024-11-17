import math

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory_indexes = []
        for index,count in factory:
            factory_indexes.extend([index] * count)
        factory_indexes.sort()
        dp = [0] * len(factory_indexes)
        for r_index,r in enumerate(robot):
            dp2 = [math.inf] * len(factory_indexes)
            for f_index in range(r_index, len(factory_indexes)):
                f = factory_indexes[f_index]
                if (r_index == 0):
                    if (f_index == 0):
                        dp2[f_index] = abs(r - f)
                    else:
                        dp2[f_index] = min(dp2[f_index-1],abs(r-f))
                else:
                    dp2[f_index] = min(dp2[f_index-1], abs(r-f) + dp[f_index-1])
            dp = dp2

        return dp[-1]