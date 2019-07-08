num = 0
if num>0:
    print("the number is positive")
elif num == 0:
    print("the number is zero")
else:
    print("the number is negative")

fruits = ["apple","oranges","banana"]
for val in fruits:
    print(val)

num = 5
sum = 0
i = 1
while i<num:
    sum=sum+i
    i=i+1
print("the sum is",sum)


def sum(a,b):
    print(a+b)

sum(20,30)

def returnfunc(a,b):
    """this function is for returning an sum"""
    return (a+b)

x = returnfunc(50,30)
print(x)







