import math

def is_zero(n):
    if isinstance(n, list):
        for v in n:
            if v != 0:
                return False  
        return True     
    return to_int(n) == 0

def is_all_nines(n):
    for v in n:
        if v != 9:
            return False
    return True

def to_int_array(n):
    if n == None:
        raise ('n == None')
    s = str(n)
    return [int(c) for c in str(n)]

def to_int(n):
    if isinstance(n, int):
        return n
    elif isinstance(n, list):
        if not n:
            return 0
        return int(''.join([str(c) for c in n]))
    

def is_palindrome(n):
    if isinstance(n, int):
        n = to_int_array(n)
    return n == n[::-1]

def increment_list(n):
    result = n[:]
    for i in range(len(n)-1, -1, -1):
        if result[i] != 9:
            result[i] += 1
            break
        else:
            result[i] = 0
    return result


def decrement_list(n):
    result = n[:]
    for i in range(len(n)-1, -1, -1):
        if result[i] != 0:
            result[i] -= 1
            break
        else:
            result[i] = 9
    return result


def find_next_higher_palindromic_number(n):
    if n < 9:
        return n + 1
    n_list = to_int_array(n)
    if len(n_list) % 2 == 0:
        left = n_list[:len(n_list)//2]
        construct = lambda l: l + l[::-1]
    else:
        left = n_list[:len(n_list)//2+1]
        construct = lambda l: l + l[-2::-1]
    while(True):
        result = to_int(construct(left))
        if result > n:
            return result
        elif left == [9] * len(left):
            return to_int([1] + [0]*len(n_list)) + 1
        left = increment_list(left)
 
def find_lower_palindromic_number(n : int):
    if n <= 10:
        return n - 1
    n_list = to_int_array(n)
    if len(n_list) == 1:
        return n_list[0] - 1
    
    if (len(n_list) % 2 == 0):
        left = n_list[:len(n_list)//2]
        while(True):
            result = left + left[::-1]
            result = to_int(result)
            if result < n:
                return result
            if left == [1] + [0]*(len(left)-1):
                return to_int([9] * (len(n_list)-1))
            left = decrement_list(left)
    else:
        left = n_list[:len(n_list)//2+1]
        while(True):
            result = left + left[-2::-1]
            result = to_int(result)
            if result < n:
                return result
            if left == [1] + [0]*(len(left)-1):
                return to_int([9] * (len(n_list)-1))
            left = decrement_list(left)

def find_best(starting_value, transform, calculate_score):
    best_score = calculate_score(starting_value)
    while True:
        starting_value = transform(starting_value)
        this_score = calculate_score(starting_value)
        if this_score < best_score:
            best_score = this_score
        else:
            break
    return best_score

class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        avg = sum(nums)/len(nums)
        calculate_score = lambda p : sum([abs(n-p) for n in nums])
        m = int(math.floor(avg))
        p = find_lower_palindromic_number(m)
        score_going_up = find_best(p, find_next_higher_palindromic_number, calculate_score)
        score_going_down = find_best(find_next_higher_palindromic_number(m), find_lower_palindromic_number, calculate_score)
        return min(score_going_up, score_going_down)

