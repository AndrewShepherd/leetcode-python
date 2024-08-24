import unittest

from maximum_energy_boost import Solution

class TestSolution(unittest.TestCase):

    def test_1(self):
        energyDrinkA = [1,3,1]
        energyDrinkB = [3,1,1]
        sol = Solution()
        output = sol.maxEnergyBoost(energyDrinkA, energyDrinkB)
        self.assertEqual(output, 5)

    def test_2(self):
        energyDrinkA = [4,1,1]
        energyDrinkB = [1,1,3]
        sol = Solution()
        output = sol.maxEnergyBoost(energyDrinkA, energyDrinkB)
        self.assertEqual(output, 7)







try:
    unittest.main()
except SystemExit:
    None




















