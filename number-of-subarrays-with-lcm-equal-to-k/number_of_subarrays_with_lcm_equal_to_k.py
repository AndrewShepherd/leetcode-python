def gcd(l, r):
    l,r = min(l,r), max(l,r)
    if r%l == 0:
        return l
    else:
        return gcd(l, r%l)

def lcm(l, r):
    return l*r // gcd(l, r)


class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            l = nums[i]
            for j in range(i, len(nums)):
                n = nums[j]
                l = lcm(l, n)
                if l == k:
                    count += 1
                elif l > k:
                    break
        return count
