class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #return the indices of two numbers that add up to a target number
        #subtract an element from target. try to see if difference is in the list
        #enumerate func to return index

        seen = {}
        for index, element in enumerate(nums):
            diff = target - element
            if diff in seen:
                return [seen[diff], index]
            seen[element] = index
