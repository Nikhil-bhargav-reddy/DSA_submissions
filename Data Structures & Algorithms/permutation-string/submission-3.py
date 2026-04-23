class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap_s1 = {}

        for i in s1:
            if i in hmap_s1:
                hmap_s1[i]+=1
            else:
                hmap_s1[i] = 1

        hmap_s2 = {}

        l,r= 0, len(s1)

        print(l,r)

        # wlak though s1: a:1, b:1, c:1
        # s2: e:1, i:1, d:1
        # at this point the len(s1) == r-l+1
        # check if both hashmaps are equal
        # if not, move left pointer and remove the left element from hashmap,
        # keep adding right pointer and its value
        # sliding window but of fixed length of s1
        # tickey part is how do we check the counts of first slide?
        # should we do it outside the loop?

        for i in s2[l:r]:
            if i in hmap_s2:
                hmap_s2[i]+=1
            else:
                hmap_s2[i] = 1
        print(hmap_s2)
            
        while r< len(s2):
            if hmap_s2 == hmap_s1:
                print('Its a permutation', hmap_s1, hmap_s2, '-----------breaking------')
                break
            else: # move the pointers
                print(l,r)
                hmap_s2[s2[l]]-=1
                # decrement by one if already has multiple vals

                # now check if the vals are zero and remove
                if hmap_s2[s2[l]] ==0:
                    del hmap_s2[s2[l]]
                    #use a function to remove
                print(hmap_s2, 'after del', l, r)


                if s2[r] in hmap_s2:
                    hmap_s2[s2[r]]+=1
                else:
                    hmap_s2[s2[r]] = 1

                l+=1
                r+=1
            
        return True if hmap_s1 == hmap_s2 else False



