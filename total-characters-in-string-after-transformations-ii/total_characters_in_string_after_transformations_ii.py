MOD = 10**9 + 7

def generate_initial_matrix(nums):
    result = [[0] * 26 for _ in range(26)]
    for i,n in enumerate(nums):
        for j in range(n):
            result[(i+j+1)%26][i] += 1
    return result

def generate_identity_matrix():
    result = [[0] * 26 for _ in range(26)]
    for i in range(26):
        result[i][i] = 1
    return result

def matrix_multiply(m1, m2):
    result_rows = len(m1[0])
    result_cols = len(m2[0])

    result = [[0] * result_cols for _ in range(result_rows)]
    for row_index, row in enumerate(result):
        for col_index in range(result_cols):
            row[col_index] = sum(m1[row_index][i] * m2[i][col_index] for i in range(len(m2)))
    return result

def matrix_times_vector(m, v):
    result = [0] * 26
    for i in range(26):
        result[i] = sum((m[i][j] * v[j] for j in range(26))) % MOD
    return result

def to_vector(s):
    result = [0] * 26
    for c in s:
        result[ord(c) - ord('a')] += 1
    return result


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        initial_matrix = generate_initial_matrix(nums)
        v = to_vector(s)

        as_binary = []
        while(t):
            as_binary.append(t%2)
            t //= 2
        
        m = generate_identity_matrix()
        while(as_binary):
            m = matrix_multiply(m, m)
            if (as_binary.pop()):
                m = matrix_multiply(m, initial_matrix)

        v = matrix_times_vector(m, v)

        return sum(v) % MOD

