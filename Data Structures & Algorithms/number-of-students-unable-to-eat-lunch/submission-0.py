class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1 = students.count(1)
        s0 = students.count(0)
        
        while students:
            # student at front wants the sandwich
            if sandwiches[0] == 0 and s1 > 0 and s0 == 0:
                return len(students)
            elif sandwiches[0] == 1 and s0 > 0 and s1 == 0:
                return len(students)


            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                s1 = students.count(1)
                s0 = students.count(0)
            else:
                back = students.pop(0)
                students.append(back)
        return len(students)




            
