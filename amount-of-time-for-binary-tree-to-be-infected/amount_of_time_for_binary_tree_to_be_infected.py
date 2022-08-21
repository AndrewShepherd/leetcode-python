from collections import defaultdict

class Solution:
    def amountOfTime(self, root, start: int) -> int:
        d = defaultdict(set)

        def populate(n):
            if n.left:
                d[n.val].add(n.left.val)
                d[n.left.val].add(n.val)
                populate(n.left)
            if n.right:
                d[n.val].add(n.right.val)
                d[n.right.val].add(n.val)
                populate(n.right)
        populate(root)

        visited = set()
        q = [(start, 0)]
        max_length = 0
        while q:
            n,l = q.pop(0)
            if n in visited:
                continue
            visited.add(n)
            for destNode in d[n]:
                if destNode not in visited:
                    q.append((destNode,l+1))
            max_length = max(max_length, l)
        return max_length