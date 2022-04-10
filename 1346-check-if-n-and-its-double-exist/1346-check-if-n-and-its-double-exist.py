class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr = [abs(i*999) if i<0 else i  for i in arr]
        arr = sorted(arr)
        print(arr)
        for i, v in enumerate(arr):
            if v*2 in arr[i+1:]:
                return True
        return False