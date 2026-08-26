class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        # two pointers to loop over s,t


        i, j = 0,0

        while i < len(s) and j < len(t):

            if t[j] == s[i]:
                j+=1
            i+=1 # we keep moving on s untill we find a match again

        return len(t) - j



