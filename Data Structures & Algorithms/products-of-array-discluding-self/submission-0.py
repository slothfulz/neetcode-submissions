'''
understand --> integer array, at each position find the product of the elements before it and after it and append that product to a list
- keep track of the other numbers while being one number 
- exclude that number
edge cases:
empty list [] => empty list
duplicates => output would also be duplicates 

match ==> an array problem 
plan==> 
pointer =0 #poistion we are on/i
right pointer =0
left pointer =len(list)
prod = 1
listski = []
while pointer<len(nums):
        at index 0 finding all poistions pointer =+1<less than length (if)
                while rightpointer<len(nums):
                        rightponter +=1
                        prod* nums[right]
                listski.append(prod)
                pointer +=1   
        at index 3 finding all positions -= less than length-1  (if)
        while leftpointer> pointer:
                        leftpointer -=1
                        prod* nums[left]
                listski.append(prod) 
        index in between  has positions to the right and left of it (alogirthim)
        while pointer>len
        rightpointer= pointer
        left pointer>pointer
        prod = prod * nums[rightpointer+1] * nums[leftpointer -1] 
        pointer +=1 

        pointer =1 nums[pointer -1]* nums [pointer+1] * nums[pointer + 2]
        pointer =2 nums[pointer-2] * nums[pointer-1] * nums[pointer+1] *nums[pointer+1]
        left = 

''' 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre = 1
        post = 1
        for i in range(n):
                res[i] = pre
                pre *= nums[i]
        for i in range(n-1, -1, -1):
                res[i] *=  post
                post *= nums[i]
        return res


        
        