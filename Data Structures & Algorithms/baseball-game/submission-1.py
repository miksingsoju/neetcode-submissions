class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for x in range(len(operations)):
            if operations[x].strip("-").isdigit():
                scores.append(int(operations[x]))
            elif operations[x] == "+":
                scores.append(scores[-1]+scores[-2])
            elif operations[x] == "C":
                scores.pop(-1)
            elif operations[x] == "D":
                scores.append(scores[-1]*2)
        
        return sum(scores)
        