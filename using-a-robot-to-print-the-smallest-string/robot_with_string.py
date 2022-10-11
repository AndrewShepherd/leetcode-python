class Solution:
    def robotWithString(self, s: str) -> str:
        result = []
        t = []
        while s:
            indexes = [0]
            minChar = s[0]
            for i in range(1, len(s)):
                thisChar = s[i]
                if thisChar < minChar:
                    minChar = thisChar
                    indexes = [i]
                elif thisChar == minChar:
                    indexes.append(i)
            while t and t[-1] <= minChar:
                result.append(t.pop())
            prev = 0
            for i in indexes:
                t.extend(s[prev:i])
                result.append(minChar)
                prev = i + 1
            s = s[indexes[-1]+1:]
        result.extend(t[::-1])
        return "".join(result)

