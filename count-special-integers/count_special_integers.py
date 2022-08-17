from functools import cache
from unicodedata import digit
import math

@cache
def combos(len, digits_to_choose_from):
    p = 1
    for f in range(digits_to_choose_from, digits_to_choose_from-len, -1):
        p *= f
    return p

@cache
def specialNumbersWithDigitCount(digit_count):
    if digit_count == 0:
        return 0
    elif digit_count == 1:
        return 9
    else:
        return 9 * combos(digit_count-1, 9)

def getDigits(n : int):
    result = set()
    while (n > 0):
        result.add(n%10)
        n //= 10
    return result


def countdownSolve(n: int) -> int:
    if n < 10:
        return n
    lastDigit = n % 10
    otherDigits = getDigits(n//10)
    
    thisDigitCountDown = sum([0 if i in otherDigits else 1 for i in range(lastDigit+1)])
    others = countdownSolve(n//10-1)
    return thisDigitCountDown + others * (10-len(otherDigits))

def countNumbersWithFixedDigitCount(digitCount: int, noGreaterThan: int, digitsUsedAlready) :
    if digitCount == 0:
        return 0
    if digitCount == 1:
        return sum([1 for i in range(0, noGreaterThan+1) if not i in digitsUsedAlready])
    noGreaterThanStr = str(noGreaterThan)
    noGreaterThanStr = '0'*(digitCount-len(noGreaterThanStr)) + noGreaterThanStr
    firstDigit = int(noGreaterThanStr[0])
    total = 0
    if not firstDigit in digitsUsedAlready:
        digitsUsedAlready.add(firstDigit)
        total += countNumbersWithFixedDigitCount(digitCount-1, int(noGreaterThanStr[1:]), digitsUsedAlready)
        digitsUsedAlready.remove(firstDigit)
    nines = int(10**(digitCount-1))-1
    for n in range(firstDigit):
        if n in digitsUsedAlready:
            continue
        digitsUsedAlready.add(n)
        #total +=   countNumbersWithFixedDigitCount(digitCount-1, nines, digitsUsedAlready)
        countOfDigitsAvailable = 10-len(digitsUsedAlready)
        total += math.factorial(countOfDigitsAvailable)/math.factorial(countOfDigitsAvailable-digitCount+1)
        digitsUsedAlready.remove(n)
    return total
    

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        if(n < 11):
            return n 
        nStr = str(n)
        digitCount = len(nStr)
        firstDigit = int(nStr[0])
        
        total = countNumbersWithFixedDigitCount(digitCount-1, int(nStr[1:]), set([firstDigit])) # countNumbersWithFixedDigitCount(digitCount, n, set())
        nines = int(10**(digitCount-1))-1
        for d in range(1, firstDigit):
            total += countNumbersWithFixedDigitCount(digitCount-1, nines, set([d]))
    
        for d in range(1, digitCount):
            amountWithDigits = 9 * math.factorial(9)/math.factorial(9-d+1)
            total += amountWithDigits # countNumbersWithFixedDigitCount(d, nines, set())
        return int(total)
