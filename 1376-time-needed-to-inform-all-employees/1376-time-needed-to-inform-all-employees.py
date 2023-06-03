class Solution:
	def numOfMinutes(self, n, headID, manager, informTime):
		sub = {i: [] for i in range(n)}
		for i, v in enumerate(manager):
			if v != -1:
				sub[v].append(i)
				
		def dfs(node, time):
			time += informTime[node]
			_max = 0
			if len(sub[node]) > 0:
				for _, v in enumerate(sub[node]):
					cur = dfs(v, time)
					_max = max(_max, cur)
				return _max
			return time
		return dfs(headID, 0)