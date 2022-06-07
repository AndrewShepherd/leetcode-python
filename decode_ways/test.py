import unittest


from decode_ways import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, s, expectedResult):
        sol= Solution()
        result = sol.numDecodings(s)
        self.assertEqual(result, expectedResult)

    def test_2(self):
        self.run_test(
            "12",
            2
        )

    def test_4(self):
        self.run_test(
            "226",
            3
        )

    def test_3(self):
        self.run_test(
            "06",
            0
        )

    def test_1(self):
        self.run_test(
            "2611055971756562",
            4
        )

try:
    unittest.main()
except SystemExit:
    None
