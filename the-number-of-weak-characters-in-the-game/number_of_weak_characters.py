from collections import defaultdict

class StrengthNode:

    def __init__(self, max_defense = 0, count = 0):
        self.max_defense = max_defense
        self.count = count

    def onNext(self, defense):
        return StrengthNode(max(self.max_defense, defense), self.count + 1)



class Solution:
    def numberOfWeakCharacters(self, properties) -> int:

        max_defense_for_attacker = defaultdict(lambda: 0)
        for attack,defense in properties:
            max_defense_for_attacker[attack] = max(max_defense_for_attacker[attack], defense)

        max_defense_for_attacker = sorted(max_defense_for_attacker.items(), key = lambda p: 0-p[0])

        highest_defense_of_larger = dict()

        highest_defense_so_far = 0

        for attack, defense in max_defense_for_attacker:
            highest_defense_of_larger[attack] = highest_defense_so_far
            highest_defense_so_far = max(highest_defense_so_far, defense)

        count = 0
        for attack, defense in properties:
            if defense < highest_defense_of_larger[attack]:
                count += 1
        return count