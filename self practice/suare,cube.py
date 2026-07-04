class Calculator():
    def __init__(self,n):
        self.n=n
    def square(self):
       print( self.n*self.n)
    def cube(self):
        print(self.n*self.n*self.n)
    @staticmethod
    def h():
        print("Hello")
a=Calculator(2)
a.square()
a.cube()
a.h()

