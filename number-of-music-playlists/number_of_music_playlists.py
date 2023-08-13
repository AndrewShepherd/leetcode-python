from functools import cache

MODULUS = 1000000007

def fact(n):
    result = 1
    for v in range(1, n+1):
        result = result * v % MODULUS
    return result

@cache
def solve_rec(goal : int, must_use: int, available: int,  k):
    if (goal == must_use):
        return fact(goal)
    
    if k < 0:
        available += 1

    result = 0
    if must_use:
        result = (result + must_use * solve_rec(goal - 1, must_use - 1, available, k - 1)) % MODULUS
    if available:
        result = (result + available * solve_rec(goal - 1, must_use, available - 1, k - 1)) % MODULUS

    return result


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        return solve_rec(goal, n, 0, k)
