class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l = 0
        r = k
        counter = 0

        for i in blocks[l:r]:
            if i =='B':
                counter+=1

        temp_c = counter
        while r<len(blocks):
            if blocks[l] == 'B':
                temp_c-=1
            if blocks[r] == 'B':
                temp_c+=1
            
            counter = max(counter, temp_c)
            l+=1
            r+=1
            
        
        return k-counter
