class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def form_pairs(max_allow):
            pairs = 0
            num = 0
            while num + 1 < N:
                if nums[num + 1] - nums[num] <= max_allow:
                    pairs += 1
                    num += 1
                num += 1
            return pairs >= p

        N = len(nums)
        nums.sort()
        left,right = 0, (nums[-1]- nums[0])

        while left<right:
            mid = left+(right-left)//2
            if form_pairs(mid):
                right = mid
            else:
                left = mid + 1
        return left