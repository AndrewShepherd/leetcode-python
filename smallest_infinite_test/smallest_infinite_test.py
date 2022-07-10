import heapq

class SmallestInfiniteSet:


    def __init__(self):
        self.rangeStart = 1
        self.addedBack = []

    def popSmallest(self) -> int:
        if self.addedBack:
            return heapq.heappop(self.addedBack)
        else:
            result = self.rangeStart
            self.rangeStart += 1
            return result

    def addBack(self, num: int) -> None:
        if num >= self.rangeStart:
            return
        for n in self.addedBack:
            if num == n:
                return
        heapq.heappush(self.addedBack, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)