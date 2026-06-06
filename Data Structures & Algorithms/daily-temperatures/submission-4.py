class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we can use stack
        # lets add todays temp to stack
        # check if tomorrows temp is > if yes, we foudn warmer day, so we pop element from stack and add difference between indexes into res
        # res could be [0]*len(temp)
        # we should somehow add indexes to stack, wait we can add a tuple to stack right, or even a list
        # lets do (index, value)
        stack = []

        res = [0]*len(temperatures)

        for index,val in enumerate(temperatures):
            print(index,val)
            while stack and val > stack[-1][1] : # if stack has values and warmer incoming, we update res as we found warmer day
                prev_index, pev_val = stack.pop()
                res[prev_index] = index - prev_index # index value at stack top's element in res gets assigned the value of index of warmer day - stack tops index = num of days

            # else we just append to stack 

            stack.append((index,val))
        return res