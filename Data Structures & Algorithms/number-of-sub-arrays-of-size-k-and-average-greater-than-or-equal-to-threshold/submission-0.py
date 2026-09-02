class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        r_sum = 0

        for i in range(k):
            r_sum+=arr[i]
        
        if r_sum/k >= threshold:
            cnt = 1

        l,r = 0,k

        while r<len(arr):

            
            r_sum-=arr[l]
            r_sum+=arr[r]

            avg = r_sum/k

            if avg>=threshold:
                cnt+=1

            l+=1
            r+=1
        
        return cnt
