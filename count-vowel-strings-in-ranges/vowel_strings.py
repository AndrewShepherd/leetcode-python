vowels = 'aeiou'

class Solution:
    def vowelStrings(self, words, queries):
        cumulative_vowel_counts = [0] * len(words)
        cumulative_value = 0
        for i,w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                cumulative_value += 1
            cumulative_vowel_counts[i] = cumulative_value
        results = []
        for l,r in queries:
            total = cumulative_vowel_counts[r]
            if l > 0:
                total -= cumulative_vowel_counts[l-1]
            results.append(total)
        return results
