class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(set)
        for i,x in enumerate(arr):
            d[x].add(i)
            
        steps = {i:-1 for i in range(len(arr))}
        steps[0] = 0
        q = deque([0])
        level = 0
        while q:
            for _ in range(len(q)):
                t = q.popleft()
                if t == len(arr)-1:
                    return steps[t]
                if steps[t] < level:
                    continue
                for next_id in [t-1, t+1, *d[arr[t]]]:
                    if next_id>=0 and next_id<len(arr) and steps[next_id] == -1:
                        steps[next_id] = 1 + steps[t]
                        q.append(next_id)
                d[arr[t]] = []
            level+=1