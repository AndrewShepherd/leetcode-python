class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        stars = 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if c == '*':
                stars += 1
            elif stars:
                stars -= 1
            else:
                l.append(c)
        return ''.join(reversed(l))