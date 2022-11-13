import unittest
from convert_the_temperature import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        result = s.convertTemperature(36.50)
        self.assertEqual([309.65000,97.70000], result)

    def test_2(self):
        s = Solution()
        result = s.convertTemperature(122.11)
        self.assertEqual([395.26000,251.79800], result)
try:
    unittest.main()
except SystemExit:
    None





