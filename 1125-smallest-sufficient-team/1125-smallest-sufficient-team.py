class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        convert = {key:idx for idx, key in enumerate(req_skills)}

        n, m = len(req_skills), len(people)
        end_mask = 2 ** n - 1
        visit = set()

        for idx, i in enumerate(people):
            temp = 0
            for j in range(len(i)):
                temp += (1 << convert[i[j]])
            people[idx] = temp
        
        q = [(0, [])]
        while q:
            mask, arr = q.pop()
            if mask == end_mask:
                return arr
            for idx, skill in enumerate(people):
                new_mask = mask | skill
                if new_mask not in visit:
                    visit.add(new_mask)
                    q.insert(0, (new_mask, arr + [idx]))