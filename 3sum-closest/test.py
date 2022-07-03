import unittest
from threesum_closest import Solution



class TestSolution(unittest.TestCase):


    def test_3(self):
        s = Solution()
        result = s.threeSumClosest([-1,2,1,-4], 1)
        self.assertEqual(result, 2)

    def test_2(self):
        s = Solution()
        result = s.threeSumClosest([0,0,0], 0)
        self.assertEqual(result, 0)

    def test_4(self):
        s = Solution()
        large_input = [4,-94,-14,98,-54,-16,18,-24,47,-84,-57,81,-48,-64,-64,-42,-94,34,-55,-25,-78,25,-32,53,-6,75,-30,-81,-15,-61,36,12,70,36,-44,-100,-69,-50,-6,-45,5,75,-74,-80,-32,0,42,30,25,-36,-94,90,-92,28,8,43,59,15,-38,-55,-34,71,34,-87,100,-61,90,-88,56,-11,56,10,37,-80,-53,11,-56,-28,15,-82,36,-6,-25,-40,-43,78,72,-79,46,-50,59,-18,-76,37,61,-38,94,89,4,-32,46,11,30,92,-15,-7,-70,21,-72,36,8,95,-84,-54,-44,-68,-62,-39,-2,-100,-73,-23,-100,87,34,-69,-28,-78,-79,100,83,45,12,34,-15,-64,41,96,64,77,37,-74,40,9,48,75,42,74,-36,-1,41,71,-85,88,81,13,7,48,-3,-100,-99,13,-92,-94,95,-45,92,84,-14,25,34,11,-57,55,-16,77,-26,88,77,-12,41,-72,5,-75,-93,-14,70,-33,18,-52,-41,14,-18,18,48,98,19,-54,91,-11,95,-41,-84,57,95,1];
        result = s.threeSumClosest(large_input, 69)
        self.assertEqual(result, 69)

    def test_5(self):
        s = Solution()
        result = s.threeSumClosest([-100,-98,-2,-1], -101)
        self.assertEqual(result, -101)

    def test_6(self):
        s = Solution()
        result = s.threeSumClosest([1,1,-1,-1,3], -1)
        self.assertEqual(result, -1)

    def test_1(self):
        s = Solution()
        result = s.threeSumClosest([1,-3,3,5,4,1], 1)
        self.assertEqual(result, 1)

try:
    unittest.main()
except SystemExit:
    None