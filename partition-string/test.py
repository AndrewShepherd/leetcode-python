import unittest


from partition_string import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.partitionString(input)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            "abacaba",
            4
        )

    def test_2(self):
        self.run_test(
           "ssssss",
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
