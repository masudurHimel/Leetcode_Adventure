class Solution(object):
    def isPathCrossing(self, path):
        x, y = 0, 0
        pos = {(0, 0)}
        for move in path:
            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            elif move == 'W':
                x -= 1
            if (x, y) in pos:
                return True
            pos.add((x, y))
        return False
