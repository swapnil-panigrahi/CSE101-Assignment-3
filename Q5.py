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

def grading_policy(cutoff,marks_list):
        marks_list=sorted(marks_list,reverse=True)
        
        cutoff["A"]=change_cutoff(marks_list,78,82)
        cutoff["B"]=change_cutoff(marks_list,63,67)
        cutoff["C"]=change_cutoff(marks_list,48,52)
        cutoff["D"]=change_cutoff(marks_list,38,42)
        cutoff["F"]=change_cutoff(marks_list,-2,2)
        
course=input("Enter name of the course: ")
creds=int(input("Enter the number of credits: "))
assessments=list(input("Enter the criteria for assessments: ").split())
weights=list(map(int,input("Enter the weights: ").split()))

course1=[]
course1.extend([course,creds,list(zip(assessments,weights))])

cutoff={"A":80,"B":65,"C":50,"D":40,"F":0}
        
file_name=input("Enter the filename: ")
with open(f"CSE101-Assignment-3\{file_name}.txt","r") as F:
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

option=int(input("1) Generate a summary\n2) Print the grades in a file\n3) Search for a student record\nEnter the option: "))

while option:
    
    if option=='1':
        print(f"Course name: {course1[0]}, Credits: {course1[1]}, Assessments: {[i[0] for i in course1[2]]}, Weights: {[i[1] for i in course1[2]]}")
        print("Cutoffs:",cutoff)
        
        frequency={"A":0,"B":0,"C":0,"D":0,"F":0}
        for i in marks:
            for j in cutoff:
                if i>=cutoff[j]:
                    frequency[j]+=1
                    break
            
        print("Number of A's:",frequency["A"], "Number of B's:",frequency["B"], "Number of C's:",frequency["C"], "Number of D's:",frequency["D"], "Number of F's:",frequency["F"])
        
    elif option=='2':
        for i in student_list:
            print(i,student_list[i],end=" Grade:")
            
            if student_list[i][1]>=cutoff["A"]:
                print('A')
            elif student_list[i][1]>=cutoff["B"]:
                print('B')
            elif student_list[i][1]>=cutoff["C"]:
                print('C')
            elif student_list[i][1]>=cutoff["D"]:
                print('D')
            else:
                print('F')
            
            print()
    
    elif option=='3':
        name=input("Enter roll no. of student: ")
        
        if name in student_list:
            print(list(zip(student_list[name][0],course1[2])),end=" Grade:")
            if student_list[i][1]>=cutoff["A"]:
                print('A')
            elif student_list[i][1]>=cutoff["B"]:
                print('B')
            elif student_list[i][1]>=cutoff["C"]:
                print('C')
            elif student_list[i][1]>=cutoff["D"]:
                print('D')
            else:
                print('F')
        else:
            print("Name not found!")
    else:
        print("Enter a valid option!")
    
    option=input("1) Generate a summary\n2) Print the grades in a file\n3) Search for a student record\nEnter the option: ").strip()