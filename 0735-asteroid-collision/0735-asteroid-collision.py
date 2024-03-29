class Solution(object):
    def asteroidCollision(self, asteroids):
        res = []
        for asteroid in asteroids:
            while len(res) and asteroid < 0 < res[-1]:
                if res[-1] == -asteroid:
                    res.pop()
                    break
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                elif res[-1] > -asteroid:
                    break
            else:
                res.append(asteroid)
        return res