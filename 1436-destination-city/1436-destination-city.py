class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cache = {}

        for path in paths:
            cityA, cityB = path

            if cityA in cache:
                cache[cityA][0] += 1
                cache[cityA][1] = 0
            else:
                cache[cityA] = [1, 0]

            if cityB in cache:
                cache[cityB][0] += 1
                cache[cityB][1] = 1
            else:
                cache[cityB] = [1, 1]

        for city, (count, destination) in cache.items():
            if count == 1 and destination == 1:
                return city
