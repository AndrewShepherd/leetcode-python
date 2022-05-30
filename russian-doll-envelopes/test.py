import unittest

from russian_doll_envelopes import Solution
from large_testcase import large_testcase

class TestSolution(unittest.TestCase):

    def run_test(self, envelopes, exprectedResult):
        s = Solution()
        result = s.maxEnvelopes(envelopes)
        self.assertEqual(result, exprectedResult)

    def test_3(self):
        self.run_test([[5,4],[6,4],[6,7],[2,3]], 3)

    def test_4(self):
        self.run_test([[1,1],[1,1],[1,1]], 1)

    def test_5(self):
        self.run_test(large_testcase, 127) 

    def test_2(self):
        self.run_test([[46,89],[50,53],[52,68],[72,45],[77,81]], 3)

    def test_1(self):
        self.run_test([[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]], 7)
try:
    unittest.main()
except SystemExit:
    None
