def odds_and_even(up_to):
    odds = up_to//2 + up_to % 2
    evens = up_to // 2
    return (odds, evens)

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        nOdd, nEven = odds_and_even(n)
        mOdd, mEven = odds_and_even(m)
        return nOdd * mEven + nEven * mOdd
