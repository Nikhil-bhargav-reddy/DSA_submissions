class Solution:
    def isValid(self, s: str) -> bool:

        lookup = {
            '}':'{',
            "]":"[",
            ")":'('
        }
# if we see a open bracket, we add it to a stack
# if we see a closed bracket, we pop from stack and compare
        stack = []
        for i in s:
            if stack and i in lookup:
                val = stack.pop()
                if val != lookup[i]:
                    return False
            else:
                stack.append(i)
        return not stack



        # alternative approach of keys and vals reverse
        # lookup = {"(":")","{":"}", "[":"]"}

        # stack = []

        # for i in s:
        #     if i not in lookup: # if it's closed bracket
        #         if stack:
        #             val = stack.pop()
        #             if lookup[val] != i:
        #                 return False
        #         else: # stack empty and we adding closed so false
        #             return False
            
        #     else: # open brackets
        #         stack.append(i)

        # return not stack
        






