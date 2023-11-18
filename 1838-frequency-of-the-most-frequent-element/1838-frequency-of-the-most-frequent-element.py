class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
      nums.sort()

      start, end = 0, 0
      amount = 0

      maxSize = 1

      for newEnd in nums[1:]:
        oldEnd = nums[end]
        oldSize = (end-start) + 1

        newAmount = amount + ((newEnd - oldEnd) * oldSize)

        while newAmount > k and start < len(nums):
          newAmount -= (newEnd - nums[start])
          start += 1

        end += 1
        amount = newAmount

        maxSize = max(maxSize, ((end-start)+1))

      print(maxSize)
      return maxSize