#A variable is created the moment you first assign a value to it.
x = 5  #x is int type
y = "Nishita Jangid"  #y is str type


print(y)

x = "Vishu"  #x is string type now
print(x) 

'''If you want to specify the 
data type of a variable, 
this can be done by casting.
'''

p = str(3)    # p will be '3'
q = int(44)   # q will be 44
r = float(4)  # r will be 4.0

'''you can get the data type of 
the variable by using the type() 
function.'''

a = 5
b = 'Sun'

print(type(a))
print(type(b))


#Camel Case
myVariableName = "Nishita Jangid"

#pascal Case
MyVariableName = "Nishita Jangid"

#snake Case
my_variable_name = "Nishita Jangid"

#Assign multiple values to multiple variables in one line
a, b, c = "Nishita", "Vishu", "Jangid"

print(a)
print(b)
print(c)

#Assign the same value to multiple variables in one line
x = y = z = "Nishita Jangid"

print(x)
print(y)
print(z)

#unpacking a collection
fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)


'''
To create a global variable inside 
a function, 
you can use the global keyword.
'''
def myFunc():
    global x
    x = 'fantastic'

myFunc()

print("python is ", x)

