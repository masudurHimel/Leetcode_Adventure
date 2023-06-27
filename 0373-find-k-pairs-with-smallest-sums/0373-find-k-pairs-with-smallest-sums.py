class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        N1 = len(nums1)
        N2 = len(nums2)
        H = [(nums1[0] + nums2[0], 0, 0, 1)]
        while H:
            for _ in range(len(H)):
                s, i, j, a = heappop(H)
                res += (nums1[i], nums2[j]),
                if len(res) >= k:
                    break
                if a and i + 1 < N1: #avoid dup
                    heappush(H, (nums1[i+1] + nums2[j], i+1, j, 1))
                if j + 1 < N2:
                    heappush(H, (nums1[i] + nums2[j+1], i, j+1, 0))
            if len(res) >= k:
                break
        return res