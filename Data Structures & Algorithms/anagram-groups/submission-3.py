class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # find a unique pattern for each of anagram
        # use a 26 letter string with counters 00001122110000 etc but how?
        hmap={}

        for i in strs:
            unique_key = [0]*26
            for j in i:
                pos = ord(j)- ord('a')
                unique_key[pos]+=1
            uk = tuple(unique_key)
            if uk in hmap:
                hmap[uk].append(i)
            else:
                hmap[uk] = [i]
        res = [i for i in hmap.values()]

        return res
            


        

