def get_lps(s: str) -> list[int]:
    result = [0] * len(s)
    l = 0
    i = 1
    while i < len(s):
        if s[l] == s[i]:
            l += 1
            result[i] = l
            i += 1
        elif l > 0:
            l = result[l-1]
        else:
            result[i] = 0
            i += 1
    return result

def get_backward_lengths_kmp(target, w):
    backward_lengths = [0] * len(target)
    lps = get_lps(w)
    w_index = -1
    i = 0
    while i < len(target):
        if w_index == len(w) - 1:
            w_index = lps[w_index] - 1
        elif target[i] == w[w_index+1]:
            w_index += 1
            backward_lengths[i] = w_index + 1
            i += 1
        elif (w_index != -1):
            w_index = lps[w_index] - 1
        else:
            i += 1
    return backward_lengths


class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        backward_lengths = [0] * len(target)
        for w in words:
            bw_2 = get_backward_lengths_kmp(target, w)
            backward_lengths = [max(l, r) for l,r in zip(backward_lengths, bw_2)]
        count = 0
        index = len(backward_lengths) - 1
        while(index >= 0):
            if backward_lengths[index] == 0:
                return -1
            index -= backward_lengths[index]
            count += 1
        return count
