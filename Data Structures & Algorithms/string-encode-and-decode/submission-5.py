''' 
understand: 
goal ==> encode a list of strings that outputs a string and decode that string into original list
edges
duplicate list ==> output duplicate list
empty list ==> output empty list
plan:
encode ==> apply delimiter and number in front of list characters 
decode ==> 
identify delimeter + len of word, slicing string from [index of delimiter: len of word + 1]
countinue that loop until there is no delimeter + len of word 
for i in s:
j +=1
if i == "?":
       len = s[j-1] +1 
      list.append( s[j: len])



'''


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
                lenword=str(len(i))
                encoded_string += lenword + "?" + i
        return encoded_string


    def decode(self, s: str) -> List[str]:
        j = 0
        decoded_strs = []
        while j< len(s):
                k=j
                while s[k] != "?":
                        k +=1
                lenofword = int(s[j:k]) 
                startword = k+1
                endofword = startword + lenofword
                decoded_strs.append(s[startword:endofword])
                j= endofword 

        return decoded_strs
