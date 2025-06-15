import unittest
from min_moves_to_clean_the_classroom import Solution

class TestSolution(unittest.TestCase):

    def test_01(self):
        classroom = ["S.", "XL"]
        energy = 2
        expectedResult = 2
        sol = Solution()
        result = sol.minMoves(classroom, energy)
        self.assertEqual(expectedResult, result)

    def test_02(self):
        classroom = ["LS", "RL"]
        energy = 4
        expectedResult = 3
        sol = Solution()
        result = sol.minMoves(classroom, energy)
        self.assertEqual(expectedResult, result)

    def test_03(self):
        classroom = ["L.S", "RXL"]
        energy = 3
        expectedResult = -1
        sol = Solution()
        result = sol.minMoves(classroom, energy)
        self.assertEqual(expectedResult, result)

    def test_04(self):
        classroom = ["L", "S", "R"]
        energy = 2
        expectedResult = 1
        sol = Solution()
        result = sol.minMoves(classroom, energy)
        self.assertEqual(expectedResult, result)


    #
    # R L
    # S L
    # L R
    def test_05(self):
        classroom = ["RL", "SL", "LR"]
        energy = 2
        expectedResult = 4
        sol = Solution()
        result = sol.minMoves(classroom, energy)
        self.assertEqual(expectedResult, result)


    def test_06(self):
        classroom = ["S...................", "....................", "....................", "....................", ".....RL........RR...", "....................", "......L....R..L.....", ".....L..............", ".........L........LL", "....................", "....................", "....................", "........L...........", "....................", "....................", "....................", "....L...............", "....................", ".....R..............", "..............L....."]
        energy = 20
        expectedResult = 71
        sol = Solution()
        result = sol.minMoves(classroom, energy)
        self.assertEqual(expectedResult, result)

    def test_07(self):
        classroom = ["XR.XRX.....RR..XX..R", "RR..XRXRXR.RR..X.RRL", ".RLRX.R.XXRX....XR.R", "RX..X..XRRR.RX..R...", "XRLRR..X.RX.RR...RR.", "XXRXXXX.X..RR....RX.", "RRR.RR..XXXX.R.X....", "RRX.R..RXR...RRXXR.R", "RRR..X..X..RRXXRXRRR", "X.XRXRR.XR.XX.LRRR.X", "RX..RX.XRXRX.X.SR.R.", ".XXXXXR.XXRXLRRX.RLR", ".XRRR.XLXR..XR.RRRRX", "RX.XXLXRRRX..LRXRR..", "RRRRRRR.R.XR.RXR..RR", "R..XXXRRRXRX.XX..RRR", "RRXX.XX..RR..XX..XRR", ".XR..X.RXXRX...RXXRR", "XXX.XX.RLRX.RRXXXR.X", "RXX.RXXX..X.XX..R..R"]
        energy = 23
        expectedResult = 75
        sol = Solution()
        result = sol.minMoves(classroom, energy)
        self.assertEqual(expectedResult, result)

    def test_00(self):
        classroom = ["LR", ".S", ".L", "XR"]
        energy = 5
        expected_result = 4
        sol = Solution()
        result = sol.minMoves(classroom, energy)
        self.assertEqual(expected_result, result)

try:
    unittest.main()
except SystemExit:
    None














