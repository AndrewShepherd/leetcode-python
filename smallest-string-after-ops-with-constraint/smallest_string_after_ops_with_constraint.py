def smallest_number(s, k):
    if (k == 0):
        return (s, 0)
    for n in range(26):
        r1 = (n-s)%26
        r2 = (s-n)%26
        this_cost = min(r1, r2)
        if(this_cost <= k):
            return (n, this_cost)

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        as_numbers = [ord(c) - ord('a') for c in s]
        result = []
        for n in as_numbers:
            n2, cost = smallest_number(n, k)
            result.append(n2)
            k -= cost
        result_string = "".join([chr(n + ord('a')) for n in result])
        return result_string
