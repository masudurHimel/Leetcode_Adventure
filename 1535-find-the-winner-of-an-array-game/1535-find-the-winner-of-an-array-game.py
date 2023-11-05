class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n=len(arr)
        if(k>=n or arr[0]==max(arr)):
            return max(arr)

        else:
            ele=arr[0]
            streak=0
            for i in range(1,n):
                if(ele>arr[i]):
                    streak+=1
                else:
                    ele=arr[i]
                    streak=1
                if(streak==k):
                    return ele
            return ele