class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s:
            number = ""
            for i in range(len(s)):
                if i == 0:
                    try:
                        digit = int(s[i])
                        number += str(digit)
                    except ValueError:
                        if s[i] == "+" or s[i] == "-":
                            if len(s) == 1:
                                return 0
                            else:
                                number += s[i]
                        else:
                            return 0
                else:
                    if s[i] == "+" or s[i] == "-":
                        break
                    else:
                        try:
                            digit = int(s[i])
                            number += str(digit)
                        except ValueError:
                            break
            if number != "+" and number != "-":
                number = int(number)
                if number < -2**31:
                    return -2 ** 31
                elif number > (2**31) - 1:
                    return (2**31) - 1
                else:
                    return number
            else:
                return 0
        else:
            return 0
