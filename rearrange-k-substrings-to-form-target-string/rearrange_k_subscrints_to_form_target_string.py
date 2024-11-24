def to_split_string(s, k):
    each_size = len(s)//k
    start_ranges = range(0, len(s), each_size)
    return [s[i:i+each_size] for i in start_ranges]

def to_buckets(l):
    return [sorted(s) for s in l]

def transform(s, k):
    return sorted(to_buckets(to_split_string(s, k)))


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        bs = transform(s, k)
        bt = transform(t, k)
        return bs == bt
        
