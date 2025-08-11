from collections import Counter

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = Counter(ransomNote)
        y = Counter(magazine)

        if (x - y) == {}:
            return True
        else:
            return False