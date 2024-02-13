import unittest, big_input

from number_of_arrays_that_match_a_pattern import Solution, smart_search, dumb_search, create_lookup


class TestSolution(unittest.TestCase):

    def test_0(self):
        sol = Solution()
        p = 'aabaaab'
        lookup = create_lookup(p)
        self.assertEqual([0, 1, 0, 1, 2, 2, 3], lookup)

    def test_1(self):
        sol = Solution()
        n = 'vvyzzvzyyyvzvvyvvyvyzyzvvvvvyvvvyzzvzyyyvzvvyvvyvyzyzvvvvvyvvvyzzvvyzzvzyyyvzvvyvvyvyzyzvvvvvyvvvyzz'
        p = 'vvyzzvzyyyvzvvyvvyvyzyzvvvvvyvvvyzz'

        s_result = smart_search(p, n)
        d_result = dumb_search(p, n)

        for i,(s, d) in enumerate(zip(s_result, d_result)):
            print(f'i = {i}, s = {s}, d = {d}')
            if(s != d):
                self.fail(f'i = {i}, s = {s}, d = {d}')
  
  
        nums = big_input.nums
        pattern = big_input.pattern
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(250, result)

    def test_6(self):
        sol = Solution()
        nums = [185323856,6702969,185323856,235305212]
        pattern = [-1, 1]
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(1, result)

    def test_5(self):
        sol = Solution()
        nums = [132030805,226565039,226565039,234134481,362977930,362977930,565625669,651711104,713365290,651711104,713365290,713365290,718731626]
        pattern = [1,0,1,1]
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(2, result)

    def test_4(self):
        sol = Solution()
        nums = [45860857,105553509,105553509,531087159,531087159,105553509]
        pattern = [1,0,1,0]
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(1, result)

    def test_3(self):
        sol = Solution()
        nums = [1,2,3,4,5,6]
        pattern = [1,1]
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(4, result)

    def test_2(self):
        sol = Solution()
        nums = [1,4,4,1,3,5,5,3]
        pattern = [1,0,-1]
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(2, result)

    def test_7(self):
        sol = Solution()
        nums = [481251768,481251768,481251768,463564806]
        pattern = [0]
        result = sol.countMatchingSubarrays(nums, pattern)
        self.assertEqual(2, result)


try:
    unittest.main()
except SystemExit:
    None

















