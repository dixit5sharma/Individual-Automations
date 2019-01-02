print("Input Sudoku - ")
with open("Files/SudokuFile2.txt","r") as f:
    a=[]
    for line in f:
        a.append(list(map(str,line.split())))
        print(line,end="")

def create_inner_cube(k,a,i,j):
    if (i+1)%3==2:  # Good logic
        i=i-1
    if (i+1)%3==0:
        i=i-2
    if (j+1)%3==2:
        j=j-1
    if (j+1)%3==0:
        j=j-2
    if (i+1)%3==1 and (j+1)%3==1:
        k={'0'}
        for m in range(i,i+3):
            for n in range(j,j+3):
                k.add(a[m][n])
    return k

counter=0
loopContinue=True
inner={}
while(loopContinue):
    for i in range(9):
        for j in range(9):
            inner = create_inner_cube(inner,a,i,j)
            #print(inner)
            if a[i][j]=="*":
                s={'1','2','3','4','5','6','7','8','9'} # Set
                for k in range(9):
                    s.discard(a[i][k])
                    s.discard(a[k][j])
                s = s.difference(inner)
                if len(s)==1:
                    a[i][j]=str(s.pop())
                    loopContinue=False
                elif len(s)==0:
                    loopContinue=False

    for i in range(9):
        for j in range(9):
            if a[i][j]=="*":
                loopContinue=True
    counter+=1
print("\n")
print("Solved Sudoku")
for i in range(9):
    for j in range(9):
        print(a[i][j],end=" ")
    print()
