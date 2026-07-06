class Solution:
    '''understand
    input: string w/ alpha numeric characters
    output: boolean
    edge cases: empty string ==> true, string w/ all duplicats ==> return true, 
    logic: one pointer at the begining of string(representing index) & one at end, if the they equal each other then continue, else then return False  
    '''
    def isPalindrome(self, s: str) -> bool:
       string = s.strip().lower()
       s=list(string)
       new_string = ["".join(i) for i in s if i.isalnum()]
       left = 0
       right = len(new_string)-1
       while left<right:
        if new_string[left] != new_string[right]:
            return False
        left+=1
        right -=1
       return True  
        
        