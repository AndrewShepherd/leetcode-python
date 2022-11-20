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
        for i in range(k//2-1, len(s)-k//2):
            # Find palindromes where i is the center
            left = i
            right = i
            # odd length palindromes
            while True:
                if left < 0:
                    break
                if right >= len(s):
                    break
                if s[left] != s[right]:
                    break
                this_score = (0 if left == 0 else best_result_up_to[left-1]) + 1
                if best_result_up_to[right] >= this_score:
                    break
                if right - left + 1 >= k:
                    for rIndex in range(right, len(best_result_up_to)):
                        best_result_up_to[rIndex] = max(best_result_up_to[rIndex], this_score)
                    break
                left -= 1
                right += 1
            left = i
            right = i+1
            while True:
                if left < 0:
                    break
                if right >= len(s):
                    break
                if s[left] != s[right]:
                    break
                this_score = (0 if left == 0 else best_result_up_to[left-1]) + 1
                if best_result_up_to[right] >= this_score:
                    break
                if right - left + 1 >= k:
                    for rIndex in range(right, len(best_result_up_to)):
                        best_result_up_to[rIndex] = max(best_result_up_to[rIndex], this_score)
                    break
                left -= 1
                right += 1

        return best_result_up_to[-1]