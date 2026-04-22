class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = {
            #index : [word, drow],
        }

        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s not in anagram:
                anagram[sort_s] = []
            anagram[sort_s].append(s)
        
        result = []
        for x in anagram.values():
            result.append(x)
        
        return result




        



        
                

        
                
                


        