class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l<r:
            # we first need to run a small while loops till we find a alnum for both pointers
            # this would not cause time complexity increase, because our while loops just skip non alnums just once, no repetition
        
            while l<r and not s[l].isalnum():
                # this is still 0(n) because we are just moveing left pointer to a proper alnum
                l+=1
            while l<r and not s[r].isalnum():
                # moveing right pointer to stop at alnum character
                r-=1
            # once we meet two alnums at l,r, we simply compare
            if s[l].lower()==s[r].lower(): #case insensitive condition
                l+=1
                r-=1
            else:
                return False

        return True