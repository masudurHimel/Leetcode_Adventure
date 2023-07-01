class Solution:
    def distributeCookies(self, cookies, k: int) -> int:

        n = len(cookies)

        if n == k:
            return max(cookies)

        cks = [0] * k

        max_ = {
            'answer': 10 ** 9
        }

        def solve(i, n, k, cks):
            if max(cks) >= max_['answer']:
                return
            if i == n:
                max_['answer'] = min(max_['answer'], max(cks))
                return
            for child in range(k):
                cks[child] += cookies[i]
                solve(i + 1, n, k, cks)
                cks[child] -= cookies[i]
            
        solve(0, n, k, cks)

        return max_['answer']