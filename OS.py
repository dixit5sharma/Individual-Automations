import os
import datetime
print(os.getcwd())
print("_____________")
print(os.listdir())

root="C:\\"
print(os.path.join(root,'directory','subdirectory','file'))

##for file in os.listdir():
##    if os.path.isfile(file):
##        print("file:",file)
##    else:
##        print("directory:",file)
##
##for root,directory,file in os.walk(os.getcwd()):
##    for f in file:
##        print(os.path.join(root,f))

for root,directory,file in os.walk(os.getcwd()):
    for f in file:
        print(os.path.join(root,f),datetime.datetime.fromtimestamp(int(os.stat(os.path.join(root,f)).st_mtime)))


print(datetime.date.today()-datetime.timedelta(days=1))


print(datetime.datetime.strptime("2018:11:02","%Y:%m:%d"))
