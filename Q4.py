def change_cutoff(marks_list,x,y):
    max=0
    change=False
    for i in range(len(marks_list)-1):
        if (marks_list[i]>=x and marks_list[i]<=y) and (marks_list[i+1]>=x and marks_list[i+1]<=y):
            change=True
            if marks_list[i]-marks_list[i+1]>=max:
                max=marks_list[i]-marks_list[i+1]
                index=i
    else:
        if change:
            return (marks_list[index]+marks_list[index+1])/2
        else:
            return (x+y)/2

class Course:
    def __init__(self,name="",credits=0,assessments=[]):
        self.name=name
        self.credits=credits
        self.assessments=assessments
        
    def grading_policy(self,marks_list):
        self.cutoff={"A":80,"B":65,"C":50,"D":40,"F":0}
        self.marks_list=sorted(marks_list,reverse=True)
        
        self.cutoff["A"]=change_cutoff(self.marks_list,78,82)
        self.cutoff["B"]=change_cutoff(self.marks_list,63,67)
        self.cutoff["C"]=change_cutoff(self.marks_list,48,52)
        self.cutoff["D"]=change_cutoff(self.marks_list,38,42)
        self.cutoff["F"]=change_cutoff(self.marks_list,-2,2)
    
class Student:
    def __init__(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks
        
    def calc_marks(self):
        return sum(self.marks)
    
course=input("Enter name of the course: ")
creds=int(input("Enter the number of credits: "))
assessments=list(input("Enter the criteria for assessments: ").split())
weights=list(map(int,input("Enter the weights: ").split()))

course1=Course(course,creds,list(zip(assessments,weights)))
    
file_name=input("Enter the filename: ")
with open(f"CSE101-Assignment-3\{file_name}.txt","r") as F:
    data=F.readlines()

marks=[]
student_list={}
for i in data:
    student1=Student(i.strip().split()[0],list(map(float,i.strip().split()[1:])))
    
    student_list.update({student1.rollno:[student1.marks,student1.calc_marks()]})
    marks.append(student1.calc_marks())
else:        
    course1.grading_policy(marks)

option=input("1) Generate a summary\n2) Print the grades in a file\n3) Search for a student record\nEnter the option: ")

while option:
    
    if option=='1':
        print(f"Course name: {course1.name}, Credits: {course1.credits}, Assessments: {[i[0] for i in course1.assessments]}, Weights: {[i[1] for i in course1.assessments]}")
        print("Cutoffs:",course1.cutoff)
        
        frequency={"A":0,"B":0,"C":0,"D":0,"F":0}
        for i in course1.marks_list:
            for j in course1.cutoff:
                if i>=course1.cutoff[j]:
                    frequency[j]+=1
                    break
            
        print("Number of A's:",frequency["A"], "Number of B's:",frequency["B"], "Number of C's:",frequency["C"], "Number of D's:",frequency["D"], "Number of F's:",frequency["F"])
        
    elif option=='2':
        F=open("CSE101-Assignment-3\Course_coding.txt","w")
        for i in student_list:
            to_write=i+str(student_list[i])+" Grade:"
            
            if student_list[i][1]>=course1.cutoff["A"]:
                to_write+='A'
            elif student_list[i][1]>=course1.cutoff["B"]:
                to_write+='B'
            elif student_list[i][1]>=course1.cutoff["C"]:
                to_write+='C'
            elif student_list[i][1]>=course1.cutoff["D"]:
                to_write+='D'
            else:
                to_write+='F'
                
            print(to_write)             
            F.write(to_write+"\n")
        else:
            F.close()
            
    elif option=='3':
        name=input("Enter roll no. of student: ")
        
        if name in student_list:
            print(list(zip(student_list[name][0],course1.assessments)),end=" Grade:")
            if student_list[i][1]>=course1.cutoff["A"]:
                print('A')
            elif student_list[i][1]>=course1.cutoff["B"]:
                print('B')
            elif student_list[i][1]>=course1.cutoff["C"]:
                print('C')
            elif student_list[i][1]>=course1.cutoff["D"]:
                print('D')
            else:
                print('F')
        else:
            print("Name not found!")
    else:
        print("Enter a valid option!")
    
    option=input("1) Generate a summary\n2) Print the grades in a file\n3) Search for a student record\nEnter the option: ").strip()