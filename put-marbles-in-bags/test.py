import unittest
from put_marbles import Solution


class TestSolution(unittest.TestCase):

    def test_2(self):
        weights = [1,3,5,1]
        k = 2
        s = Solution()
        result = s.putMarbles(weights, k)
        #[1][4][2,5,2] = (1+1) + (4+4)+(2+2) = 2 + 8 + 4 = 12
        #[1, 4, 2][5][2] = (5+5) + (2) + (3) = 15
        # 
        # (5+4+2+2) - (1+2+2+4) =  
        self.assertEqual(4, result)


    def test_1(self):
        weights = [1,4,2,5,2]
        k = 3
        s = Solution()


        # k = 1
        # [1], [1,4], [1,2]

        # k = 2
        # min [1][4]  (10) # max [1,4] (10)
        # min [1][4,2]=8 # max [1,4][2] = 9
        # min [1][4,2,5] = 10 # max [1,4,2][5] = 13  


        #[1][4][2,5,2] = (1+1) + (4+4)+(2+2) = 2 + 8 + 4 = 12
        #[1, 4, 2][5][2] = (5+5) + (2) + (3) = 15
        # 
        # (5+4+2+2) - (1+2+2+4) =  

        result = s.putMarbles(weights, k)

        self.assertEqual(3, result)


    def test_6(self):
        weights = [54,6,34,66,63,52,39,62,46,75,28,65,18,37,18,13,33,69,19,40,13,10,43,61,72]
        k = 4
        s = Solution()
        result = s.putMarbles(weights, k)
        self.assertEqual(289, result)

    def test_3(self):
        weights = [1,2]
        k = 1
        s = Solution()
        result = s.putMarbles(weights, k)
        self.assertEqual(0, result)


    def test_0(self):
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
