class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        unq = [0]*26
        hmap = {}

        # tmp = []
        for string in strs:
            for char in string:
                pos = ord(char) - ord('a')
                unq[pos]+=1
            # tmp.append(tuple(unq))
            key = tuple(unq)
            if key in hmap:
                hmap[key].append(string)
            else:
                hmap[key] = [string]
            unq = [0]*26
        
        # print(tmp)

        # hmap = {}

        # for i in range(len(tmp)):
        #     if tmp[i] in hmap:
        #         hmap[tmp[i]].append(strs[i])
        #     else:
        #         hmap[tmp[i]] = [strs[i]]
        
        # print(hmap)
        res = []
        for i in hmap.values():

            res.append(i)

        return res

        # time 
        # o(n*m) n is length of strs and m is length of each element, or can simply be length or all characters in array strs
        # one o(n) for hmap, one o(n) during res
        # space
        # o(n) *o(1)26 characters one

            
            



        

