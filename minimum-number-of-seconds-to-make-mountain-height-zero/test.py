import unittest


from minimum_number_of_seconds_to_make_mountain_height_zero import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        mountainHeight = 4
        workerTimes = [2,1,1]
        result = s.minNumberOfSeconds(mountainHeight, workerTimes)
        self.assertEqual(3, result)

    def test_2(self):
        s = Solution()
        mountainHeight = 10
        workerTimes = [3,2,2,4]
        result = s.minNumberOfSeconds(mountainHeight, workerTimes)
        self.assertEqual(12, result)

    def test_3(self):
        s = Solution()
        mountainHeight = 5
        workerTimes = [1]
        result = s.minNumberOfSeconds(mountainHeight, workerTimes)
        self.assertEqual(15, result)

try:
    unittest.main()
except SystemExit:
    None











