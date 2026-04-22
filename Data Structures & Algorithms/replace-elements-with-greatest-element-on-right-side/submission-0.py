class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new = []
        for x in range(1,len(arr)):
            new.append(max(arr[x:])) 
        new.append(-1)
        return new

       