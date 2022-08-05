class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        
        tok, pair = False, False
        ranks_map = Counter(ranks)
        
        for i in ranks_map.values():
            if i >= 3:
                return "Three of a Kind"
            
            if i >= 2:
                pair = True
        
        if pair:
            return "Pair"
        return "High Card"