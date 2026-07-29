class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l = 0
        r = k-1
        counter = 0

        while r<len(blocks):
            temp_c = 0
            for i in blocks[l:r+1]:
                if i =='B':
                    temp_c+=1
            
            counter = max(counter,temp_c)
            l+=1
            r+=1
        
        return k-counter
