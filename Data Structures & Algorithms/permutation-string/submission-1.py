class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r= 0,len(s1) # start with l, r as 0, len of s1
        hmap_s1 = {}
        for i in s1:
            if i in hmap_s1:
                hmap_s1[i]+=1
            else:
                hmap_s1[i] = 1
        hmap_s2 ={}
        # get the hmap counter for initial fixed window
        for i in s2[l:r]:
            if i in hmap_s2:
                hmap_s2[i]+=1
            else:
                hmap_s2[i] =1

        while r-l == len(s1) and r<len(s2):
            # now that we have equal lens hmap
        
            if hmap_s2 == hmap_s1:
                return True
            
            hmap_s2[s2[l]]-=1
            if hmap_s2[s2[l]]==0:
                del hmap_s2[s2[l]]
            
            #decrement the left element from hmap


            if s2[r] in hmap_s2:
                hmap_s2[s2[r]]+=1
            else:
                hmap_s2[s2[r]]=1
            print(hmap_s2, hmap_s1)
            # ruthlessly increment l, r as they are same window length now till we find the match
            l+=1
            r+=1

        return True if hmap_s2 == hmap_s1 else False
            
            



