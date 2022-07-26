from food_rating_system import FoodRatings
import unittest

class TestSolution(unittest.TestCase):


    def test_1(self):
        foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
        self.assertEqual(
            foodRatings.highestRated("korean"),
            "kimchi"
         ) # return "kimchi"
        self.assertEqual(
            foodRatings.highestRated("japanese"),
            "ramen"
         ) # return "ramen"

        self.assertEqual(
            foodRatings.changeRating("sushi", 16),
            None
        ) # "sushi" now has a rating of 16.
        self.assertEqual(
            foodRatings.highestRated("japanese"),
            "sushi"
         ) # return "kimchi"
        foodRatings.changeRating("ramen", 16),
        self.assertEqual(
            foodRatings.highestRated("japanese"),
            "ramen"
         ) # return "ramen"
        self.assertEqual(
            foodRatings.highestRated("japanese"),
            "ramen"
         ) # return "ramen"
        foodRatings.changeRating("ramen", 15),
        self.assertEqual(
            foodRatings.highestRated("japanese"),
            "sushi"
         ) # return "kimchi"["FoodRatings","changeRating","highestRated","highestRated","highestRated"]
 #[[
 # ["cpctxzh","bryvgjqmj","wedqhqrmyc","ee","lafzximxh","lojzxfel","flhs"]
 # ,["wbhdgqphq","wbhdgqphq","mxxajogm","wbhdgqphq","wbhdgqphq","mxxajogm","mxxajogm"],[15,5,7,16,16,10,13]],["lojzxfel",1],["mxxajogm"],["wbhdgqphq"],["mxxajogm"]]
    def test_2(self):
        foods = ["cpctxzh","bryvgjqmj","wedqhqrmyc","ee","lafzximxh","lojzxfel","flhs"]
        categories = ["wbhdgqphq","wbhdgqphq","mxxajogm","wbhdgqphq","wbhdgqphq","mxxajogm","mxxajogm"]
        ratings = [15,5,7,16,16,10,13]

        foodRatings = FoodRatings(foods, categories, ratings)
        foodRatings.changeRating("lojzxfel", 1)
        self.assertEqual(
            foodRatings.highestRated("mxxajogm"),
            "flhs"
        )
        self.assertEqual(
            foodRatings.highestRated("wbhdgqphq"),
            "ee"
        )
        self.assertEqual(
            foodRatings.highestRated("mxxajogm"),
            "flhs"
        )


try:
    unittest.main()
except SystemExit:
    None