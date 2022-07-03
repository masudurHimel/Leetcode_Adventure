class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck_hash = {}
        for i in deck:
            deck_hash[i] = deck_hash.get(i, 0) + 1
            
#         target_val = list(deck_hash.values())[0]
        
#         for i in range(2, target_val//2):
#             if target_val%i==0:
#                 target_val = i
#                 break
        gcm_list = []

        for i in deck_hash.values():
            if i < 2:
                return False
            gcm_list.append(i)
        return math.gcd(*gcm_list) >= 2