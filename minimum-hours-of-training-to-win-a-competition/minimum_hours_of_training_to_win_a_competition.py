class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy, experience) -> int:
        minimumEnergyRequired = sum(energy)+1

        minimumExperienceRequired = 0
        
        gainedExperience = 0
        for (i, e) in enumerate(experience):
            minimumExperienceRequired = max(minimumExperienceRequired, e-gainedExperience+1)
            gainedExperience += e
        return max(minimumEnergyRequired - initialEnergy, 0) + max(minimumExperienceRequired-initialExperience, 0)