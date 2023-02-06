def print_menu():
    print("Enter your option:\n1) Show the records of the student and wheter currently present\n2) List of students who entered and exited the campus during the time interval\n3) List of students who entered/exited from a certain gate number\n")
    
with open("CSE101-Assignment-3\sorted_data.txt","r") as F:
    file=F.readlines()
    
data={}
for i in range(1,len(file)):
    temp=file[i].split(",")
    time=temp[3].strip().split(":")
    seconds=int(time[0])*3600+int(time[1])*60+int(time[2])

    if temp[0] in data:                                                                             #Appending the data            
        data[temp[0]]+=[{"Crossing":temp[1].strip(),"Gate":temp[2].strip(),"Time":seconds}]
    else:
        data.update({temp[0]:[{"Crossing":temp[1].strip(),"Gate":temp[2].strip(),"Time":seconds}]})

for i in data:     
    j=0                                                                                             #Removing consecutive Entries and Exits
    while j<len(data[i])-1:                                                                                      
        if data[i][j]["Crossing"]==data[i][j+1]["Crossing"]=="ENTER":
            data[i].pop(j+1)
        elif data[i][j]["Crossing"]==data[i][j+1]["Crossing"]=="EXIT":
            data[i].pop(j)
        else:
            j+=1
            
for i in data:                                                                                      #Sorting crossing wrt. time
    data[i].sort(key=lambda x:x["Time"])
    
print(len(data))
for i in data:
    print(i,len(data[i]))

print_menu()
option=input()
while option:
        
    if option=="1":
        name=input("Student name: ")
        time=input("Enter the current time: ").split(":")
        
        seconds=int(time[0])*3600+int(time[1])*60+int(time[2])
        
        for i in data[name]:
            if i["Time"]<seconds:
                print(i)
        else:
            in_campus="is in" if i["Crossing"]=="ENTER" else "is not in"
            
            print(f'{name} {in_campus} the campus currently')
            
    elif option=="2":
        start_time=input("Enter the start time: ").split(":")
        end_time=input("Enter the end time: ").split(":")
        
        start_seconds=int(time[0])*3600+int(time[1])*60+int(time[2])
        end_seconds=int(time[0])*3600+int(time[1])*60+int(time[2])
        
        G=open("CSE101-Assignment-3\Enter.txt","w")    
        H=open("CSE101-Assignment-3\Exit.txt","w")
        for i in data:
            for j in range(len(data[i])):
                if data[i][j]["Time"]>start_seconds and data[i][j]["Time"]<end_seconds:
                        gate=data[i][j]["Gate"]
                            
                        hours=data[i][j]["Time"]//3600
                        hours=str(hours) if hours>9 else "0"+str(hours)
                            
                        minutes=(data[i][j]["Time"]%3600)//60
                        minutes=str(minutes) if minutes>9 else "0"+str(minutes)
                            
                        seconds=(data[i][j]["Time"]%3600%60)
                        seconds=str(seconds) if seconds>9 else "0"+str(seconds)
                        
                        time=hours+":"+minutes+":"+seconds
                        
                        if data[i][j]["Crossing"]=="ENTER":
                            G.write(f"{i}, ENTER, {gate}, {time}")
                        else:
                            H.write(f"{i}, EXIT, {gate}, {time}")
        else:
            G.close()
            H.close()
            
    elif option=="3":
        gate=input("Enter the gate number: ")
        
        count_entry=0
        count_exit=0
        
        for i in data:
            for j in range(len(data[i])):
                if data[i][j]["Gate"]==gate and data[i][j]["Crossing"]=="ENTER":
                    count_entry+=1
                elif data[i][j]["Gate"]==gate and data[i][j]["Crossing"]=="EXIT":
                    count_exit+=1
        else:
            print("Number of entries from the gate:",count_entry)
            print("Number of exits from the gate:",count_exit)
    else:
        print("Enter a valid input!")
    
    print_menu()
    option=input()