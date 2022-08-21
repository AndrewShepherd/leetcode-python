import math

def countNumbersWithFixedDigitCount(digitCount: int, noGreaterThan: int, digitsUsedAlready) :
    if digitCount == 0:
        return 0
    if digitCount == 1:
        return sum([1 for i in range(0, noGreaterThan+1) if not i in digitsUsedAlready])

    tens = 10**(digitCount-1)

    firstDigit = noGreaterThan//tens
    remaining = noGreaterThan % tens
    total = 0
    if not firstDigit in digitsUsedAlready:
        digitsUsedAlready.add(firstDigit)
        total += countNumbersWithFixedDigitCount(digitCount-1, remaining, digitsUsedAlready)
        digitsUsedAlready.remove(firstDigit)

    countOfDigitsAvailable = 10-len(digitsUsedAlready) - 1
    total += math.perm(countOfDigitsAvailable, digitCount-1) * len([1 for n in range(firstDigit) if n not in digitsUsedAlready])
    return total
    

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        if(n < 11):
            return n 

        digitCount = int(math.log10(n)) + 1
        tens = 10**(digitCount-1)
        firstDigit = n // tens
        remainingNumber = n % tens
        total = countNumbersWithFixedDigitCount(digitCount-1, remainingNumber, set([firstDigit])) 
        for d in range(1, firstDigit):
            total += math.perm(9, digitCount-1) 
    
        for d in range(1, digitCount):
            amountWithDigits = 9 * math.perm(9, d-1)
            total += amountWithDigits
        return int(total)
