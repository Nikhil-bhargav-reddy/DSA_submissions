class Solution:

    def encode(self, strs: List[str]) -> str:
        str= '#'.join(strs)
        print(str)
        return str

    def decode(self, s: str) -> List[str]:
        return s.split('#')
