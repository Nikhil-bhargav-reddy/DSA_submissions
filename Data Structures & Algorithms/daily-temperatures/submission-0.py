class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[] # index, tmp
        res= [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                # we found the hotter day, so we pop stack top
                stackIndex, stacktmp = stack.pop()
                res[stackIndex] = i - stackIndex  
                # we add current hotterdays index- the stack top day's index into, res.stacktopday value
            stack.append([i,t])
        return res


