import re

def isPalindrome(self, s: str) -> bool:
        replcedstr = re.sub('[^A-Za-z0-9]+', '', s).lower()
        return replcedstr[::-1] == replcedstr