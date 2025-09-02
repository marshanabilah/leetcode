def isSubsequence(self, s: str, t: str) -> bool:
        if s and not t:
            return False
        if not s:
            return True
        
        arr, sym, subarr, subsym = t[1:], t[0], s[1:], s[0]
        if sym == subsym:
            return self.isSubsequence(subarr, arr)
        else:
            return self.isSubsequence(s, arr)