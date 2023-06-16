class Solution:
	def numOfWays(self, nums: List[int]) -> int:

		def DFS(current_array):

			length = len(current_array)

			if length <= 2:
				return 1

			left_nodes , right_nodes = [] , []

			root_element = current_array[0]

			for num in current_array[1:]:

				if num < root_element:
					left_nodes.append(num)
				else:
					right_nodes.append(num) 

			return DFS(left_nodes) * DFS(right_nodes) * math.comb(length - 1, len(left_nodes)) 

		return (DFS(nums) - 1) % (1000000007)