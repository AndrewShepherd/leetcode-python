import unittest

from check_if_rectangle_corner_is_reachable import Solution

class TestSolution(unittest.TestCase):


    def test_1(self):
        X = 500000000
        Y = 500000000
        circles = [[499980000,699999999,200000000],[500020000,300000001,200000000]]
        sol = Solution()
        output = sol.canReachCorner(X, Y, circles)
        self.assertEqual(output, True)

    def test_2(self):
        X = 3
        Y = 3
        circles = [[2,1,1],[1,2,1]]
        sol = Solution()
        output = sol.canReachCorner(X, Y, circles)
        self.assertEqual(output, False)

    def test_3(self):
        X = 5
        Y = 8
        circles = [[4,7,1]]
        sol = Solution()
        output = sol.canReachCorner(X, Y, circles)
        self.assertEqual(output, False)

    def test_4(self):
        X = 8
        Y = 5
        circles = [[2,3,1],[5,4,1],[2,1,1],[5,4,1],[3,2,1],[5,2,2],[7,1,1]]
        sol = Solution()
        output = sol.canReachCorner(X, Y, circles)
        self.assertEqual(output, False)

    def test_5(self):
        X = 3
        Y = 4
        circles = [[2,1,1]]
        sol = Solution()
        output = sol.canReachCorner(X, Y, circles)
        self.assertEqual(output, True)

    def test_6(self):
        X = 3
        Y = 3
        circles = [[2,1000,997],[1000,2,997]]
        sol = Solution()
        output = sol.canReachCorner(X, Y, circles)
        self.assertEqual(output, True)

    def test_7(self):
        X = 15
        Y = 15
        # These two circles intersect
        # but the areas of intesection fall outside the rectangle
        circles = [[1,99,85],[99,1,85]]


        sol = Solution()
        output = sol.canReachCorner(X, Y, circles)
        self.assertEqual(output, True)

    def test_8(self):
        X = 15
        Y = 15
        circles = [[2,20,13],[20,2,13]]
        sol = Solution()
        output = sol.canReachCorner(X, Y, circles)
        self.assertEqual(output, False)




try:
    unittest.main()
except SystemExit:
    None

















