from collections import defaultdict

def isPalindrome(compressedWord, start, endExclusive):
    l = start
    r = endExclusive - 1
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
    return tuple(result)

def getPrefixBeforePalindromes(compressedWord):
    for index, pivotWord in enumerate(compressedWord):
        char, count = pivotWord
        lastChar, lastCount = compressedWord[-1]
        if char != lastChar or count < lastCount:
            continue
        if index == len(compressedWord) - 1:
            yield compressedWord[:index]
            for c in range(1, count):
                yield compressedWord[:-1] + ((char, c),)
        else:
            if not isPalindrome(compressedWord, index+1, len(compressedWord)-1):
                continue
            if count == lastCount:
                yield compressedWord[:index]
            else:
                yield compressedWord[:index] + ((char, count-lastCount),)

def getSufixAfterPalindromes(compressedWord):
    for index, pivotWord in reversed(list(enumerate(compressedWord))):
        char, count = pivotWord
        lastChar, lastCount = compressedWord[0]
        if char != lastChar or count < lastCount:
            continue
        if index == 0:
            yield compressedWord[1:]
            for c in range(1, count):
                yield ((char, c),) + compressedWord[1:]
        else:
            if isPalindrome(compressedWord, 1, index):
                if count == lastCount:
                    yield compressedWord[index+1:]
                else:
                    yield ((char, count-lastCount),) + compressedWord[index+1:]

class Solution:
    def palindromePairs(self, words):
        wordLookup = {makeCompressedWord(word): index for index, word in enumerate(words)}
        result = set()
        for word, index in wordLookup.items():
            if isPalindrome(word, 0, len(word)):
                empty = makeCompressedWord("")
                if empty in wordLookup:
                    result.add((index, wordLookup[empty]))
                    result.add((wordLookup[empty], index))

            requiredMatch = word[::-1]
            if requiredMatch in wordLookup:
                result.add((index, wordLookup[requiredMatch]))

            for prefix in getPrefixBeforePalindromes(word):
                requiredMatch = prefix[::-1]
                if requiredMatch in wordLookup:
                    result.add((index, wordLookup[requiredMatch]))

            for suffix in getSufixAfterPalindromes(word):
                requiredMatch = suffix[::-1]
                if requiredMatch in wordLookup:
                    result.add((wordLookup[requiredMatch], index))

        return [[l,r] for l,r in result if l != r]