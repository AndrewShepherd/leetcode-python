import unittest


from hardest_worker import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, n, logs, expectedResult):
        sol= Solution()
        result = sol.hardestWorker(n, logs)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            10, [[0,3],[2,5],[0,9],[1,15]],
            1
        )

    def test_2(self):
        self.run_test(
            26,[[1,1],[3,7],[2,12],[7,17]],
            3
        )

    def test_3(self):
        self.run_test(
            70, [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]],
            12,
        )


try:
    unittest.main()
except SystemExit:
    None



