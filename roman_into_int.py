def romanToInt(self, s: str) -> int:
       roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
       num = 0
       temp = 0

       for char in reversed(s):
            if char in roman_dict:
                val = roman_dict[char]
                if temp > val:
                    num -= val
                else:
                    num += val
                temp = val
       return num