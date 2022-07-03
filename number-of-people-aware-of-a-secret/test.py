import unittest
from number_of_people_aware_of_a_secret import Solution





class TestSolution(unittest.TestCase):


    def test_0(self):
        s = Solution()
        result = s.peopleAwareOfSecret(6, 2, 4)
        self.assertEqual(result, 5)

    def test_1(self):
        s = Solution()
        result = s.peopleAwareOfSecret(4, 1, 3)
        self.assertEqual(result, 6)

    def test_2(self):
        s = Solution()
        result = s.peopleAwareOfSecret(684, 18, 496)
        self.assertEqual(result, 653668527)

try:
    unittest.main()
except SystemExit:
    None