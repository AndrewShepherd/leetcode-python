import unittest


from minimum_lines_to_represent_a_line_chart import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, stock_prices, expectedResult):
        sol= Solution()
        result = sol.minimumLines(stock_prices)
        self.assertEqual(result, expectedResult)

    def test_1(self):
        self.run_test(
            [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]],
            3
        )

    def test_5(self):
        self.run_test(
            [[93,6],[87,11],[26,58],[28,1],[69,87],[45,59],[29,3],[5,58],[60,94],[46,54],[38,58],[88,10],[94,7],[72,96],[2,93],[63,54],[74,22],[77,84],[33,64],[13,71],[78,59],[76,93],[3,31],[7,95],[68,32],[27,61],[96,31],[4,67],[75,36],[67,21],[8,66],[83,66],[71,58],[6,36],[34,7],[86,78]],
            35,
        )

    def test_2(self):
        self.run_test([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]], 3)

    def test_3(self):
        self.run_test([[3,4],[1,2],[7,8],[2,3]], 1)

    def test_4(self):
        self.run_test(
            [[36,9],[17,93],[34,4],[30,11],[11,41],[53,36],[5,92],[81,92],[28,36],[3,45],[72,33],[64,1],[4,70],[16,73],[99,20],[49,33],[47,74],[83,91]],
            17
        )

try:
    unittest.main()
except SystemExit:
    None
