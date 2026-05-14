class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # we need to look into a few things here
        # if the incoming number is +ve we simply append
        # if its -ve , there can be multiple possibilities 
        #1) if abs of current -ve value is > stack top: we pop from stack top and continue 
        # 2) if abs of current -ve is equal to stack top: we pop from stack and break the loop
        # 3) if in any case the current value abs is smaller than stack top, we break the while
         # in all these steps, if we think about it, the second and third case when the asteroid is either equal means blast or if the stack top is bigger guy, we simply set a flag so that our final stack.append doesnt include these to be added to the stack

        for i in asteroids:
            # all in all we use three checks, one while loop to keep popping, the remainign conditions within are used for simple if else type
            should_add = True
            while stack and stack[-1]>0 and i<0:
                # collision happens only when stack top is +ve and incoming is -ve
                if stack[-1] < abs(i):
                    stack.pop()
                    continue
                elif stack[-1] == abs(i):
                    stack.pop()
                    should_add = False # the incoming i is being skipped as it met a equal sized guy
                    break # break while loop
                else: # if stack top is greater than incoming value, we simply break out of loop
                    should_add = False # the incoming i is being skipped here too as it met a bigger guy on stack top, so this i is killed
                    break
            if should_add:
                stack.append(i) # if we don't use a flag we would end up adding the equal sized guy who got destoryed and smaller guy from else
        return stack