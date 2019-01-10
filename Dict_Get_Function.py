student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student.get('name','Not Found'))

print(student.get('result','Not Found'))    # for value not in dict, print Not Found. Does not give syntax error.

student.update({'name' : "Dixit", 'age' : '25', 'result': 'pass'})  # Update and Add in a single line

print(student)

# del student['result']     # Old Method
result = student.pop('result')  # Removes and also returns the value, if required.

print(result)
print(student)

print(student.keys())   # Print all the keys of the dictionary. type - dict_keys    Output - dict_keys(['name', 'age', 'courses'])
print(student.values()) # Print all the values of the dictionary. type - dict_values    Output - dict_values(['Dixit', '25', ['Math', 'CompSci']])
