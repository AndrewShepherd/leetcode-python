def isPalindrome(s, i, j):
    if j > len(s):
        return False
    lastIndex = j-1

    while(i < len(s) and 0 <= lastIndex < len(s) and i < lastIndex):
        if s[i] != s[lastIndex]:
            return False
        i += 1
        lastIndex -= 1
    return True

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        best_result_up_to = [0] * len(s)
        for i in range(len(s)):
            this_score = (0 if i == 0 else best_result_up_to[i-1]) + 1
            for j in range(i+k, len(s)+1):
                if best_result_up_to[j-1] >= this_score:
                    break
                if isPalindrome(s, i, j):
                    for l in range(j-1, len(best_result_up_to)):
                        best_result_up_to[l] = max(
                            best_result_up_to[l],
                            this_score
                        )
                    break
        return best_result_up_to[-1]