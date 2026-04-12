class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # find a unique pattern for each of anagram
        # use a 26 letter string with counters 00001122110000 etc but how?
        hmap={}

        for i in range(len(strs)):
            str_base = [0]*26
            for j in  strs[i]:
                pos = ord(j)-ord('a') # ord(a) would get us starting pos of ascii small a value
                str_base[pos]+=1
            key = tuple(str_base) #making it hashable to be able to store as key

            if key in hmap:
                hmap[key].append(strs[i])
            else:
                hmap[key]= [strs[i]]

        res = []

        for i in hmap.values():
            res.append(i)
        return res
            


        

