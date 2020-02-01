class Solution:
    def myAtoi(self, s: str) -> int:
        
        # If s has no numbers, return 0
        s_nums = [char for char in s if char.isdigit()]
        if not s_nums:
            return 0
        
        # If s has numbers:
        else:
            
            # Remove Leading/Trailing whitespaces from s:
            s = s.strip()
            
            # Create Variable "number" that will later be converted to int.
            number = ""
            
            # Loop over chars in s. Find the valid ones and add them to "number":
            for i in range(len(s)):
                
                # If char is a number, add to "number":
                if s[i].isdigit():
                    number += s[i]
                    
                # If char isn't a number:
                else:
                    
                    # If it's the first char:
                    if i == 0:
                        
                        # If it's a plus or minus, add to "number":
                        if s[i] == "+" or s[i] == "-":
                            number += s[i]
                        else:
                            return 0
                        
                    # If it's not the first char:
                    else:
                        break  
            
            # If number only has a plus or minus sign, return 0
            if number == "+" or number == "-":
                return 0
            
            # Else, compare and return correct value according to requirements:
            else:
                if int(number) < -2**31:
                    return -2 ** 31
                elif int(number) > (2**31) - 1:
                    return (2**31) - 1
                else:
                    return int(number)
