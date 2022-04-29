class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = list((''.join(char for char in s if char.isalnum())).lower())
        length = len(new_string)
     
        for i in range(0, length//2):
            if new_string[i] != new_string[length -1 - i]:
                return False
        return True