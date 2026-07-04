class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #take the lenght of the list
        #iterate through the list and put it in a variable step function
        #if the length of the list = legnth of the variable step func return false
        #otherwise return true

        nodupes = {}

        for num in nums:
            nodupes[num] = nodupes.get(num, 0) + 1

        for num in nodupes:
            if nodupes[num] > 1:
                return True
        return False

    