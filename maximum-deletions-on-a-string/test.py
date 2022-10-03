import unittest

from maximum_deletions_on_a_string import Solution, possibleLengths

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.deleteString(s)
        self.assertEqual(result, expectedResult)

    def test_3(self):
        self.run_test(
            "abcabcdabc",
            2
        )

    def test_5(self):
        l = list(possibleLengths("aaabaab", 1))
        self.assertEqual(2, len(l))
        self.run_test(
            "aaabaab",
            4
        )

    def test_2(self):
        self.run_test(
            "aaaaa",
            5
        )

    def test_0(self):
        self.run_test(
            "a"*4000,
            4000
        )


try:
    unittest.main()
except SystemExit:
    None





