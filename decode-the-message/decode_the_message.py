class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s = set()
        targetOrd = ord('a')
        lookup = [None] * 26
        for c in key:
            if c != ' ' and c not in s:
                lookupIndex = ord(c) - ord('a') 
                lookup[lookupIndex] = targetOrd
                targetOrd += 1
                s.add(c)

        def substitute(c):
            if (c == ' '):
                return c
            o = lookup[ord(c) - ord('a')]
            return chr(o)
        
        return ''.join([substitute(c) for c in message])