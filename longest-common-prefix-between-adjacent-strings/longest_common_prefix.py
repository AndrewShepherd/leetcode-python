def longestCommonPrefixBetweenTwoWords(word1: str, word2: str) -> int:
    # Find the longest common prefix between two words
    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            return i
    return min(len(word1), len(word2))


class Solution:
    def longestCommonPrefix(self, words: list[str]) -> list[int]:
        # Create a list of (longest_common_prefix, index)
        result = []
        for i in range(len(words) - 1):
            longest_common_prefix = longestCommonPrefixBetweenTwoWords(words[i], words[i + 1])
            result.append((longest_common_prefix, i))
        result.sort(key=lambda x: x[0], reverse=True)

        answer = []
        for i in range(len(words)):
            longest_common_prefix_without_i = 0
            for (longest_common_prefix, index) in result:
                if (index != i) and (index + 1 != i):
                    longest_common_prefix_without_i = longest_common_prefix
                    break
            new_prefix_length = 0
            if 1 <= i < len(words) - 1:
                new_prefix_length = longestCommonPrefixBetweenTwoWords(words[i - 1], words[i + 1])
            answer.append(max(longest_common_prefix_without_i, new_prefix_length))

        return answer

