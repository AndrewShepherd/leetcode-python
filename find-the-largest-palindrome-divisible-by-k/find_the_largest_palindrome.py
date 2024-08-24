def padstr(n, l):
    s = str(n)
    if len(s) < l:
        s = ('0' * (l - len(s))) + s
    return s

def get_palindromes(l):
    if (l == 1):
        for n in range(9, -1, -1):
            yield n
    elif l == 2:
        for n in range(9, -1, -1):
            yield n*10 + n
    else:
        for n in range(9, -1, -1):
            for p in get_palindromes(l - 2):
                yield n * 10**(l-1) + p * 10 + n

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k in (1, 3, 9):
            return '9' * n
        if k == 5:
            return '5' if n == 1 else '5' + ('9' * (n -2)) + '5'
        if k == 2:
            return '8' if n == 1 else '8' + ('9' * (n -2)) + '8'
        if k == 4:
            return '8' * n if n <= 4 else '88' + ('9' * (n-4)) + '88' 
        if k == 8:
            return '8' * n if n <= 6 else '888' + ('9' * (n-6)) + '888' 
        if n == 1:
            for attempt in range(9, 0, -1):
                if attempt % k == 0:
                    return str(attempt)
        if k % 2 == 0:
            attempt = '8' + ('9' * (n -2)) + '8'
        else:
            attempt = '9' * n
        def calculate_modulus(attempt:str) -> int:
            modulus = 0
            for i,c in enumerate(attempt):
                modulus = (modulus + (pow(10, len(attempt)-i-1, k) * int(c) )) % k
            return modulus
        
        if len(attempt) % 2 == 0:
            middle = (len(attempt)//2-1, 2)
        else:
            middle = (len(attempt)//2, 1)
        while(calculate_modulus(attempt) != 0):
            for p in get_palindromes(middle[1]):
                attempt = attempt[:middle[0]] + padstr(p, middle[1]) + attempt[(middle[0] + middle[1]):]
                if calculate_modulus(attempt) == 0:
                    return attempt
            middle = (middle[0]-1, middle[1] + 2)
        return attempt 