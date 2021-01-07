#Declaring Global and Local variable
var="I am Global Variable"
print(var)
def localfun():
    var="I am Local Variable"
    print(var)
localfun()
print(var)

print("--------------------------------------------------------------")
print("Referencing the global varible in function")
var="I am Global Variable"
print(var)
def localfun():
    global var
    var="I am Local Variable"
    print(var)
    var="I have changed variable"
localfun()
print(var)
#We could see that the global variable has been changed
#Deleting the varibale
del var
print(var)

