class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap_s1 = {}

        for i in s1:
            if i in hmap_s1:
                hmap_s1[i]+=1
            else:
                hmap_s1[i] = 1

        hmap_s2 = {}

        l,r= 0, 0

        # wlak though s1: a:1, b:1, c:1
        # s2: e:1, i:1, d:1
        # at this point the len(s1) == r-l+1
        # check if both hashmaps are equal
        # if not, move left pointer and remove the left element from hashmap,
        # keep adding right pointer and its value
        # sliding window but of fixed length of s1
        # tickey part is how do we check the counts of first slide?
        # should we do it outside the loop?

        while r< len(s2):

            while r-l < len(s1):
                if s2[r] in hmap_s2:
                    hmap_s2[s2[r]]+=1
                else:
                    hmap_s2[s2[r]] = 1
                r+=1
            print(hmap_s1, hmap_s2)
            
            # above while loop handles initial condition of adding to inital hmap
            # l is still at 0 here if you see, which can help us next

            # now that the elements are added to hashmap and r-l+1 == len(s1)

            # we can compare, here its a:1,b:1,c:1 vs e:1,i:1,d:1 

            if hmap_s2 == hmap_s1:
                return True
            else: # move the pointers
                hmap_s2[s2[l]]-=1
                # decrement by one if already has multiple vals

                # now check if the vals are zero and remove
                if hmap_s2[s2[l]] ==0:
                    del hmap_s2[s2[l]]
                    #use a function to remove

                if s2[r] in hmap_s2:
                    hmap_s2[s2[r]]+=1
                else:
                    hmap_s2[s2[r]] = 1
                
                # now incrmeent left and right
            l+=1
            r+=1
        return False
            
            



