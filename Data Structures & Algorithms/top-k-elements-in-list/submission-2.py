class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in nums]

        hmap = {}

        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i] = 1


        for key,v in hmap.items():
            print(hmap,bucket)
            bucket[v-1].append(key) # value is basically the frequency and we place its key in the bucket

        res = []

        for bkt in range(len(bucket)-1,-1,-1):
            if bucket[bkt]:
                for i in bucket[bkt]:
                    res.append(i)
                    if len(res) == k:
                        return res
