def up_pat(stars,space):
    if stars==1:
        print("* "*stars+"  "*space*2+"* "*stars)
    else:
        print("* "*stars+"  "*space*2+"* "*stars)
        return up_pat(stars-1,space+1)
    
def down_pat(stars,space):
    if space==0:
        print("* "*stars*2)
    else:
        print("* "*stars+"  "*space*2+"* "*stars)
        return down_pat(stars+1,space-1)

n=int(input("Enter N: "))
if n==1:
    print('* *')
else:
    up_pat(n,0)
    down_pat(2,n-2)