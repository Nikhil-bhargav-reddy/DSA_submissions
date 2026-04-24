class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we can use stack
        # lets add todays temp to stack
        # check if tomorrows temp is > if yes, we foudn warmer day, so we pop element from stack and add difference between indexes into res
        # res could be [0]*len(temp)
        # we should somehow add indexes to stack, wait we can add a tuple to stack right, or even a list
        # lets do (index, value)
        res = [0]*len(temperatures)

        stack =[]

        for i,val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                prev_i,temp = stack.pop()
                res[prev_i] = i-prev_i

            stack.append((i,val))
        return res