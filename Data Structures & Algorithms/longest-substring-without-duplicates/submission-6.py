class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hash_set= set()
        l,r =0,0
        longest = 0
        while l<=r and r<len(s):
            print(hash_set)
            while s[r] in hash_set:
                print(hash_set, s[r], r)
                hash_set.remove(s[l])
                l+=1
            hash_set.add(s[r])
            longest = max(longest, len(hash_set))
            r+=1
        return longest


        
           



        
