print("Input Sudoku - ")
with open("SudokuFile.txt","r") as f:
    a=[]
    for line in f:
        a.append(list(map(str,line.split())))
        print(line,end="")

counter=0
loopContinue=True
while(loopContinue):
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
                if len(s)==1:
                    a[i][j]=str(s.pop())
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
