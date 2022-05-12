class Solution:
    def replaceElements(self, arr):
        # arr[0] = max(arr[1:])
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr