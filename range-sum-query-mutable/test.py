from range_sum_query_mutable import NumArray

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = NumArray([1, 3, 5])

        result = s.sumRange(0, 2)
        self.assertEqual(9, result)
        s.update(1, 2)
        result = s.sumRange(0, 2)
        self.assertEqual(8, result)

    def test_2(self):
        s = NumArray([0,9,5,7,3])
        result = s.sumRange(4,4)
        self.assertEqual(3, result)
        result = s.sumRange(2,4)
        self.assertEqual(15, result)

    def test_3(self):
        s = NumArray([7,2,7,2,0])

        result = s.sumRange(0, 3)
        self.assertEqual(7 + 2 + 7 + 2, result)


        s.update(4, 6)
        s.update(0, 2)
        s.update(0, 9)
        result = s.sumRange(4, 4)
        self.assertEqual(6, result)
        s.update(3, 8)
        result = s.sumRange(0, 4)
        self.assertEqual(32, result)

        result = s.sumRange(0, 3)
        self.assertEqual(26, result)


        s.update(4, 1)
        result = s.sumRange(0, 3)
        self.assertEqual(26, result)


try:
    unittest.main()
except SystemExit:
    None