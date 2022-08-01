class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if k == 0 and tickets[k] == 1:
            return 1
            
        target = tickets[k]
        count = 0
        target_len = 0
        for i in tickets[:k]:
            if i < tickets[k]:
                target_len += 1
        print(target_len)
        
        
        while target > 0:
            temp = []
            for i in range(len(tickets)):
                tickets[i] -= 1
                if tickets[i] > 0:
                    temp.append(tickets[i])
            
            target -= 1
            if target <= 0 and k:
                print(temp)
                count += k + 1 - target_len
            else:
                count += len(tickets)
            
            tickets = [] + temp
            # print(tickets)
            
        return count