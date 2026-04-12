class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(":")","{":"}", "[":"]"}

        stack =[] #first in last out
        for i in s: 
            # we add to the stack ruthlessly if we see a open bracket
            if i in lookup.keys():
                stack.append(i)
            else: #if its a closed bracket, we pop from stack and compare
                if stack:
                    prev = stack.pop()
                else:
                    #if stack empty and current starts with closed, fail it
                    return False
                if lookup[prev] != i: # if last appeneded open bracket doesnt align with new closed, so its false
                    return False
        
        return False if stack else True


