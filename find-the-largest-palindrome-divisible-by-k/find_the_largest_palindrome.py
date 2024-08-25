def gcd(l: int, r: int) -> int:
    if l == r:
        return l
    s,b = (l,r) if l <= r else (r,l)
    if s == 0:
        return b
    m = b % s
    if m == 0:
        return s
    elif m == 1:
        return 1
    else:
        return gcd(s, m)
    


# Return the largest palindromic number x so that
# (a*x) % m == remainder
def solve(num_digits: int, a: int, m: int, remainder:int) -> str:
    if (a%m == 0):
        if remainder == 0:
            return '9' * num_digits
        else:
            return None        
    a %= m
    remainder %= m
    gcd_a_m = gcd(a, m)
    if gcd_a_m > 1:
        gcd2 = gcd(remainder, gcd_a_m)
        if gcd2 == 1:
            return None
        else:
            a,m,remainder = a//gcd2,m//gcd2,remainder//gcd2

    if num_digits == 0:
        return '' if remainder == 0 else None
    if num_digits == 1:
        result = None
        for k in range(10):
            test = a*k%m
            if test == remainder:
                result = k
        return str(result) if result != None else None
    if num_digits == 2:
        result = None
        for k in range(10):
            test = 11*a*k%m
            if test == remainder:
                result = k
        return str(result)*2 if result != None else None

    for d in range(9, -1, -1):
        # Result must equal m*n + lc
        this_value = a * (pow(10, num_digits-1, m) * d + d) % m
        sub_string_target = (remainder - this_value) % m
        sub_string = solve(num_digits-2, (10 * a)%m, m, sub_string_target)
        if sub_string != None:
            return str(d) + sub_string + str(d)
    return None 


class Solution:
    def largestPalindrome(self, num_digits: int, divisor: int) -> str:
        return solve(num_digits, 1, divisor, 0)
