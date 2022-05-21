import unittest
from network_delay_time import Solution

class TestSolution(unittest.TestCase):
    def run_test(self, times, n, k, expected):
        s = Solution()
        result = s.networkDelayTime(times, n, k)
        self.assertEqual(result, expected)

    def test_1(self):
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2
        self.run_test(times, n, k, 2)

    def test_2(self):
        times = [[1,2,1]]
        n = 2
        k = 1
        self.run_test(times, n, k, 1)

    def test_3(self):
        times = [[1,2,1]]
        n = 2
        k = 2
        self.run_test(times, n, k, -1)

    def test_4(self):
        times = [[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]]
        n = 5
        k = 1
        self.run_test(times, n, k, 69)

try:
    unittest.main()
except SystemExit:
    None