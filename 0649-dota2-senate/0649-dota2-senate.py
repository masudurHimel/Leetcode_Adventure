class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        senate = list(senate)
        length = len(senate)

        r_arr = []
        d_arr = []

        for i in range(len(senate)):
            if senate[i] == "R":
                r_arr += [i]
            else:
                d_arr += [i]

        while r_arr and d_arr:
            r_senate = r_arr.pop(0)
            d_senate = d_arr.pop(0)

            if r_senate < d_senate:
                r_arr += [r_senate + length]
            else:
                d_arr += [d_senate + length]

        if len(r_arr) == 0:
            return "Dire"
        else:
            return "Radiant"