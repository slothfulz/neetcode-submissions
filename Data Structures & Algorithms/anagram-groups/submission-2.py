class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List]:
        # sort every string 
        #anagrams added to key list value
        res= defaultdict(list)
        for s in strs:
            sortedS= ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

    
    
        