def distinct_ideas(bucket1, bucket2, ideas_lookup):
    if bucket1 == None or bucket2 == None:
        return 0
    b1Allowed = 0
    letter1 = bucket1[0][0]
    letter2 = bucket2[0][0]

    for w in bucket1:
        newWord = letter2 + w[1:]
        if newWord not in ideas_lookup:
            b1Allowed += 1
    b2Allowed = 0
    for w in bucket2:
        newWord = letter1 + w[1:]
        if newWord not in ideas_lookup:
            b2Allowed += 1
    return b1Allowed * b2Allowed * 2

class Solution:
    def distinctNames(self, ideas) -> int:
        letter_buckets = [None] * 26
        for idea in ideas:
            letter_bucket_index = ord(idea[0]) - ord('a')
            if letter_buckets[letter_bucket_index] == None:
                letter_buckets[letter_bucket_index] = []
            letter_buckets[letter_bucket_index].append(idea)
        ideas_lookup = set(ideas)

        count = 0
        for letter_index in range(25):
            bucket1 = letter_buckets[letter_index]
            for other_bucket_index in range(letter_index+1, 26):
                bucket2 = letter_buckets[other_bucket_index]
                count += distinct_ideas(bucket1, bucket2, ideas_lookup)
        return count
        