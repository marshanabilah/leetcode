def lengthOfLastWord(self, s: str) -> int:
    s_trimmed = s.strip()
    len = 0

    for char in reversed(s_trimmed):
        if char == " ":
            break
        len += 1
        
    return len