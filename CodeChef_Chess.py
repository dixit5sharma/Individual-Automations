def permutation(i):
    return [[int(i[0]+2),int(i[1]+1)],[int(i[0]+2),int(i[1]-1)],[int(i[0]-2),int(i[1]+1)],[int(i[0]-2),int(i[1]-1)],[int(i[0]-1),int(i[1]+2)],[int(i[0]-1),int(i[1]-2)],[int(i[0]+1),int(i[1]-2)],[int(i[0]+1),int(i[1]-2)]]

def permut_King(i):
    return [[int(i[0]+0),int(i[1]+0)],[int(i[0]+1),int(i[1]+0)],[int(i[0]-1),int(i[1]+0)],[int(i[0]-1),int(i[1]+1)],[int(i[0]+0),int(i[1]+1)],[int(i[0]+1),int(i[1]+1)],[int(i[0]-1),int(i[1]-1)],[int(i[0]+0),int(i[1]-1)],[int(i[0]+1),int(i[1]-1)]]

testcases = int(input())
answer = []
while(testcases>0):    
    N = int(input())
    pos=[]
    for i in range(N):
        pos.append(list(map(int,input().split())))
    Kpos = list(map(int,input().split()))

    Knightpos=[]
    check=False
    for items in pos:
        ret = permutation(items)
        Knightpos.extend(ret)
            
    Kret = permut_King(Kpos)
    for each in Kret:
        if each in Knightpos:
            check=True
    if check==True:
        answer.append("YES")
    else:
        answer.append("NO")
    testcases = testcases-1

for each in answer:
    print(each)
