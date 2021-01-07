`#Declaring variable
a=10
print(a)

#Declaring as string
name="Sachin"
print(name)

#concatenation 
print(str(a)+name)

#print(a+name)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Declaring Global and Local variable
var="I am Global Variable"
print(var)
def localfun():
    var="I am Local Variable"
    print(var)
localfun()
print(var)

