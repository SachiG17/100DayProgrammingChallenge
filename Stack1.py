#Creating the stack
def create_stack():
    stack=[]
    return stack

#Checking if stack is empty
def isempty(stack):
    return len(stack)==0

#Pushing the item into stack
def push(stack,item):
    stack.append(item)
    print("Appended item is ",item)
    
#Popping item out
def pop(stack):
    if isempty(stack):
        print("Stack is empty")
    return stack.pop()

stack=create_stack()
push(stack,1)
push(stack,2)
push(stack,3)
print(stack)

print("popped item is ",pop(stack))
print("stack after popping",str(stack))
