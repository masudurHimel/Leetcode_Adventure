class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        cnt = list(dict(sorted(cnt.items(), key=lambda x: x[1], reverse=True)).keys())
        return cnt[:k]