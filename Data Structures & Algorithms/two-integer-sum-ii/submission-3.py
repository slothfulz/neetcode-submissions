class Solution:
    '''
    understand: 
    input: array of integers NEVER in decreasing order
    ouput: two indices where index one has to be greater than index 2
    edge cases: index1 != index2, solution must be o(1), 1-indexed
    logic: two elements need to add up to each other   
    plan (brute force):
    1. create two pointers
    2. take the length of array
    3. if sum is two big, move right pointer -=1, if it is too small, move left pointer +1
    4. w
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0
        right = len(numbers)-1
        sumidx = []
        for num in numbers:
           if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
           elif numbers[left] + numbers[right] > target:
            right -=1
           elif numbers[left] + numbers[right]< target:
            left +=1



        