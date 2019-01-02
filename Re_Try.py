import re

'''
The ? matches zero or one of the preceding group.

The * matches zero or more of the preceding group.

The + matches one or more of the preceding group.

The {n} matches exactly n of the preceding group.

The {n,} matches n or more of the preceding group.

The {,m} matches 0 to m of the preceding group.

The {n,m} matches at least n and at most m of the preceding group.

{n,m}? or *? or +? performs a nongreedy match of the preceding group.

^spam means the string must begin with spam.

spam$ means the string must end with spam.

The . matches any character, except newline characters.

\d, \w, and \s match a digit, word, or space character, respectively.

\D, \W, and \S match anything except a digit, word, or space character, respectively.

[abc] matches any character between the brackets (such as a, b, or c).

[^abc] matches any character that isn’t between the brackets.

'''

Re_MO = re.compile(r'\d{3}')
K = Re_MO.findall("String 123 String 345 String")   # Finds all occurrences
K = Re_MO.search("String 123 String 345 String")  # Search first occurrence
print(K)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')   # 0 or 1 occurrence
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo1.group(),mo2.group())

batRegex = re.compile(r'Bat(wo)*man')   # 0 or more occurrences
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo1.group(),mo2.group(),mo3.group())

batRegex = re.compile(r'Bat(wo)+man')   # 1 or more occurrences
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group(),mo3.group())


greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())


wholeStringIsNum = re.compile(r'^\d+$')
mo3 = wholeStringIsNum.search('1234567890')
print(mo3.group())


atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

robocop = re.compile(r'robocop', re.I)  # re.IGNORECASE or re.I
print(robocop.search('Robocop is part man, part machine, all cop.').group())

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))