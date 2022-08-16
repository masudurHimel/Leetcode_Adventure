class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_map = {}
        reject_map = {}
        for i, v in enumerate(s):
            if reject_map.get(v):
                continue
            if v in s_map:
                s_map.pop(v)
                reject_map[v] = True
            else:
                s_map[v] = i
        print(s_map)
        return min(s_map.values()) if s_map else -1  