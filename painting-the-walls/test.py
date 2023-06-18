import unittest


from painting_the_walls import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        s = Solution()

        cost = [1,2,3,2]
        time = [1,2,3,2]
        expected = 3
        result = s.paintWalls(cost, time)
        self.assertEqual(result, expected)

    def test_1(self):
        s = Solution()

        cost = [2,3,4,2]
        time = [1,1,1,1]
        expected = 4
        result = s.paintWalls(cost, time)
        self.assertEqual(result, expected)

    def test_0(self):
        s = Solution()

        cost = [26,53,10,24,25,20,63,51]
        time = [1,1,1,1,2,2,2,1]
        expected = 55
        result = s.paintWalls(cost, time)
        self.assertEqual(result, expected)

    def test_3(self):
        s = Solution()

        cost = [518,1033,1025,939,2184,2142,1623,194,660,243,1957,1883,1313,210,1940,1825,1896,315,149,1632,721,1496,1498,1824,1199,1920,2170,4,1294,516,997,426,169,1016,2129,1411,2190,1475,1430,465,2174,986,982,2025,1377,1110,448]
        time = [2,4,2,4,1,1,3,1,5,1,3,5,6,6,2,2,6,3,3,1,3,2,3,2,1,6,1,6,4,2,2,1,5,1,5,4,5,3,5,3,4,5,1,6,3,1,4]

        expected = 2857
        result = s.paintWalls(cost, time)
        self.assertEqual(result, expected)

    def test_4(self):
        s = Solution()
        cost = [2173,1293,760,1400,1164,1091,488,448,605,780,1359,1706,236,574,23,1505,1776,1252,379,1432,238,1647,1155,1424,967,2004,668,1635,342,1496,1729,294,1113,211,1395,3,341,2046,1077,1769,406,2050,853,2184,2165,1609,1845]
        time = [2,6,6,4,4,6,1,1,4,2,1,3,2,2,5,5,6,5,5,4,5,6,6,5,5,6,1,1,2,2,1,3,5,3,2,6,3,1,2,1,6,3,1,4,4,5,1]

        expected = 2131
        result = s.paintWalls(cost, time)
        self.assertEqual(result, expected)

    def test_5(self):
        s = Solution()
        cost = [1492,1059,343,1037,471,218,1370,324,1475,228,683,860,123,923,628,960,622,634,1269,1400,265,532,152,965,1114,220,388,424,406,473,818,986,505,542,1184,964,1215,1485,1243]
        time = [1,1,4,1,1,6,6,1,1,2,4,2,1,4,5,4,4,2,1,5,1,2,6,1,5,1,5,2,3,1,3,4,3,2,2,1,1,6,1]
        expected = 2478
        result = s.paintWalls(cost, time)
        self.assertEqual(result, expected)
try:
    unittest.main()
except SystemExit:
    None














