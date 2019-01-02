Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ("a", "b", "c", "d", "e", "f", "g", "h")
>>> a[slice[2]]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[slice[2]]
TypeError: 'type' object is not subscriptable
>>> a[slice(2)]
('a', 'b')
>>> a[:2]
('a', 'b')
>>> alph = ["a", "b", "c", "d"]
>>> list(reversed(alph))
['d', 'c', 'b', 'a']
>>> k = (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> 
>>> x = k
>>> print(x)
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> 
>>> a = ("John", "Charles", "Mike")
>>> b = ("Jenny", "Christy", "Monica")
>>> 
>>> x = zip(a, b)
>>> x
<zip object at 0x02DFA288>
>>> a
('John', 'Charles', 'Mike')
>>> b
('Jenny', 'Christy', 'Monica')
>>> x
<zip object at 0x02DFA288>
>>> vars
<built-in function vars>
>>> x
<zip object at 0x02DFA288>
>>> x
<zip object at 0x02DFA288>
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': ('John', 'Charles', 'Mike'), 'alph': ['a', 'b', 'c', 'd'], 'k': (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')), 'x': <zip object at 0x02DFA288>, 'b': ('Jenny', 'Christy', 'Monica')}
>>> 
>>> x
<zip object at 0x02DFA288>
>>> x
<zip object at 0x02DFA288>
>>> tuple(x)
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> x
<zip object at 0x02DFA288>
>>> k = tuple(x)
>>> x
<zip object at 0x02DFA288>
>>> k
()
>>> print(tuple(x))
()
>>> 
>>> x
<zip object at 0x02DFA288>
>>> tuple(x)
()
>>> list(x)
[]
>>> x = zip(a, b)
>>> tuple(x)
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> tuple(x)
()
>>> tuple(x)
()
>>> x = zip(a, b)
>>> print(tuple(x))
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> print(tuple(x))
()
>>> x = zip(a, b)
>>> m = tuple(x)
>>> n = tuple(x)
>>> m
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> n
()
>>> m
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> m
(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
>>> n
()
>>> t = tuple(1,2,3)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    t = tuple(1,2,3)
TypeError: tuple expected at most 1 arguments, got 3
>>> t = tuple(1)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    t = tuple(1)
TypeError: 'int' object is not iterable
>>> t = (1,2,3,4,5)
>>> type(t)
<class 'tuple'>
>>> m = t
>>> n = t
>>> m
(1, 2, 3, 4, 5)
>>> n
(1, 2, 3, 4, 5)
>>> l = [1,2,3,4,5]
>>> t = tuple(l)
>>> t
(1, 2, 3, 4, 5)
>>> t
(1, 2, 3, 4, 5)
>>> m
(1, 2, 3, 4, 5)
>>> l = [1,2,3,4,5,6]
>>> t = tuple(l)
>>> t
(1, 2, 3, 4, 5, 6)
>>> m
(1, 2, 3, 4, 5)
>>> n
(1, 2, 3, 4, 5)
>>> m = tuple(t)
>>> n = tuple(t)
>>> m
(1, 2, 3, 4, 5, 6)
>>> n
(1, 2, 3, 4, 5, 6)
>>> n = tuple(m)
>>> n
(1, 2, 3, 4, 5, 6)
>>> x
<zip object at 0x02C4FF58>
>>> m = x
>>> m
<zip object at 0x02C4FF58>
>>> n = x
>>> n
<zip object at 0x02C4FF58>
>>> m = tuple(x)
>>> x
<zip object at 0x02C4FF58>
>>> m
()
>>> txt = "Hello, And Welcome To My WORLD!"
>>> txt.casefold()
'hello, and welcome to my world!'
>>> txt
'Hello, And Welcome To My WORLD!'
>>> txt.lower()
'hello, and welcome to my world!'
>>> txt
'Hello, And Welcome To My WORLD!'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
>>> logging.debug('Start of program')
 2018-12-22 11:10:09,692 - DEBUG - Start of program
>>> 
>>> 
>>> 
>>> 
>>> txt = "My name is Ståle"
>>> k = txt.encode()
>>> k
b'My name is St\xc3\xa5le'
>>> k.decode()
'My name is Ståle'
>>> k
b'My name is St\xc3\xa5le'
>>> k.pop()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    k.pop()
AttributeError: 'bytes' object has no attribute 'pop'
>>> k.pop
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    k.pop
AttributeError: 'bytes' object has no attribute 'pop'
>>> k.flush
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    k.flush
AttributeError: 'bytes' object has no attribute 'flush'
>>> k.flush()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    k.flush()
AttributeError: 'bytes' object has no attribute 'flush'
>>> var(k)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    var(k)
NameError: name 'var' is not defined
>>> var(string)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    var(string)
NameError: name 'var' is not defined
>>> help(string)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    help(string)
NameError: name 'string' is not defined
>>> dir(string)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    dir(string)
NameError: name 'string' is not defined
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> 
>>> 
>>> if "i" in "Dixit":
	print("YES")

	
YES
>>> __hash__
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    __hash__
NameError: name '__hash__' is not defined
>>> 
>>> 
>>> "Dixit".__hash__
<method-wrapper '__hash__' of str object at 0x02E92960>
>>> list("Dixit".__hash__)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    list("Dixit".__hash__)
TypeError: 'method-wrapper' object is not iterable
>>> list("Dixit".__hash__())
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    list("Dixit".__hash__())
TypeError: 'int' object is not iterable
>>> int("Dixit".__hash__())
581075685
>>> int("Dixit".__hash__)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    int("Dixit".__hash__)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'method-wrapper'
>>> int("Dixit".__hash__())
581075685
>>> 
>>> 
>>> a = "Dixit"
>>> b = hash(a)
>>> b
581075685
>>> b=a
>>> hash(b)
581075685
>>> a = "Dixit"
>>> c = "Dixiu"
>>> hash(c)
-1272286860
>>> hash(a)
581075685
>>> hash(c)
-1272286860
>>> hash(c) = 2313423
SyntaxError: can't assign to function call
>>> hash(14235)
14235
>>> hash(142354647563)
620726861
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
KeyboardInterrupt
>>> txt = "H\te\tl\tl\to"
>>> txt
'H\te\tl\tl\to'
>>> txt.expandtabs()
'H       e       l       l       o'
>>> txt.expandtabs(8)
'H       e       l       l       o'
>>> txt.expandtabs(1)
'H e l l o'
>>> a = "Hello"
>>> a.expandtabs(2)
'Hello'
>>> a.expandtabs(10)
'Hello'
>>> 
>>> 
>>> 
>>> a = [1,2,3,4,5]
>>> k = ";".join(tuple(list(a[0],a[3])))
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    k = ";".join(tuple(list(a[0],a[3])))
TypeError: list expected at most 1 arguments, got 2
>>> k = ";".join(tuple(list(a[0]+a[3])))
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    k = ";".join(tuple(list(a[0]+a[3])))
TypeError: 'int' object is not iterable
>>> k = ";".join(tuple(list(a)))
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    k = ";".join(tuple(list(a)))
TypeError: sequence item 0: expected str instance, int found
>>> k = ";".join(tuple(list(map(str,a))))
>>> k
'1;2;3;4;5'
>>> k = ";".join(tuple(list(map(str,a[0::3]))))
>>> k
'1;4'
>>> k = ";".join(tuple(list(a[0::3])))
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    k = ";".join(tuple(list(a[0::3])))
TypeError: sequence item 0: expected str instance, int found
>>> tuple(1,2,3)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    tuple(1,2,3)
TypeError: tuple expected at most 1 arguments, got 3
>>> tuple(a)
(1, 2, 3, 4, 5)
>>> k = ";".join(tuple(a[0::3]))
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    k = ";".join(tuple(a[0::3]))
TypeError: sequence item 0: expected str instance, int found
>>> k = ";".join(
	)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    k = ";".join(
TypeError: join() takes exactly one argument (0 given)
>>> tuple(a[0::3])
(1, 4)
>>> k = ";".join(tuple(a[0::3]))
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    k = ";".join(tuple(a[0::3]))
TypeError: sequence item 0: expected str instance, int found
>>> k = "1".join(tuple(a[0::3]))
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    k = "1".join(tuple(a[0::3]))
TypeError: sequence item 0: expected str instance, int found
>>> k = 1.join(tuple(a[0::3]))
SyntaxError: invalid syntax
>>> k = 1.join(tuple(a[0::3]))
SyntaxError: invalid syntax
>>> b = 1
>>> k = b.join(tuple(a[0::3]))
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    k = b.join(tuple(a[0::3]))
AttributeError: 'int' object has no attribute 'join'
>>> k = ";".join(tuple(a[0::3]))
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    k = ";".join(tuple(a[0::3]))
TypeError: sequence item 0: expected str instance, int found
>>> t = tuple((1,2))
>>> t
(1, 2)
>>> ";".join(t)
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    ";".join(t)
TypeError: sequence item 0: expected str instance, int found
>>> 
>>> 
>>> 
>>> 
>>> txt = "I could eat bananas all day bananas are very good"
>>> txt.partition("ban")
('I could eat ', 'ban', 'anas all day bananas are very good')
>>> txt.partition("zan")
('I could eat bananas all day bananas are very good', '', '')
>>> txt.partition("bananas")
('I could eat ', 'bananas', ' all day bananas are very good')
>>> txt.partition("bananas")[3]
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    txt.partition("bananas")[3]
IndexError: tuple index out of range
>>> txt.partition("bananas")[2]
' all day bananas are very good'
>>> txt.partition("bananas")[2].strip()
'all day bananas are very good'
>>> txt.partition("bananas")[2].strip().isEmpty()
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    txt.partition("bananas")[2].strip().isEmpty()
AttributeError: 'str' object has no attribute 'isEmpty'
>>> txt.partition("bananas")[2].strip()==""
False
>>> for i in range(10):
        if i==5:
            break
        print(i)
else:
    print(i)
    print("for statement successful")

0
1
2
3
4
>>> for i in range(10):
        if i==5:
        print(i)
else:
    print(i)
    print("for statement successful")
SyntaxError: expected an indented block
>>> 
>>> for i in range(10):
        print(i)
else:
    print(i)
    print("for statement successful")

0
1
2
3
4
5
6
7
8
9
9
for statement successful
>>> 
>>> 
>>> 
>>> 
>>> x = ('key1', 'key2', 'key3')
>>> l = dict.fromkeys(x,1)
>>> l
{'key1': 1, 'key2': 1, 'key3': 1}
>>> 
>>> 
>>> def myfunc1():
  x = "John"
  def myfunc2():
    global x = "hello"
  myfunc2()
  return x
SyntaxError: invalid syntax
>>> 
>>> 
>>> def myfunc1():
	x = "John"
	def myfunc2():
		global x = "hello"
	myfunc2()
	return x
SyntaxError: invalid syntax
>>> def myfunc1():
	x = "John"
	def myfunc2():
global x = "hello"
	myfunc2()
	return x
SyntaxError: expected an indented block
>>> def func1():
x= "John"
SyntaxError: expected an indented block
>>> 
>>> txt = "Hello World"
>>> txt.reverse()
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    txt.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> txt.reverse
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    txt.reverse
AttributeError: 'str' object has no attribute 'reverse'
>>> 
>>> 
>>> 
>>> mylist = ["a", "b", "a", "c", "c"]
>>> mylist = list(dict.fromkeys(mylist))
>>> mylist
['a', 'b', 'c']
>>> 
