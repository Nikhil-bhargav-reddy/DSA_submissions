class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # find a unique pattern for each of anagram
        # use a 26 letter string with counters 00001122110000 etc but how?
        

        map = []

        hmap={}

        for i in strs:
            unique_key = [0]*26
            for j in i:
                
                pos = ord(j)- ord('a')
                
                unique_key[pos]+=1
            map.append(tuple(unique_key))

        for i in range(len(map)):
            if map[i] in hmap:
                hmap[map[i]].append(strs[i])
            else:
                hmap[map[i]] = [strs[i]]

        print(hmap)

        res = [i for i in hmap.values()]

        return res
            


        

