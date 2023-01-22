import unittest
from sort_students import Solution



class TestSolution(unittest.TestCase):

    def test_0(self):
        score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
        k = 2
        expected = [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
        s = Solution()
        generated = s.sortTheStudents(score, k)
        self.assertEqual(generated, expected)


try:
    unittest.main()
except SystemExit:
    None







