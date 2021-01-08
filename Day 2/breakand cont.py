#break is used to exit a for loop or a while loop,
#whereas continue is used to skip the current block, and return to the "for" or "while" statement. 


#Break
count=0
while True:
    print(count)
    count=count+1
    if count>5:
        break
print()
#Continue
#Print odd numbers upto 10

for i in range(10):
    if i%2==0:
        continue
    print(i)