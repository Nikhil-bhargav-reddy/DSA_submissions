class MinStack:

    def __init__(self):
        self.stack =[]
        

    def push(self, val: int) -> None:
        if self.stack:
            min_val = min(val,self.stack[-1][1])
        else:
            min_val = val
        self.stack.append((val,min_val))
        return None

    def pop(self) -> None:
        self.stack.pop()
        return None
        

    def top(self) -> int:
        top_val = self.stack[-1]
        return top_val[0]        # can use stack.peek or pop? as well
        

    def getMin(self) -> int:
        return self.stack[-1][-1]



        
