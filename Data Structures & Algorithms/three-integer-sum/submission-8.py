class Solution:
    '''
    understand
    input: list
    output: list of sublists
    logic: two poitner it. if hi and low + currnet == 0 then add elements to list if not then hi + 1 low -1 while low< hi.
    edge cases: if first elemeents are positive when sorted to ascending then break if first ements are negative when sorted descending break, duplicates, skip duplciates by continuing  
    plan 
    1. for loop in range (0,n)
    2. sort list in ascending or in descending order and evaluate edge cases
    3. left, right = i+1, len(n) - 1
    4. in ascending order evaluate problem
    5. if left + right + current == 0: add to sublist
    6. elif left + right + current > 0: move right pointer and do operation again
    7. elif left + right + curren < 0: move left pointer and do operation again
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tri = []
        l = len(nums)

        for i in range(l - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, l - 1

            while left < right:
                sumski = nums[i] + nums[left] + nums[right]
                if sumski == 0:
                    tri.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sumski < 0:
                    left += 1
                else:
                    right -= 1
        return tri
    
        
        # l = len(nums)
        # tri = []
        # nums.sort(reverse = False)
        # if l>0 and nums[0] > 0: 
        #     return tri
        # if nums[-1]<0:
        #     return tri

        # for i in range(0,l-2):
        #     left,right = i+1,l-1
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue
        #     while left<right:
        #         sumski = nums[i] + nums[left] + nums[right]
        #         if sumski == 0:
        #             tri.append([nums[i],nums[left],nums[right]]) 
        #             left +=1
        #             right -=1
        #             while left<right and nums[left] == nums[left-1]:
        #                 left +=1
        #             while left<right and nums[right] == nums[right-1]:
        #                 right -=1 
        #         elif sumski<0:
        #             left +=1
        #         elif sumski>0:
        #             right -= 1
                
        # return tri
                 



            
            


        