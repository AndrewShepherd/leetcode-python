from collections import defaultdict

def compareEntries(left, right):
    if left[0] < right[0]:
        return 1
    elif left[0] > right[0]:
        return -1
    elif left[1] < right[1]:
        return -1
    elif right[1] < left[1]:
        return 1
    else:
        return 0

class FoodRatingCategory:
    def __init__(self):
        self.foodIndexLookup = dict()
        self.heapSortedFoods = []

    def updateIndexLookup(self, index):
        entry = self.heapSortedFoods[index]
        self.foodIndexLookup[entry[1]] = index

    def swap(self, left, right):
        l = self.heapSortedFoods
        l[left], l[right] = l[right], l[left]
        self.updateIndexLookup(left)
        self.updateIndexLookup(right)

    def compareIndexes(self, i1, i2):
        e1 = self.heapSortedFoods[i1]
        e2 = self.heapSortedFoods[i2]
        return compareEntries(e1, e2)

    def heapSortUp(self, index):
        if index == 0:
            return
        upperIndex = (index-1)//2
        if self.compareIndexes(upperIndex, index) > 0:
            self.swap(index, upperIndex)
            self.heapSortUp(upperIndex)
    
    def heapSortDown(self, index):
        i1 = index * 2 + 1
        i2 = index * 2 + 2
        if i1 < len(self.heapSortedFoods) and self.compareIndexes(i1, index) < 0:
            self.swap(index, i1)
            self.heapSortDown(i1)
        if i2 < len(self.heapSortedFoods) and self.compareIndexes(i2, index) < 0:
            self.swap(index, i2)
            self.heapSortDown(i2)

    def addFood(self, name, rating):
        self.heapSortedFoods.append((rating, name))
        self.updateIndexLookup(len(self.heapSortedFoods) - 1)
        self.heapSortUp(len(self.heapSortedFoods)-1)

    def changeRating(self, name, rating):
        queueIndex = self.foodIndexLookup[name]
        self.heapSortedFoods[queueIndex] = (rating, name)
        self.heapSortDown(queueIndex)
        self.heapSortUp(queueIndex)

    def highestRating(self):
        return self.heapSortedFoods[0][1]


class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.cuisines = defaultdict(FoodRatingCategory)
        self.foodLookup = dict()

        for index in range(len(foods)):
            food = foods[index]
            rating = ratings[index]
            cuisine = cuisines[index]

            self.cuisines[cuisine].addFood(food, rating)
            self.foodLookup[food] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.cuisines[self.foodLookup[food]]
        cuisine.changeRating(food, newRating)

    def highestRated(self, cuisine: str) -> str:
        cuisine = self.cuisines[cuisine]
        return cuisine.highestRating()

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)