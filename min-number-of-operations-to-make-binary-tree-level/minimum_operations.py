def sort_operations(l):
    lBefore = l[:]
    lSorted = sorted(l)
    originalLocations = dict()
    for (i, n) in enumerate(l):
        originalLocations[n] = i
    count = 0
    for i,n in enumerate(l):
        target_value = lSorted[i]
        if n != target_value:
            target_value_location = originalLocations[target_value]
            l[target_value_location] = n
            originalLocations[n] = target_value_location
            l[i] = target_value
            count += 1
    if (l != lSorted):
        raise("Failure")
    return count

def get_next_level(nodes):
    for n in nodes:
        if n.left and n.left.val:
            yield n.left
        if n.right and n.right.val:
            yield n.right

class Solution:
    def minimumOperations(self, root) -> int:
        level = [root]
        count = 0
        while(level):
            level = list(get_next_level(level))
            if not level:
                break
            values = [n.val for n in level]
            count += sort_operations(values)
        return count
