import random

def sentences(x):
    k=0
    sentences=[]
    
    for i in range(len(x)):
        if x[i] in ".":
            for j in range(i,len(x)):
                if x[j] in "  \n":
                    break
            sentences.append(x[k:i+1])
            k=j+1
    else:
        sentences.append(x[k:i+2])
        sentences=[x for x in sentences if x]
        
        return sentences
            
def words(x):
    return x.split()

def F1_factor(x):
    w1=words(x)
    
    if not w1:
        return 0
    return len(set(w1))/len(w1)

def F2_factor(x):
    dict={}
    for i in words(x):
        if i not in dict:
            dict.update({i:1})
        else:
            dict[i]+=1
    
    items=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    if not words(x):
        return 0
    
    sum_items=0
    top5=[]
    for i in range(5):
        sum_items+=items[i][1]
        top5.append(items[i][0])
        
    return sum_items/len(words(x)),top5

def F3_factor(x):
    if not words(x):
        return 0
    return len([i for i in sentences(x) if len(i.split())>35 or len(i.split())<5])/len(sentences(x))
            
def F4_factor(x):
    count=0
    if not words(x):
        return 0
    
    for j in words(x):
        if j.count(".")+j.count(",")+j.count(":")+j.count(";")>1:
            count+=1
    return count/len(words(x))
        
def F5_factor(x):
    return 1 if len(words(x))>750 else 0

n=int(input("Enter the number of files to be graded: "))

try:
    G=open("CSE101-Assignment-3\scores.txt","w")
    for i in range(1,n+1):
        with open(f"CSE101-Assignment-3\File{i}.txt","r") as F:
            x=F.read().lower()
        
        net_score=4+F1_factor(x)*6+F2_factor(x)[0]*6-F3_factor(x)-F4_factor(x)-F5_factor(x)
        #print(F1_factor(x),F2_factor(x),F3_factor(x),F4_factor(x),F5_factor(x))
    
        G.write(f"File{n}.txt\n")
        G.write(f"score:{net_score}\n")
        G.write(f"{F2_factor(x)[1]}\n")
        G.write(f"{random.choices(words(x), k=5)}\n\n")
    else:
        G.close()
except FileNotFoundError:
    print("File not Found!")