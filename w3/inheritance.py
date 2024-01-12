class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

x=Person("Mahady","hasan")
x.printname()

class Student(Person):
#  pass 
#  pass used for skipped the other properties to the class

    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.g=year

    # def printname(self):
    #         super().printname()
    #         print("Year:", self.g)
        
o = Student("Hasan","Fahim",2025)
## for the probelm of 2025, it need to add
o.printname()