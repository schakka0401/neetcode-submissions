class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)
        if a == b and len(a) == len(b):
            return True
        else:
            return False