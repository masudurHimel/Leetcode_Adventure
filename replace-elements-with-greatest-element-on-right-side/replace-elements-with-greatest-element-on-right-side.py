class Solution:
    def replaceElements(self, arr):
        try:
            if len(arr) == 1:
                return [-1]
            i = 0
            tmp_l = -9999
            while True:
                max_arr = max(arr[i+1:])
                if arr.count(max_arr) > 1:
                    tmp_ind = arr.index(max_arr)
                    arr[tmp_ind] = -1
                    continue
                max_ind = arr.index(max_arr)
                arr[i] = max_arr
                arr[i+1:max_ind+1] = [-1] * (max_ind - i)
                i = max_ind
        except Exception:
            tmp = arr[0]
            for i, v in enumerate(arr[1:len(arr)-1]):
                if v == -1:
                    arr[i+1] = tmp
                else:
                    tmp = v
            return arr