class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= {}
        res = []
        for num in nums:
            freq[num] = freq.get(num,0) +1
            sortedL = sorted(freq, key= lambda x: freq[x], reverse= True)
        for i in range(0,k):
            res.append(sortedL[i])
        return res
        ''' 
        abt problem:
        list with integers
         return k most present element

        edge cases 
        empty list --> return [""]

        solution 
         1. iterate through list and count frequency of numbs and put in hashmap
        2. list(dict.keys) and list(dict.values).max 
        3. 



     
        '''
    
    


