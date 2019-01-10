Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> chr(45)
'-'
>>> odr('A')

>>> odr(A)

>>> ord(A)

>>> ord('A')
65
>>> ord('&')
38
>>> ord(',')
44
>>> ord('z')
122
>>> a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

SyntaxError: multiple statements found while compiling a single statement
>>> a = ("John", "Charles", "Mike")
>>> b = ("Jenny", "Christy", "Monica")
>>> x = zip(a, b)
>>> print(x)
<zip object at 0x02D302B0>
>>> print(x[0])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(x[0])
TypeError: 'zip' object is not subscriptable
>>> print(x(0))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(x(0))
TypeError: 'zip' object is not callable
>>> print(tuple(x))
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> type(x)
<class 'zip'>
>>> type(tuple(x))
<class 'tuple'>
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': ('John', 'Charles', 'Mike'), 'b': ('Jenny', 'Christy', 'Monica'), 'x': <zip object at 0x02D302B0>}
>>> k=tuple(x)
>>> 
>>> 
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': ('John', 'Charles', 'Mike'), 'b': ('Jenny', 'Christy', 'Monica'), 'x': <zip object at 0x02D302B0>, 'k': ()}
>>> print(k)
()
>>> print(tuple(x))
()
>>> x = zip(a, b)
>>> print(tuple(x))
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> k=tuple(x)
>>> print(k)
()
>>> print(tuple(x))
()
>>> x = zip(a, b)
>>> k=tuple(x)
>>> print(k)
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': ('John', 'Charles', 'Mike'), 'b': ('Jenny', 'Christy', 'Monica'), 'x': <zip object at 0x004BE698>, 'k': (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))}
>>> a = ("a", "b", "c", "d", "e", "f", "g", "h")
>>> x=slice(2)
>>> print(x)
slice(None, 2, None)
>>> type(x)
<class 'slice'>
>>> a[x]
('a', 'b')
>>> x
slice(None, 2, None)
>>> alph = ["a", "b", "c", "d"]
>>> reversed(alph)
<list_reverseiterator object at 0x02D31870>
>>> for x in reversed(alph):
	print(x)

	
d
c
b
a
>>> x
'a'
>>> k
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> x
'a'
>>> x = zip(a, b)
>>> x
<zip object at 0x004501C0>
>>> list(x)
[('a', 'Jenny'), ('b', 'Christy'), ('c', 'Monica')]
>>> txt = "Hello, And Welcome To My World!"
>>> txt = "Hello, And Welcome To My WORLD!"
>>> txt.casefold()
'hello, and welcome to my world!'
>>> txt
'Hello, And Welcome To My WORLD!'
>>> txt.lower()
'hello, and welcome to my world!'
>>> txt = "banana"
>>> x = txt.center(20,"*")
>>> x
'*******banana*******'
>>> range(0,10)
range(0, 10)
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> if 1 in range(10)
SyntaxError: invalid syntax
>>> if 1 in range(10):
	print("Yes")

	
Yes
>>> txt = "My name is Ståle"
>>> txt.encode()
b'My name is St\xc3\xa5le'
>>> txt.encode(encoding="ascii",errors="backslashreplace")
b'My name is St\\xe5le'
>>> txt.encode(encoding="ascii",errors="ignore")
b'My name is Stle'
>>> txt.encode(encoding="ascii",errors="namereplace")
b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
>>> txt.encode(encoding="ascii",errors="replace")
b'My name is St?le'
>>> txt.encode(encoding="ascii",errors="xmlcharrefreplace")
b'My name is St&#229;le'
>>> txt.encode(encoding="ascii",errors="strict")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    txt.encode(encoding="ascii",errors="strict")
UnicodeEncodeError: 'ascii' codec can't encode character '\xe5' in position 13: ordinal not in range(128)
>>> 
>>> 
>>> txt = "Hello, welcome to my world."

>>> txt.endswith(".")
True
>>> txt = "H\te\tl\tl\to"
>>> txt.expandtab()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    txt.expandtab()
AttributeError: 'str' object has no attribute 'expandtab'
>>> txt.expandtabs()
'H       e       l       l       o'
>>> txt.expandtabs(2)
'H e l l o'
>>> txt.expandtabs(10)
'H         e         l         l         o'
>>> txt.expandtabs(8)
'H       e       l       l       o'
>>> txt.expandtabs()
'H       e       l       l       o'
>>> 
>>> 
>>> 
>>> txt = "Hello, welcome to my world."

>>> txt.find("q")
-1
>>> txt.index("q")
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    txt.index("q")
ValueError: substring not found
>>> txt.find("e")
1
>>> txt.index("e")
1
>>> myTuple = ("John", "Peter", "Vicky")
>>> x = "#".join(myTuple)
>>> x
'John#Peter#Vicky'
>>> string.join(iterable)

>>> txt = "Mi casa, su casa."
>>> x = txt.rfind("casa")
>>> x
12
>>> txt.rindex("casa")
12
>>> 
>>> 
>>> 
>>> txt "I like bananas"
SyntaxError: invalid syntax
>>> txt = "I like bananas"
>>> x = txt.replace("bananas", "apples")
>>> x
'I like apples'
>>> txt
'I like bananas'
>>> 
>>> 
>>> 
>>> 
>>> txt = "I could eat bananas all day"
>>> x = txt.partition("bananas")
>>> x
('I could eat ', 'bananas', ' all day')
>>> txt = "I could eat bananas all day bananas are very good"
>>> x = txt.partition("bananas")
>>> x
('I could eat ', 'bananas', ' all day bananas are very good')
>>> 
>>> 
>>> 
>>> txt = "welcome to the jungle"
>>> txt.split()
['welcome', 'to', 'the', 'jungle']
>>> 
>>> 
>>> txt = "apple#banana#cherry#orange"

>>> x = txt.split("#",2)
>>> x
['apple', 'banana', 'cherry#orange']
>>> 
>>> 
>>> 
>>> txt = "Thank you for the music\nWelcome to the jungle"
>>> x = txt.splitlines()
>>> x
['Thank you for the music', 'Welcome to the jungle']
>>> 
>>> x = txt.splitlines(True)
>>> x
['Thank you for the music\n', 'Welcome to the jungle']
>>> 
>>> 
>>> txt.swapcase()
'tHANK YOU FOR THE MUSIC\nwELCOME TO THE JUNGLE'
>>> 
>>> 
>>> 
>>> 
>>> fruits = ['apple', 'banana', 'cherry']
>>> fruits.reverse()
>>> fruits
['cherry', 'banana', 'apple']
>>> car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

>>> car.copy()
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> car.pop()
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    car.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> car.popitem()
('year', 1964)
>>> car
{'brand': 'Ford', 'model': 'Mustang'}
>>> car.setdefault("model", "Bronco")
'Mustang'
>>> 
>>> car.update({'year': 1964})
>>> car
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> 
>>> thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
>>> thistuple.coun
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    thistuple.coun
AttributeError: 'tuple' object has no attribute 'coun'
>>> thistuple.count(5)
2
>>> thistuple.index(8)
3
>>> x = "hello"
>>> assert x=="hello"
>>> assert x=="bye"
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    assert x=="bye"
AssertionError
>>> x= 1,2,3
>>> x
(1, 2, 3)
>>> def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2() 
  return x

>>> myfunc1()
'hello'
>>> def myfunc1():
  x = "John"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x

>>> myfunc1()
'John'
>>> def myfunc1():
  x = "John"
  def myfunc2():
    global x
    x = "hello"
  myfunc2()
  return x

>>> myfunc1()
'John'
>>> def myfunc1():
  x = "John"
  def myfunc2():
    global x = "hello"
  myfunc2()
  return x
SyntaxError: invalid syntax
>>> 
>>> x = ('key1', 'key2', 'key3')

>>> dict.fromkeys(x)
{'key1': None, 'key2': None, 'key3': None}
>>> list(dict.fromkeys(x))
['key1', 'key2', 'key3']
>>> list(dict.fromkeys(x,0))
['key1', 'key2', 'key3']
>>> list(dict.fromkeys(x,1))
['key1', 'key2', 'key3']
>>> 
>>> 
>>> 
>>> x = ('key1', 'key2', 'key3')
>>> mylist = ["a", "b", "a", "c", "c"]
>>> mylist = list(dict.fromkeys(mylist))
>>> mylist
['a', 'b', 'c']
>>> # Way of removing duplicates
>>> 
>>> txt = "Hello World"
>>> txt.reverse()

>>> txt = "Hello World"[::-1]
>>> txt
'dlroW olleH'
>>> 
