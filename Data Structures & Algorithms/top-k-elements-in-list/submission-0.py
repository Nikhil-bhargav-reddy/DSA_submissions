class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # could use a hashmap but how
        # one hashmap to count occurances
        # hashmap with counters as keys [0-n) n is the length of nums at max

        counter= {}
        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i] = 1
        
        key_counter =[]
        for i in range(len(nums)+1):
            key_counter.append([])
        #print(key_counter)
        
        for key,value in counter.items():
            key_counter[value].append(key)
        #print(key_counter)
        res= []
        for i in range(len(key_counter)-1,0,-1):
            for num in key_counter[i]:
                res.append(num)
                if len(res)==k:
                    return res
