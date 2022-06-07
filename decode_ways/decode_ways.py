class Solution:
    def numDecodings(self, s: str) -> int:
        number_two_ahead, number_one_ahead = None, None
        score_two_ahead, score_one_ahead = None, None
        score = 0
        for n in (int(c) for c in reversed(s)):
            score = 0
            if number_one_ahead == 0:
                if 1 <= n <= 2:
                    score = score_two_ahead if score_two_ahead else 1
                else:
                    return 0
            elif n == 0:
                None
            elif number_one_ahead == None:
                score = 1
            elif number_two_ahead == 0:
                score = score_one_ahead
            elif n * 10 + number_one_ahead <= 26:
                score = score_one_ahead + (score_two_ahead if score_two_ahead else 1)
            else:
                score = score_one_ahead
            number_two_ahead, number_one_ahead = number_one_ahead, n
            score_two_ahead, score_one_ahead = score_one_ahead, score
        return score
