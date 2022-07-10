import unittest


from smallest_infinite_test import SmallestInfiniteSet

class TestSolution(unittest.TestCase):

    def test_1(self):
        sis = SmallestInfiniteSet()
        sis.addBack(2)
        self.assertEqual(
            sis.popSmallest(),
            1
        )
        self.assertEqual(
            sis.popSmallest(),
            2
        )
        self.assertEqual(
            sis.popSmallest(),
            3
        )
        sis.addBack(1)
        self.assertEqual(
            sis.popSmallest(),
            1
        )
        self.assertEqual(
            sis.popSmallest(),
            4
        )
        self.assertEqual(
            sis.popSmallest(),
            5
        )

try:
    unittest.main()
except SystemExit:
    None
