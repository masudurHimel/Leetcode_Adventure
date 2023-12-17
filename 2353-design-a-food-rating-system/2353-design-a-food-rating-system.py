class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.index = {food: i for i, food in enumerate(foods)}
        self.cuisines_map = defaultdict(list)

        for i, (cuisine, rating, food) in enumerate(zip(cuisines, ratings, foods)):
            heappush(self.cuisines_map[cuisine], (-rating, food))

    def changeRating(self, food: str, new_rating: int) -> None:
        i = self.index[food]
        self.ratings[i] = new_rating
        cuisine = self.cuisines[i]
        heappush(self.cuisines_map[cuisine], (-new_rating, food))

    def highestRated(self, cuisine: str) -> str:
        rating, food = self.cuisines_map[cuisine][0]
        
        while rating != -self.ratings[self.index[food]]:
            heappop(self.cuisines_map[cuisine])
            rating, food = self.cuisines_map[cuisine][0]

        return food
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)