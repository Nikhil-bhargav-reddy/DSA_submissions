class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]

        # def decode(n,s):
        #     return n*s

        for i in s:
            if i == ']':
                # pop alphabets untill we find integers
                # small function should do
                tmp = ''
                val = None
                while not val:
                    popped = stack.pop()
                    if popped.isdigit():
                        val = popped
                    elif popped == '[':
                        continue
                    else:
                        tmp = popped+tmp
                
                tmp = tmp*int(val)

                stack.append(tmp)
            elif stack and i.isdigit() and stack[-1].isdigit():
                stack[-1]+=i
                print(stack[-1])
            else:
                stack.append(i)
        
        res = ''

        for i in stack:
            res+=i
        
        return res