class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        pushed = deque(pushed)
        popped = deque(popped)
        res = [pushed.popleft()]
        temp = popped.popleft()
        while popped:
            if res and temp == res[-1]:
                temp = popped.popleft()
                res.pop()
            else:
                if len(pushed) == 0:
                    return False
                res.append(pushed.popleft())
        if len(popped):
            return False
        return True