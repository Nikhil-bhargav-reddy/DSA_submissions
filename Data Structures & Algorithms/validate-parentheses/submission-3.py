class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(":")","{":"}", "[":"]"}
        stack = []

        for i in s:
            if i not in lookup:
                if stack:
                    val = stack.pop()

                    if lookup[val] != i:
                        return False
                else: # stack empty and we adding closed
                    return False
            
            else:
                stack.append(i)

        return not stack



