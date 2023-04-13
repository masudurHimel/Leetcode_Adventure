class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = [pushed[0]]
        i = 0
        j = 1
        while i < len(popped):
            if len(stack) > 0 and stack[-1] == popped[i]:
                stack.pop(-1)
                i += 1
            elif j >= len(pushed):
                break
            else:
                stack.append(pushed[j])
                j += 1
        if len(popped) == i:
            return True
        return False