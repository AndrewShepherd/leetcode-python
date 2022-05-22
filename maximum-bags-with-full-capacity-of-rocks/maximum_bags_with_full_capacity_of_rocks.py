def getDifferences(l1, l2):
    for i in range(len(l1)):
        yield l1[i] - l2[i]

class Solution(object):


    def maximumBags(self, capacity, rocks, additionalRocks):
        differences = dict()
        for d in getDifferences(capacity, rocks):
            differences[d] = differences.get(d, 0) + 1
        
        count = 0
        for required in sorted(differences.keys()):
            bagQuantity = differences[required]
            taken = min(
                bagQuantity, 
                bagQuantity if required == 0 else additionalRocks // required
            )
            if taken == 0:
                break
            additionalRocks -= taken * required
            count += taken
        return count

        