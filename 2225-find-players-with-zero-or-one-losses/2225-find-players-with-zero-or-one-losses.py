class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_dict = {}
        loser_dict = {}
        counter_dict = {}
        
        for match in matches:
            winner, loser = match[0], match[1]
            winner_dict[winner] = winner_dict.get(winner, 0) + 1
            
            if winner_dict.get(loser):
                winner_dict[loser] = winner_dict.get(loser, 0) - 1
            
            loser_dict[loser] = loser_dict.get(loser, 0) + 1
            
            counter_dict[winner] = counter_dict.get(winner, 0) + 1
            counter_dict[loser] = counter_dict.get(loser, 0) + 1
            
        winner_res = []
        loser_res = []
        
        for i in winner_dict:
            if winner_dict[i] == counter_dict.get(i, 0):
                winner_res.append(i)
            
        for i in loser_dict:
            if loser_dict[i] == 1:
                loser_res.append(i)
                
        return [sorted(winner_res), sorted(loser_res)]
        