l=[1,2,3,4,5,1000,1234,4534]

for x in l:
    print(f"{x} - line x")

for x in l:
    print(f"{x:5} - line x")


for x in l:
    print(f"{x:^5} - line x")

for x in l:
    print(f"{x:<5.2f} - line x")

for x in l:
    print("{:^5.2f} - line x".format(x))

for x in l:
    print("{1:^5.2f} - line {0:<5d}".format(x,x+100))
