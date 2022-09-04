import unittest
from build_a_matrix_with_special_conditions import Solution




class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]])
        self.assertEqual([[3,0,0],[0,0,1],[0,2,0]], result)

    def test_0(self):
        s = Solution()
        result = s.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]])
        self.assertEqual([], result)

 

try:
    unittest.main()
except SystemExit:
    None
