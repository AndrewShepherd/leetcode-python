from collections import defaultdict

def gcd(n1, n2):
    if n1 > n2:
        n1,n2 = n2,n1
    if n2%n1 == 0:
        return n1
    else:
        return gcd(n1, n2%n1)
    
def lcm(n1, n2):
    return (n1 * n2) // gcd(n1, n2)


def generateCalculationFunction(coins, max_amount):
    def generate_divisors(inputs):
        result = [(n, 1) for n in inputs]
        for i in range(1, len(inputs)):
            n1 = inputs[i]
            s = set()
            for j in range(i):
                n2 = inputs[j]
                l = lcm(n1, n2)
                if l <= max_amount:
                    s.add(l)
            to_subtract = generate_divisors(list(s))
            result.extend([(n, 0-q) for n,q in to_subtract])
        return result
    
    divisors = generate_divisors(coins)
    # Normalize them
    d = defaultdict(int)
    for n,q in divisors:
        d[n] += q
    divisors = [(n,q) for n,q in d.items() if (q != 0)]



    return lambda amount: sum([amount//d * q for d,q in divisors])

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        r = k*min(coins)
        calculate = generateCalculationFunction(coins, r)
        l = 1
        while(r - l > 1):
            m = (l+r)//2
            this_result = calculate(m)
            if this_result >=k:
                r = m
            else:
                l = m
        return r