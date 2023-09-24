import unittest

from maximum_number_of_alloys import Solution, calculateForMachine


class TestSolution(unittest.TestCase):

    def test_0(self):
        solution = Solution()
        n = 9
        k = 3
        budget = 90
        composition = [[10,9,1,3,3,5,5,10,7],[2,6,4,9,9,1,9,6,7],[1,4,7,6,7,7,10,6,6]]
        stock = [3,10,10,8,10,5,7,1,2]
        cost = [9,8,10,9,9,3,9,5,8]
        result = solution.maxNumberOfAlloys(n, k, budget, composition, stock, cost)
        self.assertEqual(1, result)

    def test_1(self):
        solution = Solution()
        n = 3
        k = 2
        budget = 15
        composition = [[1,1,1],[1,1,10]]
        stock = [0,0,0]
        cost = [1,2,3]
        result = solution.maxNumberOfAlloys(n, k, budget, composition, stock, cost)
        self.assertEqual(2, result)

    def test_2(self):
        solution = Solution()
        n = 3
        k = 2
        budget = 15
        composition = [[1,1,1],[1,1,10]]
        stock = [0,0,100]
        cost = [1,2,3]
        result = solution.maxNumberOfAlloys(n, k, budget, composition, stock, cost)
        self.assertEqual(5, result)

    def test_3(self):
        solution = Solution()
        n = 2
        k = 3
        budget = 10
        composition = [[2,1],[1,2],[1,1]]
        stock = [1,1]
        cost = [5,5]
        result = solution.maxNumberOfAlloys(n, k, budget, composition, stock, cost)
        self.assertEqual(2, result)

    def test_4(self):
        result = calculateForMachine(10, [1, 1], [1, 1], [5, 5])
        self.assertEqual(2, result)
try:
    unittest.main()
except SystemExit:
    None










