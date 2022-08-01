from maximum_number_of_groups_entering_a_competition import Solution

import unittest

class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.maximumGroups([10,6,12,7,3,5])
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        result = s.maximumGroups([8,8])
        self.assertEqual(1,result)

try:
    unittest.main()
except SystemExit:
    None