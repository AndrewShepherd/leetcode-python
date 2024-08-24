class Solution:
    def maxEnergyBoost(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        dpa = (sum(energyDrinkA[-2:]), energyDrinkA[-1])
        dpb = (sum(energyDrinkB[-2:]), energyDrinkB[-1])
        for i in range(len(energyDrinkA)-3, -1, -1):
            dpa2 = (
                max(energyDrinkA[i] + dpa[0], energyDrinkA[i] + dpb[1]),
                dpa[0]
            )
            dpb2 = (
                max(energyDrinkB[i] + dpb[0], energyDrinkB[i] + dpa[1]),
                dpb[0]
            )
            dpa, dpb = dpa2, dpb2 


        return max(dpa[0], dpb[0])
