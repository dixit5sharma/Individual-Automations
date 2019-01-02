with open(r"Line.txt","r") as f:
    f.seek(0)
    k = f.readlines()

with open(r"Line2.txt","w") as second:
    second.seek(0)
    for i in range(len(k)):
        print(str(i+1)+"."+str(k[i]),file = second, end="")
