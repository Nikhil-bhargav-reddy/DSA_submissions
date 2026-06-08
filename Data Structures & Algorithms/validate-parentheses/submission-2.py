class Solution:
    def isValid(self, s: str) -> bool:
        # lookup = {"(":")","{":"}", "[":"]"}

        # stack =[] #first in last out
        # for i in s: 
        #     # we add to the stack ruthlessly if we see a open bracket
        #     if i in lookup.keys():
        #         stack.append(i)
        #     else: #if its a closed bracket, we pop from stack and compare
        #         if stack:
        #             prev = stack.pop()
        #         else:
        #             #if stack empty and current starts with closed, fail it
        #             return False
        #         if lookup[prev] != i: # if last appeneded open bracket doesnt align with new closed, so its false
        #             return False
        
        # return False if stack else True


        lookup = {
            '}':'{',
            "]":"[",
            ")":'('
        }

# Open brackets must be closed by the same type of brackets.

# Open brackets must be closed in the correct order.  

# Every close bracket has a corresponding open bracket of the same type

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
        






