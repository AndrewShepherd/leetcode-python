from collections import defaultdict

def isPalindrome(compressedWord):
    l = 0
    r = len(compressedWord) - 1
    while l < r:
        if compressedWord[l] != compressedWord[r]:
            return False
        l += 1
        r -= 1
    return True

def makeCompressedWord(word):
    result = []
    for c in word:
        if not result or result[-1][0] != c:
            result.append((c, 1))
        else:
            result[-1] = (c, result[-1][1]+1)
    return result

class Solution:
    def palindromePairs(self, words):
        wordLookup = {word: index for index, word in enumerate(words)}
        result = set()
        for index, word in enumerate(words):
            requiredMatch = word[::-1]
            if requiredMatch in wordLookup:
                result.add((index, wordLookup[requiredMatch]))

            compressedWord = makeCompressedWord(word)
            for i in range(len(word)):
                if isPalindrome(compressedWord):
                    requiredMatch = word[:i][::-1]
                    if requiredMatch in wordLookup:
                        result.add((index, wordLookup[requiredMatch]))
                
                compressedWord[0] = (compressedWord[0][0], compressedWord[0][1]-1)
                if not compressedWord[0][1]:
                    compressedWord.pop(0)
            
            compressedWord = makeCompressedWord(word)
            for i in range(len(word),0,-1):
                if isPalindrome(compressedWord):
                    requiredMatch = word[:i-1:-1]
                    if requiredMatch in wordLookup:
                        result.add((wordLookup[requiredMatch], index))
                compressedWord[-1] = (compressedWord[-1][0], compressedWord[-1][1]-1)
                if not compressedWord[-1][1]:
                    compressedWord.pop()
            
        return [[l,r] for l,r in result if l != r]