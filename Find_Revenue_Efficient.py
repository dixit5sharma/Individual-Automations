def second(tp):
    return tp[1]

dic={}
with open("100 Sales Records.csv","r") as f:
    for line in f:
        try:
            k = line.split("\n")
            sp_file = k[0].split(",")
            if sp_file[0] in dic:
                dic[sp_file[0]]+=float(sp_file[11])
            else:
                dic[sp_file[0]]=float(sp_file[11])
        except:
            pass
print(sorted(tuple(dic.items()),key=second))
