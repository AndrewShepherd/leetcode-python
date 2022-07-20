from move_pieces_to_obtain_a_string import Solution
import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        s = Solution()
        result = s.canChange("_L__R__R_", "L______RR")
        self.assertEqual(True,result)

    def test_2(self):
        s = Solution()
        result = s.canChange("R_L_", "__LR")
        self.assertEqual(False,result)

    def test_1(self):
        s = Solution()
        result = s.canChange("_R", "R_")
        self.assertEqual(False, result)

    def test_3(self):
        s = Solution()
        result = s.canChange("_LLLL", "LL_LL")
        self.assertEqual(True, result)



try:
    unittest.main()
except SystemExit:
    None