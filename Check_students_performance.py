class student:
    def __init__(self,name,test_score,attendence):
        self.name = name
        self.test_score = test_score
        self.attendence = attendence
        
    def student_check(self):
        self.attendence >= 75
        self.test_score > 90
        if self.attendence and self.test_score >90:
            print('Regular student')
        else:
            print('Irregular student')
            
student1 = student('Riya',55,90)
print(student1.student_check())
        
student2 = student('Arya',94,80)
print(student2.student_check())

