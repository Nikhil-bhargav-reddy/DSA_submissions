class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap={}

        if len(s)!=len(t):
            return False
        for i in s:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i] = 1
        
        for j in t:
            if j in hmap and hmap[j]>0:
                hmap[j]-=1
            else:
                #print(j, hmap)
                return False
        return True