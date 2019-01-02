import os

print(os.path.join("python371","MyP_Try"))
'''
print(os.getcwd())
os.chdir("C:\\python371\\MyP")
print(os.getcwd())

os.makedirs('C:\\delicious\\walnut\\waffles')
'''

print(os.path.abspath('.'))
print(os.path.isabs(os.path.abspath('.')))


print(os.path.relpath('C:\\Windows', 'C:\\'))

