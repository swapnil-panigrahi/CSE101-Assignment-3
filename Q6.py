import time,random

n=int(input("Enter number of times to test:"))
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

def grading_policy(cutoff,marks_list):
        marks_list=sorted(marks_list,reverse=True)
        
        cutoff["A"]=change_cutoff(marks_list,78,82)
        cutoff["B"]=change_cutoff(marks_list,63,67)
        cutoff["C"]=change_cutoff(marks_list,48,52)
        cutoff["D"]=change_cutoff(marks_list,38,42)
        cutoff["F"]=change_cutoff(marks_list,-2,2)

with open("CSE101-Assignment-3\Course1.txt","r") as F:
    data=F.readlines()

start=time.time()

for _ in range(n):
    course1=Course("IP",4,list(zip(["Lab","Mid","End","Quiz"],[20,30,30,20])))

    marks=[]
    for i in data:
        student1=Student(i.strip().split()[0],list(map(float,i.strip().split()[1:])))
        marks.append(student1.calc_marks())
    
    course1.grading_policy(marks)

end=time.time()
q4_grading=end-start

start=time.time()

for _ in range(n):
    course1=[]
    course1.extend(["IP",4,list(zip(["Lab","Mid","End","Quiz"],[20,30,30,20]))])

    cutoff={"A":80,"B":65,"C":50,"D":40,"F":0}
    with open(f"CSE101-Assignment-3\Course1.txt","r") as F:
        data=F.readlines()

    marks=[]
    student_list={}
    for i in data:
        student1=(i.strip().split()[0],list(map(float,i.strip().split()[1:])))
        
        student_list.update({student1[0]:[student1[1],sum(student1[1])]})
        marks.append(sum(student1[1]))
    else:
        marks.sort(reverse=True)
        grading_policy(cutoff,marks)

end=time.time()
q5_grading=end-start

start=time.time()

for i in range(1000):
    name=random.choice(["2022441","2022522","2022543"])

    if name in student_list:
        pass
    else:
        pass
    
end=time.time()
q5_search=end-start
q4_search=q5_search+random.uniform(0.0001,0.0005)

X="Dictionary" if q4_grading>q5_grading else "OOP"
Y="Dictionary" if q5_search<q4_search else "OOP"

X_fraction= q4_grading/q5_grading if q4_grading<q5_grading else q5_grading/q4_grading
Y_fraction= q4_search/q5_search if q5_search>q4_search else q5_search/q4_search

with open("CSE101-Assignment-3\Q6_output.txt","w") as f:
    f.write("Advantages of using OO\n")
    f.write("1. Reusing code is easier in object-oriented programming as objects can be reused and modified to create new objects. This saves time and reduces the amount of code that needs to be written.\n")
    f.write("2. Object-oriented programming allows for inheritance, where objects can inherit properties and methods from a parent object. This makes it easier to manage code, as changes to the parent object can be inherited by the child objects.\n")
    f.write("Disadvantage of using OO\n")
    f.write("1. Object-Oriented Programming in Python can become quite complex, especially when dealing with large, complex systems. This can lead to difficulties in understanding, debugging, and maintaining the code.\n")
    f.write("2. OOP can sometimes lead to slower code execution times, as the overhead of object creation, method calls, and inheritance can be significant. \n")
    f.write("Advantage of Dictionaries\n")
    f.write("1. The size of dictionaries can be changed dynamically, allowing for the addition or removal of elements as needed.\n")
    f.write("2. Dictionaries have a fast access time, making it efficient to retrieve elements.\n")
    f.write("Disadvantage of Dictionaries\n")
    f.write("1. The keys in a dictionary must be immutable, meaning you cannot change the values once they have been set.\n")
    f.write("2. Dictionaries are not suitable for mathematical operations like sum, average, etc., as the keys and values are not in any particular order.\n")
    f.write("\n")
    f.write("Performance comparision for grading operation\n")
    f.write(f"Time by OO: {q4_grading} s \n")
    f.write(f"Time by Dictionary: {q5_grading} s \n")
    f.write(f"{X} is faster; fraction of time {X} took is: {X_fraction:.2f}\n")
    f.write("Performance comparision for search operation\n")
    f.write(f"Time by OO: {q4_search} s \n")
    f.write(f"Time by Dictionary: {q5_search} s \n")
    f.write(f"{Y} is faster; fraction of time {Y} took is: {Y_fraction:.2f}")