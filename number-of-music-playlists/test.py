import unittest

from number_of_music_playlists import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        n = 3
        goal = 3
        k = 1
        expected_result = 6
        self.assertEqual(expected_result, s.numMusicPlaylists(n, goal, k))


    def test_2(self):
        s = Solution()
        n = 2
        goal = 3
        k = 0
        expected_result = 6
        self.assertEqual(expected_result, s.numMusicPlaylists(n, goal, k))


    def test_3(self):
        s = Solution()
        n = 2
        goal = 3
        k = 1
        expected_result = 2
        self.assertEqual(expected_result, s.numMusicPlaylists(n, goal, k))
       

try:
    unittest.main()
except SystemExit:
    None






