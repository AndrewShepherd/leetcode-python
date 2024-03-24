from collections import defaultdict

class left_brackets:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return '(' * self.count
    
    def __repr__(self):
        return '(' * self.count

class right_brackets:
    def __init__(self, count):
        self.count = count
    
    def __str__(self):
        return ')' * self.count
    
    def __repr__(self):
        return ')' * self.count

class text:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value

def parse(s: str):
    last = None
    for c in s:
        if c == '(':
            if type(last) == left_brackets:
                last = left_brackets(last.count + 1)
            else:
                if last != None:
                    yield last
                last = left_brackets(1)
        elif c == ')':
            if type(last) == right_brackets:
                last = right_brackets(last.count + 1)
            else:
                if last != None:
                    yield last
                last = right_brackets(1)
        else:
            if type(last) == text:
                last = text(last.value + c)
            else:
                if last != None:
                    yield last
                last = text(c)
    if last != None:
        yield last

def convert_back(token_list):
    return ''.join(f"{t}" for t in token_list)

def is_valid(token_list):
    c = 0
    for i,t in enumerate(token_list):
        if type(t) == left_brackets:
            c += t.count
        elif type(t) == right_brackets:
            c -= t.count
        if c < 0:
            return i
    return None if c == 0 else len(token_list) 

def find_valid_results(tokens, max_allowable_removals, start_index):
    validity_result = is_valid(tokens)
    if validity_result == None:
        return 0, [tokens]
    elif validity_result < start_index:
        return None, None
    if start_index == len(tokens):
        return None, None
    if max_allowable_removals <= 0:
        return None, None
    this_token = tokens[start_index]
    if type(this_token) == text:
        return find_valid_results(tokens, max_allowable_removals, start_index + 1)
    removals = 0
    results = defaultdict(list)
    while(True):
        new_token_set = tokens[:start_index] + [this_token] + tokens[start_index+1:]
        sub_removals, sub_results = find_valid_results(new_token_set, max_allowable_removals - removals, start_index+1)
        if sub_removals != None:
            total_removals = removals + sub_removals
            if(total_removals <= max_allowable_removals):
                results[total_removals].extend(sub_results)
                max_allowable_removals = total_removals
        if this_token.count == 0:
            break               
        this_token = left_brackets(this_token.count - 1) if type(this_token) == left_brackets else right_brackets(this_token.count - 1)
        removals += 1
    if not results:
        return None, None
    min_removals = min(results.keys())
    return min_removals, results[min_removals]
    

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        tokens = list(parse(s))
        removals, results = find_valid_results(tokens, 20, 0)

        return [convert_back(token_list) for token_list in results]