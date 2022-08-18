class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res_map = Counter(arr)
        sorted_res = sorted(res_map.values(), reverse=True)
        target_len = len(arr)//2
        ans = 0
        print(sorted_res)
        while target_len > 0:
            target_len -= sorted_res[ans]
            ans += 1
            
        return ans
    