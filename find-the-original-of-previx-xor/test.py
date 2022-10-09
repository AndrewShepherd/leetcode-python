import unittest


from find_the_original_of_prefix_xor import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, pref, expectedResult):
        sol= Solution()
        result = sol.findArray(pref)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [5,2,0,3,1],
            [5,7,2,3,2]
        )

    def test_2(self):
        self.run_test(
            [13],
            [13]
        )


try:
    unittest.main()
except SystemExit:
    None




