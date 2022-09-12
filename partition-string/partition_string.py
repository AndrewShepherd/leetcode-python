import math
from functools import cache
class Solution:
    def partitionString(self, s: str) -> int:
        


        if not s:
            return 0
        s = [ord(c) - ord('a') for c in s]
        last_instances = [-1]*26
        partition_start = 0
        partition_count = 0
        for i,n in enumerate(s):
            if last_instances[n] >= partition_start:
                partition_count += 1
                partition_start = i
            last_instances[n] = i
        return partition_count + 1