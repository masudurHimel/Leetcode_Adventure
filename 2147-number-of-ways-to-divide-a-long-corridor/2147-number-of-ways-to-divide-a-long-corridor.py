class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7

        if corridor.count("S") % 2 or corridor.count("S") == 0:
            return 0

        seats = 0
        res = 1
        plant_in_row = 0

        for char in corridor:
            if char == "S":
                if seats == 2:
                    seats = 1
                    res *= (plant_in_row + 1)
                    plant_in_row = 0
                else:
                    seats += 1
            else:
                if seats == 2:
                    plant_in_row += 1

        return res % mod
