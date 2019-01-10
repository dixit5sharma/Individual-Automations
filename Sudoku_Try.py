def find_posibilities(a):
    d={}
    for i in range(9):
        for j in range(9):
            if a[i][j]=="*":
                s={'1','2','3','4','5','6','7','8','9'} # Set
                for k in range(9):
                    s.discard(a[i][k])
                    s.discard(a[k][j])
                if (i+1)%3==1 and (j+1)%3==1:
                    s.discard(a[i+1][j+1])
                    s.discard(a[i+2][j+1])
                    s.discard(a[i+1][j+2])
                    s.discard(a[i+2][j+2])
                if (i+1)%3==1 and (j+1)%3==2:
                    s.discard(a[i+1][j-1])
                    s.discard(a[i+2][j-1])
                    s.discard(a[i+1][j+1])
                    s.discard(a[i+2][j+1])
                if (i+1)%3==1 and (j+1)%3==0:
                    #print(a[i+1][j-1] , a[i+2][j-1], a[i+1][j-2], a[i+2][j-2])
                    s.discard(a[i+1][j-1])
                    s.discard(a[i+2][j-1])
                    s.discard(a[i+1][j-2])
                    s.discard(a[i+2][j-2])

                if (i+1)%3==2 and (j+1)%3==1:
                    s.discard(a[i+1][j+1])
                    s.discard(a[i-1][j+1])
                    s.discard(a[i+1][j+2])
                    s.discard(a[i-1][j+2])
                if (i+1)%3==2 and (j+1)%3==2:
                    s.discard(a[i-1][j-1])
                    s.discard(a[i-1][j+1])
                    s.discard(a[i+1][j+1])
                    s.discard(a[i+1][j-1])
                if (i+1)%3==2 and (j+1)%3==0:
                    s.discard(a[i-1][j-1])
                    s.discard(a[i-1][j-2])
                    s.discard(a[i+1][j-1])
                    s.discard(a[i+1][j-2])

                if (i+1)%3==0 and (j+1)%3==1:
                    s.discard(a[i-1][j+1])
                    s.discard(a[i-2][j+1])
                    s.discard(a[i-1][j+2])
                    s.discard(a[i-2][j+2])
                if (i+1)%3==0 and (j+1)%3==2:
                    s.discard(a[i-1][j-1])
                    s.discard(a[i-2][j+1])
                    s.discard(a[i-1][j+1])
                    s.discard(a[i-2][j-1])
                if (i+1)%3==0 and (j+1)%3==0:
                    s.discard(a[i-1][j-1])
                    s.discard(a[i-2][j-1])
                    s.discard(a[i-1][j-2])
                    s.discard(a[i-2][j-2])
                #print(s)
                if len(s)==1:
                    a[i][j]=int(s.pop())
##                elif len(s)==2:
##                    d["a["+str(i+1)+"]["+str(j+1)+"]"]=list(s)
                    
##    print(d)
    return a


with open("SudokuFile2.txt","r") as f:
    a=[]
    for line in f:
        a.append(list(map(str,line.split())))

find_posibilities(a)

for i in range(9):
    for j in range(9):
        print(a[i][j],end=" ")
    print()
