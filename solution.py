class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s_nums = [char for char in s if char.isdigit()]
        if not s_nums:
            return 0
        else:
            number = ""
            for i in range(len(s)):
                if i == 0:
                    if s[i].isdigit() or s[i] == "+" or s[i] == "-":
                        number += s[i]
                    else:
                        return 0
                else:
                    if s[i].isdigit():
                        number += s[i]
                    elif s[i] == "+" or s[i] == "-":
                        break
                    else:
                        break      
            if number == "+" or number == "-":
                return 0
            else:
                if int(number) < -2**31:
                    return -2 ** 31
                elif int(number) > (2**31) - 1:
                    return (2**31) - 1
                else:
                    return int(number)
