def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif n > 9:
            while n > 9:
                digits = [int(digit) for digit in str(abs(n))]
                res = sum([i**2 for i in digits])
                n = res
                if res == 1 or res == 7:
                    return True
            return False
        else:
            return False