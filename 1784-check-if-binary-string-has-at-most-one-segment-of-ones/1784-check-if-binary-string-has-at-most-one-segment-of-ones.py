class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        first_one = True

        for digit in s:
            if digit == "1":
                if not first_one:
                    return False
            if digit == "0":
                first_one = False

        return True