print("Input Sudoku - ")

with open("Files/SudokuFileEasy.txt","r") as f:
    a=[]
    for line in f:
        print(line,end="")
        a.append(list(map(int,line.split())))

loopContinue=True
while(loopContinue):
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                s={1,2,3,4,5,6,7,8,9} # Set
                for k in range(9):
                    s.discard(a[i][k])
                    s.discard(a[k][j])
                if len(s)==1:
                    a[i][j]=int(s.pop())
                    # print("Updated - ",a[i][j],"at",i+1,j+1)
                    loopContinue=False
    
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                loopContinue=True

print("\n")
print("Solved Sudoku - ")
for i in range(9):
    for j in range(9):
        print(a[i][j],end=" ")
    print()
