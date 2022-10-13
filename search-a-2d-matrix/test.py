import unittest


from search_matrix import Solution


class TestSolution(unittest.TestCase):

    def run_test(self, matrix, target, expectedResult):
        sol= Solution()
        result = sol.searchMatrix(matrix, target)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True)

    def test_2(self):
        self.run_test(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13, expectedResult = False)

    def test_0(self):
        self.run_test([[1]], 2, False)



try:
    unittest.main()
except SystemExit:
    None






