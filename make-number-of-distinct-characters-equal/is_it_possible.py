from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        len1 = len(counter1)
        len2 = len(counter2)
        
        word1_chars = list(counter1.keys())
        word2_chars = list(counter2.keys())

        for c1 in word1_chars:
            for c2 in word2_chars:
                if c1 == c2:
                    if len1 == len2:
                        return True
                    else:
                        continue
                new_len1 = len1
                new_len2 = len2
                
                # Remove c1 from word1
                if counter1[c1] == 1:
                    new_len1 -= 1
                if counter2[c2] == 1:
                    new_len2 -= 1
                if not c2 in counter1:
                    new_len1 += 1
                if not c1 in counter2:
                    new_len2 += 1
                if new_len1 == new_len2:
                    return True
        return False
