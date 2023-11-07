class Solution:
    def eliminateMaximum(self, dist, speed):
        ans = [dist[i]/speed[i] for i in range(len(dist))]

        ans.sort()

        count, cur_time = 0, 0

        for i in ans:
            if cur_time < i:
                count += 1
                cur_time += 1
            else:
                break

        return count