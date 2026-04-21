class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # start time: 8:39PM
        # walking through [2,4,-4,-1]
        # conditions: 1) we add elements to the stack if they are +ve without any checks
        # 2) if it's a negative number, we check if stack's top is +ve, and do collision logic as below
        # 3) if i is the -ve number, if -(i) which is + is > stack top(if positive), we pop stack top, we keep doing it in while loop
        # 4) at the end we add -ve value to the stack if no popping left
        # 5) in case of a collison when equal, we pop stack and move to next element
        
        # walk through
        # we check if i(2) is not negative, then we add to stack regardless
        # we move pointer to right, i(4), we add to stack
        # i is -4 which is -ve, so we check if stack[-1] is +ve first, then 
        # while i > stack[-1]: then pop, if i == stack[-1], pop and continue, elif i<stack[-1], increment i

        res = []

        l=0
        while l<len(asteroids):

            if asteroids[l] >=0: # if positive we add to stack
                res.append(asteroids[l])
                l+=1
            else:
                #print(res,asteroids[l])
                if not res or res[-1] <0: # if stack top is negative or empty  
                    res.append(asteroids[l])    
                if res[-1] >=0: # if stack top is positive and incoming is -ve
                    while res and res[-1] >=0 and -asteroids[l] > res[-1]:
                        res.pop()
                    if not res or res[-1] <0:
                        res.append(asteroids[l])
                    
                    if res and res[-1] == -asteroids[l]: # when both equal we pop and skip to next l
                        res.pop()
                
                l+=1
        return res
                

            
