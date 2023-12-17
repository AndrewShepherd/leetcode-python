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

def decrement_list_to_next_palindrome(n):
    if is_zero(n):
        return None
    if len(n) == 0:
        return n
    if is_palindrome(n):
        n = decrement_list(n)

    if n[-1] > n[0]:
        if is_palindrome(n[1:-1]):
            return [*n[:-1], n[0]]
        else:
            middle = n[1:-1]
            middle_decremented = decrement_list_to_next_palindrome(middle)
            if middle_decremented != None:
                return [n[0], *middle_decremented, n[0]]
            else:
                raise 'Unhandled'
    if n[0] > 0:
        return [n[0]-1, *n[1:-1], n[0]-1]
    raise 'Unhandled'

def increment_list_to_next_palindrome(n):
    if len(n) == 0:
        return n
    if is_all_nines(n):
        return None
    if is_palindrome(n):
        n = increment_list(n)
    if n[-1] < n[0]:
        if is_palindrome(n[1:-1]):
            return [*n[:-1], n[0]]
        else:
            middle = n[1:-1]
            middle_incremented = increment_list_to_next_palindrome(middle)
            if(middle_incremented):
                return [n[0], *middle_incremented, n[0]]
    else:
        middle = n[1:-1]
        middle_incremented = increment_list_to_next_palindrome(middle)
        if middle_incremented != None:
            return [n[0], *middle_incremented, n[0]]
    raise 'Unhandled'

def find_next_higher_palindromic_number(n):
    if isinstance(n, int):
        n = to_int_array(n)
    if len(n) == 1 and n[0] < 9:
        return n[0] + 1
    elif is_palindrome(n):
        return find_next_higher_palindromic_number(to_int(n) + 1)
    elif n[0] > n[-1]:
        if (is_palindrome(n[1:-1])):
            return to_int([*n[:-1], n[0]])
        else:
            middle_incremented = increment_list_to_next_palindrome(n[1:-1])
            if (middle_incremented):
                return to_int([n[0], *middle_incremented, n[0]])
            raise "This is a situation not dealt with"
    else:
        middle = n[1:-1]
        if len(middle) == 0:
            if n[0] == 9:
                return 101
            else:
                return to_int([n[0]+1, n[0] + 1])
        elif is_zero(middle):
            return to_int([n[0], *([1] * len(middle)), n[0]])
        else:
            middle_higher = to_int_array(find_next_higher_palindromic_number(middle))
            if len(middle_higher) == len(middle):
                return to_int([n[0], *middle_higher, n[0]])
            else:
                return to_int([n[0]+1, *([0]*len(middle)), n[0]+1])

def find_lower_palindromic_number(n):
    if isinstance(n, int):
        n = to_int_array(n)
    if len(n) == 1:
        return n[0] - 1
    if is_palindrome(n):
        return find_lower_palindromic_number(to_int(n) - 1)
    if n[-1] > n[0]:
        if (is_palindrome(n[1:-1])):
            return to_int([*n[:-1], n[0]])
        else:
            middle = n[1:-1]
            middle_lower = decrement_list_to_next_palindrome(middle)
            if len(middle_lower) == len(middle):
                return to_int([n[0], *middle_lower, n[0]])
            else:
                raise "Unhandled situation"
    else:
        middle = n[1:-1]
        if is_zero(middle):
            return to_int([n[0]-1, *([9]*len(middle)), n[0]-1])
        else:
            middle_lower = decrement_list_to_next_palindrome(middle)
            if is_zero(middle_lower):
                middle_lower = [0] * len(middle)
            if len(middle_lower) == len(middle):
                return to_int([n[0], *middle_lower, n[0]])

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

