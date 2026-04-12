class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        def operator(op,a,b):
            if op == '/':
                return int(a/b)
            if op =="*":
                return a*b
            if op == '-':
                return a-b
            if op=='+':
                return a+b
        if len(tokens) ==1:
            return int(tokens[-1])
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                prev = stack.pop()
                prev2= stack.pop() 
                # popping twice as we saw a non integer or a operator basically
                # we can even have a set of these 4 for o(!) lookup if needed but lets leave for now
                print(prev2,prev)
                print(stack,i)
                tmp_res = operator(i,prev2,prev)
                # after getting current operators ouput, we put it back result to stack

                stack.append(tmp_res)
        return int(tmp_res)
