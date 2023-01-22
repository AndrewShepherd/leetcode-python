class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 1
        current = 0
        for n in [int(c) for c in s]:
            if n > k:
                return -1
            current = current * 10 + n
            if current > k:
                count += 1
                current = n
        return count
