class MyClass():
    print("rajesh")

    # If you want to declare some variables use __init__
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sum(self,a,b):
        print(a+b)


x = MyClass("Varun",30)
x.sum(20,30)
print(x.name)
print(x.age)




