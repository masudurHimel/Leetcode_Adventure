class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        modulo = 10**9 + 7
        result = 0
        num_count = Counter()

        for number in nums:
            reversed_num = int(str(number)[::-1])
            diff = number - reversed_num
            result += num_count[diff]
            num_count[diff] += 1

        return result % modulo
