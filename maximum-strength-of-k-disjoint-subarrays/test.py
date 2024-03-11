import unittest

from maximum_strength import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        s = Solution()
        nums = [-6381,-98262,-23255,39031,-45666,-5830,-51549,-16181,-66819,79784,86742,-90776,43072,-67153,-96178,-40818,58314,3223,14328,-80415,-32635,24212,-97424,-15808,-79862,-45280,-68732,-65450,-25592,52107,19340,-549,-88679,45310,-38686,-95951,39337,69821,-31786,-40566,-11272,9360,-13283,-68772,-93316,76919,47806,72346,-77696,43142,75905,-83739,-90780,-26099,-79015,-17369,41265,10920,-46249,90159,43276,-27937,72970,-54782,30022,-51525,89112,-93644,1774,-74229,-77828,-46488,98166,37940,55935,69926,20055,-60480,44099,-97955,-12206,-47417,43189,-67159,-60495,81865,93909,-1562,90082,9731,-20295,70529,41442,-93124,-5660,38921,58189,-63006,24768,-90463]
        k = 49
        self.assertEqual(148010755, s.maximumStrength(nums, k))

    def test_1(self):
        s = Solution()
        nums = [1,2,3,-1,2]
        k = 3
        self.assertEqual(22, s.maximumStrength(nums, k))

    def test_2(self):
        s = Solution()
        nums = [12,-2,-2,-2,-2]
        k = 5
        self.assertEqual(64, s.maximumStrength(nums, k))

    def test_3(self):
        s = Solution()
        nums = [-1,-2,-3]
        k = 1
        self.assertEqual(-1, s.maximumStrength(nums, k))



       

try:
    unittest.main()
except SystemExit:
    None












