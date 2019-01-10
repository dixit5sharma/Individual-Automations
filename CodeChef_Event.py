testcases = int(input())
answer=[]
while testcases>0:
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    k = input().split()
    S_E_sub = days.index(k[1]) - days.index(k[0])
    if S_E_sub>0:
        diff = S_E_sub+1
    else:
        diff = len(days)+S_E_sub+1
    counter=0
    while(diff<=int(k[3])):
        if diff>=int(k[2]):
            counter += 1
        diff+=7
    if counter>1:
        answer.append("many")
    elif counter==1:
        answer.append(diff-7)
    else:
        answer.append("impossible")
    testcases=testcases-1

for each in answer:
    print(each)
