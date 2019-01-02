f = open(r"CreateItself.txt","a")    # Creates itself if not there

###option 1
##f.seek(0)
##all_content = f.read()
##print(all_content)
##
###option 2
##f.seek(0)
##for line in f:
##    print(line)
##
###option 3
##f.seek(0)
##content = f.read(5)
##while content!='':
##    print(content)
##    content = f.read(5)
##    print("______________________")
##    print(f.tell())
##    print("______________________")
##
###option 4
##f.seek(0)
##lines = f.readlines()
##
##f.close()

#Write to files
f.write('anna has 2 apples\n')
print('anna has 2 apples',file = f)
f.close()
