class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        
        i = 1
        while i < len(s):
            if stack and stack[-1] == s[i]:
                _ = stack.pop()
            else:
                stack.append(s[i])
            i += 1
            
        return ''.join(stack)