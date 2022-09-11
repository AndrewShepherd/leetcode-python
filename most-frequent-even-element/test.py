import unittest


from most_frequent_even import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, input, expectedResult):
        sol= Solution()
        result = sol.mostFrequentEven(input)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [0,1,2,2,4,4,1],
            2
        )

    def test_5(self):
        self.run_test(
           [4,4,4,9,2,4],
            4,
        )

    def test_3(self):
        self.run_test(
           [29,47,21,41,13,37,25,7],
            -1,
        )


try:
    unittest.main()
except SystemExit:
    None
