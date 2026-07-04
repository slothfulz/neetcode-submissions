class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
          seen.add(i)
        if len(seen) == len(nums) : 
          return False
        return True
          
            
            

        #take the lenght of the list
        #iterate through the list and put it in a variable step function
        #if the length of the list = legnth of the variable step func return false
        #otherwise return true

        #nodupes = {}
      #  for num in nums:
          #  nodupes[num] = nodupes.get(num, 0) + 1
        
        #for i in nodupes:
          #  if nodupes[i] > 1:
          #      return True
       # return False



    