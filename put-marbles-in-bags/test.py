import unittest
from put_marbles import Solution


class TestSolution(unittest.TestCase):

    def test_0(self):
        weights = [1,4,2,5,2]
        k = 3
        s = Solution()
        result = s.putMarbles(weights, k)
        #[1][4][2,5,2] = 9   
        #[1][4, 2], 5[2] = 12
        # 
        # (5+4+2+2) - (1+2+2+4) =  
        self.assertEqual(3, result)


    def test_2(self):
        weights = [1,2,3,4,5]
        k = 1
        s = Solution()
        result = s.putMarbles(weights, k)
        self.assertEqual(0, result)

    def test_5(self):
        weights = [1,3,5,1]
        k = 2
        s = Solution()
        result = s.putMarbles(weights, k)
        self.assertEqual(4, result)

    def test_4(self):
        weights = [1,3]
        k = 1
        s = Solution()
        result = s.putMarbles(weights, k)
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None
