import unittest

from select_cells_in_grid_with_maximum_score import Solution


class TestSolution(unittest.TestCase):


    def test_0(self):
        sol = Solution()
        grid = [[] for _ in range(10)]
        n = 100
        toggle = True
        for q in range(9, 0, -1):
            if toggle:
                for q2 in range(q):
                    grid[q2].append(n)
            else:
                for q2 in range(len(grid)-1, len(grid)-1-q, -1):
                    grid[q2].append(n)
            n -= 1
        for i,r in enumerate(grid):
            to_add = 10 - len(r)
            r.extend(range(i, i + to_add))
        result = sol.maxScore(grid)
        self.assertEqual(882, result)



    def test_1(self):
        sol = Solution()
        grid = [[8,7,6],[8,3,2]]
        result = sol.maxScore(grid)
        self.assertEqual(15, result)

    def test_2(self):
        sol = Solution()
        grid = [
            list(range(1, 11))
            for _ in range(10)
        ]
        result = sol.maxScore(grid)
        self.assertEqual(55, result) 

    def test_3(self):
        sol = Solution()
        grid = [1,2,3],[4,3,2],[1,1,1]
        result = sol.maxScore(grid)
        self.assertEqual(8, result)      

    def test_4(self):
        sol = Solution()
        grid = [[5],[7],[19],[5]]
        result = sol.maxScore(grid)
        self.assertEqual(19+7+5, result) 

    def test_5(self):
        sol = Solution()
        grid = [[8,11,3],[17,7,3],[13,20,3],[3,17,20]]
        result = sol.maxScore(grid)
        self.assertEqual(20 + 17 + 13 + 11, result)

    def test_6(self):
        sol = Solution()
        grid = [[16,14],[5,4],[7,16]]
        result = sol.maxScore(grid)
        self.assertEqual(16 + 14 + 5, result)

    def test_7(self):
        sol = Solution()
        grid = [[8,8,14],[7,18,14],[12,15,15],[3,15,13]]
        result = sol.maxScore(grid)
        self.assertEqual(18 + 15 + 14 + 13, result)


try:
    unittest.main()
except SystemExit:
    None



















