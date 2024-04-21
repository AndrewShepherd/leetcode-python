
def rotated_key_fits(circle, key):
    for k in key:
        if k not in circle:
            return False
    return True

def rotate_key(circle, key):
    circle = sorted(list(circle))
    key = sorted(list(key))
    for n in circle:
        rotation = key[0] - n
        rotated_key = [(k - rotation) % 16 for k in key]
        if rotated_key_fits(circle, rotated_key):
            yield rotated_key

def apply_key_to_circle(circle, rotation):
    return tuple([c for c in circle if c not in rotation])

def match_key_to_circle(circle, key):
    if type(circle) == int:
        return
    if type(key) == int:
        return
    if len(key) <= len(circle):
        for rotation in rotate_key(circle, key):
            yield apply_key_to_circle(circle, rotation)   
    
def solve_recursively(circles, keys):
    if len(circles) == 0:
        return []
    for i,(key_index, key) in enumerate(keys):
        for circle in match_key_to_circle(circles[0][1], key):
            result = [(circles[0][0], key_index)]
            remaining_keys = keys[:i] + keys[i+1:]
            if circle:
                sub_result = solve_recursively([(circles[0][0],circle)] + circles[1:], remaining_keys)
            else:
                sub_result = solve_recursively(circles[1:], remaining_keys)
            if sub_result != None:
                return result + sub_result
    None

class Solution:

    def solve(self):
        all_circles = [
                    (1,8,9,12,14),
                    (0,2,3,4,6,11),
                    (10,11,15),
                    (1,5,10)
                ]

        all_keys = [
            (4,6,10,12),
            (0, 1),
            (4,10),
            (0,8),
            (0,5,7),
            (0,),
            (11,15),
            (12,1),
            (2,3,7),
            (0,),
            (0,),
            (0,4,11)
        ]


        all_circles = list(enumerate(all_circles))
        all_keys = list(enumerate(all_keys))

        result = solve_recursively(all_circles, all_keys)
        print(f'{result}')

        return 0