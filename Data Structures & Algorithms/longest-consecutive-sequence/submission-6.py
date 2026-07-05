class Solution:
    '''
    understand:
    input: integer array
    ouput: integer
    edge cases: empty list ==> 0, duplicates ==> would not be added to consecutive list.. return len 1,
    logic: sort the orginal list in asscending order, index i, index i +1 is greater than the last by 1 if is add to count variable if isn't move on with the loop,the loop stops when you finish going through the list

    plan:
    1. count variable = 0
    2. sort the original list in ascending roder
    3. loop through sorted list pointer: i condition is range(0, len(nums))
    4. if nums[i] + 1 == nums[i+1]:
    5. count +=1
    6. countinue
    7. return the count variable     '''
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n-1 not in numSet:
                length = 0
                while n+length in numSet:
                    length += 1
                if length>longest:
                    longest = length
        return longest
    #     count = 1
    #     nums.sort()
    #     if len(nums) == 0:
    #         return 0
    #     for num in range(0, len(nums)):
    #         if num+1 in range(0,len(nums)):
    #             if nums[num] + 1 == nums[num+1]:
    #                 count +=1
    #             else:
    #                 count = 1
    #     return count

    

        