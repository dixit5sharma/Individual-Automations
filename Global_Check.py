def myfunc1():
    vat = "John"
    def func2():
        global vat      # Changes made here to this global variable will reflect ONLY in the main function.
        # nonlocal vat    # This is used for nested functions. Value changes inside all functions but not in main.
        vat = "Hello"
    func2()
    return vat

print(myfunc1())
print(vat)

""" Every variable defined in main code is accessable to every function but only READ ONLY.
    As soon as you make change the value of any variable inside the function, it becomes local variable
     of that function. In order to reflect the changes in the main code, use 'Global' variables.
     And if there is a need to use data within nested functions, use 'nonlocal' variables """
