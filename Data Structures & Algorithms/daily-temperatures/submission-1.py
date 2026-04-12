class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i,v in enumerate(temperatures):
            while stack and v > stack[-1][-1]: # if stack isnt empty and stack's last value is < incoming temp
                prev_pos, prev_temp =  stack.pop()

                res[prev_pos] = i-prev_pos
            
            stack.append((i,v))
        return res