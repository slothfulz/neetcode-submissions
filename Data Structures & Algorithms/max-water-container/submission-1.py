class Solution:
    '''
    understand
    input: int array, height represents height of ith bar
    output: integer
    logic: find the pair that maximizes area. where width is right index - left index, height is min of two heights. 
    find the area for every combo of numbers paired with one another 
    1. make a list variable
    2. establish a for range loop 
    3. establish for loop iterating over elements 
    4. take the area
    5. add it to list 
    6. return the largest area 
    
    '''
    def maxArea(self, heights: List[int]) -> int:
       left = 0
       right = len(heights) -1
       max_area= 0
       while left<right:
        width = right - left
        h = min(heights[left], heights[right])
        area = width * h
        if area>max_area:
            max_area = area
        if heights[left]< heights[right]:
            left +=1
        else:
            right -=1
       return max_area 



                
        

        