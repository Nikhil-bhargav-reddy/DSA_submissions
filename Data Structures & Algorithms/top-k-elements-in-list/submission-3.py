class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # could use a hashmap but how
        # one hashmap to count occurances
        # hashmap with counters as keys [0-n) n is the length of nums at max

        # we move the elements into specific buckets of their own based on frequency
        # max frequency would be length of nums, so bucket max size = len

        bucket = [[] for i in nums]

        hmap = {}

        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i] = 1


        for key,v in hmap.items():
            bucket[v-1].append(key) # value is basically the frequency and we place its key in the bucket
            # we do v-1 to match the 0 indexed bucket we created, or alt would be to create bucket as 1 indexed, from 1 to n+1

        res = []

        for bkt in range(len(bucket)-1,-1,-1):
            if bucket[bkt]:
                print(bucket[bkt])
                for i in bucket[bkt]:
                    res.append(i)
                    if len(res) == k:
                        return res
