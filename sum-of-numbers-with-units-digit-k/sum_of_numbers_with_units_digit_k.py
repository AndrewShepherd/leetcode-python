from functools import cache

def set_size(num, k):
    for size in range(1, 11):
        if size*k % 10 == num % 10:
            return size
    return None

@cache
def number_of_ways(t, s, m):
    # Brute force
    if s == 0 and t == 0:
        return 1
    if t < 0:
        return 0
    if m > t:
        return 0
    if m > 9:
        return 0
    including = number_of_ways(t-m, s-1, m+1) + number_of_ways(t-m, s, m)
    not_including = number_of_ways(t, s, m + 1)
    return including + not_including

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        # How many in the set?
        s = set_size(num, k)
        if s == None:
            return -1
        if k*s > num:
            return -1
        return s
        target = num - k * s
        result = number_of_ways(target//10, s, 0)
        return -1 if result == 0 else s