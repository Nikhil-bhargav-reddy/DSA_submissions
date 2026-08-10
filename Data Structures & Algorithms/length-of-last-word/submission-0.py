class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        tmp = s.split(' ')

        for i in range(len(tmp)-1, -1, -1):
            print(tmp)
            if tmp[i] != '':
                return len(tmp[i])
        