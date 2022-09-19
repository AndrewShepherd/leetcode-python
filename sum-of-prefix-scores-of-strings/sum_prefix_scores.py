from functools import cache


TOO_SMALL = -1
EQUAL = 0
TOO_BIG = 1

def compareCharAtIndex(words, c, i):
    def compare(otherIndex):
        word = words[otherIndex]
        if i < 0:
            raise "out of range!"
        if i >= len(word):
            return TOO_SMALL
        if word[i] < c:
            return TOO_SMALL
        elif word[i] > c:
            return TOO_BIG
        else:
            return EQUAL
    return compare

def getFirstInstance(compare, rangeStart, rangeEndExclusive):
    tryThis = (rangeStart + rangeEndExclusive)//2
    comparisonResult = compare(tryThis)
    if comparisonResult == EQUAL:
        if tryThis == rangeStart:
            return tryThis
        if compare(tryThis - 1) == TOO_SMALL:
            return tryThis
        else:
            return getFirstInstance(compare, rangeStart, tryThis)
    if comparisonResult == TOO_BIG:
        return getFirstInstance(compare, rangeStart, tryThis)
    else:
        return getFirstInstance(compare, tryThis+1, rangeStart)


def getFirstInstancePast(compare, rangeStart, rangeEndExclusive):
    tryThis = (rangeStart + rangeEndExclusive)//2
    comparisonResult = compare(tryThis)
    if comparisonResult == EQUAL:
        if tryThis+1 == rangeEndExclusive:
            return tryThis+1
        elif compare(tryThis+1) == TOO_BIG:
            return tryThis+1
        return getFirstInstancePast(compare, tryThis+1, rangeEndExclusive)
    if comparisonResult == TOO_BIG:
        if compare(tryThis-1) == EQUAL:
            return tryThis
        else:
            return getFirstInstancePast(compare, rangeStart, tryThis)
    return getFirstInstancePast(compare, tryThis+1, rangeEndExclusive)

def getRange(compare, rangeStart, rangeEndExclusive):
    rangeStart = getFirstInstance(compare, rangeStart, rangeEndExclusive)
    rangeEndExclusive = getFirstInstancePast(compare, rangeStart, rangeEndExclusive)
    return rangeStart, rangeEndExclusive

class Solution:
    def sumPrefixScores(self, words):
        wordsSorted = sorted(words)
        result = [0] * len(words)
        for index, w in enumerate(words):
            rangeStart = 0
            rangeEndExclusive = len(words)
            score = 0
            for i,c in enumerate(w):
                rangeStart, rangeEndExclusive = getRange(
                    compareCharAtIndex(wordsSorted, c, i),
                    rangeStart,
                    rangeEndExclusive
                )
                score += rangeEndExclusive - rangeStart
            result[index] = score

        return result
