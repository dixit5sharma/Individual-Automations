import random

l = list(map(int,input("Enter a range of numbers comma separated and i will think of a number between them - ").split(",")))
s,e = l[0],l[1]
max_try = int(input("Enter maximum try limit - "))
print("I am thinking of a number between",s,"and",e)
secret_number = random.randint(s,e)
found=False
for i in range(max_try):
    k = int(input("Enter a guess - "))
    if k<secret_number:
        if secret_number-k<(max_try//2):
            print("You are near. Keep Guessing")
        else:
            print("Guessed number is too low")
    elif k>secret_number:
        if k-secret_number<(max_try//2):
            print("You are near. Keep Guessing")
        else:
            print("Guessed number is too High")
    else:
        print("Bingo!!! You guessed it right in",i+1,"attempts")
        found=True
        break
if not(found):
    print("The number i was thinking is",secret_number)
