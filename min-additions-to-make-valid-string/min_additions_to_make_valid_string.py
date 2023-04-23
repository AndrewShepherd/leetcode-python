


class Solution:
    def addMinimum(self, word: str) -> int:
        if len(word) == 0:
            return 0
        expected = 'a'
        count = 0
        i = 0
        while (i < len(word)):
            c = word[i]
            if expected == 'a':
                if c != 'a':
                    count += 1
                else:
                    i += 1
                expected = 'b'
            elif expected == 'b':
                if c != 'b':
                    count += 1
                else:
                    i += 1
                expected = 'c'
            elif expected == 'c':
                if c != 'c':
                    count += 1
                else:
                    i += 1
                expected = 'a'
        if c == 'a':
            count += 2
        elif c == 'b':
            count += 1
        return count
