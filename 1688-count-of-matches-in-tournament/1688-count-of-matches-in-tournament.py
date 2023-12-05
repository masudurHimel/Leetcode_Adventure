class Solution:
    def numberOfMatches(self, n: int) -> int:
        curr_teams, matches = n, 0
        while curr_teams > 1:
            if curr_teams % 2 != 0:
                matches += 1
                curr_teams -= 1
            if curr_teams % 2 == 0:
                matches += curr_teams // 2
                curr_teams = curr_teams // 2
        return matches