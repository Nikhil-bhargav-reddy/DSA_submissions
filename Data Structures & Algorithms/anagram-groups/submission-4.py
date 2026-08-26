class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        unq = [0]*26

        tmp = []
        for string in strs:
            for char in string:
                pos = ord(char) - ord('a')
                unq[pos]+=1
            tmp.append(tuple(unq))

            unq = [0]*26
        
        # print(tmp)

        hmap = {}

        for i in range(len(tmp)):
            if tmp[i] in hmap:
                hmap[tmp[i]].append(strs[i])
            else:
                hmap[tmp[i]] = [strs[i]]
        
        # print(hmap)
        res = []
        for i in hmap.values():

            res.append(i)

        return res

            
            



        

