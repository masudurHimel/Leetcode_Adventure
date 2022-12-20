class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        res = deque([0])
        visited = set()
        while len(res) > 0:
            v = res.popleft()
            if v not in visited:
                res += rooms[v]
            visited.add(v)

        return len(visited) == len(rooms)