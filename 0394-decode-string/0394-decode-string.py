class Solution:
    def decodeString(self, s):
        stack = []
        res = ""
        for i in s:
            if i == "]":
                target = ""
                count = 0
                prev = False
                dig = ''
                while stack:
                    temp = stack.pop()
                    if temp.isdigit():
                        dig = temp + dig
                        if not stack or not stack[-1].isdigit():
                            break
                        continue
                    if temp != "[":
                        target = temp + target
                stack.append(int(dig) * target)
            else:
                stack.append(i)
        return ''.join(stack)