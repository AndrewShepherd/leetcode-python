import unittest


from minimum_hours_of_training_to_win_a_competition import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        initialEnergy = 5
        initialExperience = 3
        energy = [1,4,3,2]
        experience = [2,6,3,1]
        result = s.minNumberOfHours(initialEnergy, initialExperience, energy, experience)
        self.assertEqual(8, result)

    def test_5(self):
        s = Solution()
        initialEnergy = 2
        initialExperience = 4
        energy = [1]
        experience = [3]
        result = s.minNumberOfHours(initialEnergy, initialExperience, energy, experience)
        self.assertEqual(0, result)

try:
    unittest.main()
except SystemExit:
    None
