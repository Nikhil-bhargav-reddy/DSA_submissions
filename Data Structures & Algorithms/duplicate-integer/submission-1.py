class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash_set={}

        for i in nums:
            if i in hash_set:
                return True
            else:
                hash_set[i]=1
        return False