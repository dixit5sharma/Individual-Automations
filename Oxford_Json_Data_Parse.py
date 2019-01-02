import json

with open("Files/Dic.json","r") as j:
    f = json.load(j)

def find_syn(f):
    for i in f:
        if i=="antonyms":
            for j in i:
                if j=="id":
                    return i[j]
        else:
            find_syn(i)

a = find_syn(f)
