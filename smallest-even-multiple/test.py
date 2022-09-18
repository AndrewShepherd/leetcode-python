import unittest


from smallest_even_multiple import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.smallestEvenMultiple(input)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            5,
            10
        )

    def test_2(self):
        self.run_test(
            6,
            6,
        )

    
    def test_0(self):
        self.run_test(
           "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
            4,
        )
try:
    unittest.main()
except SystemExit:
    None
