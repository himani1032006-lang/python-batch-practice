class Programmer():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("good morning")
h1=Programmer("harry",21)
print(h1.name,h1.age)
h1.display()