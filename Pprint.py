import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
d={}

for each in message:
    d.setdefault(each,0)
    d[each]+=1

##pprint.pprint(d)
k = pprint.pformat(d)   # pretty value in string
print(k)
