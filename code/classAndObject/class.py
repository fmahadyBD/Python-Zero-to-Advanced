# class Person:
#     name="Fahim"
#     occupation="Software Developer"
#     networth=10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a=Person()
# print(a.name)

# a.name="hasan"
# a.info()
class Person:
    def __init__(self,a,b):
        print("hey i am a person")
        self.a=a
        self.b=b
    def info(self):
        print(f"{self.a} is {self.b}")

a=Person("Fahim","dev")
a.info()
## Decoratoes 

