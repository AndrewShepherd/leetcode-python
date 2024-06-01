import unittest

from min_length_of_anagram_concatenation import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        s = "abba"
        # (1,1,1,2,2,3)
        # We want index 2
        result = sol.minAnagramLength(s)
        self.assertEqual(2, result)

    def test_2(self):
        sol = Solution()
        s = "cdef"
        # (1,1,1,2,2,3)
        # We want index 2
        result = sol.minAnagramLength(s)
        self.assertEqual(4, result)


try:
    unittest.main()
except SystemExit:
    None





















