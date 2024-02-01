class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("sail")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.brand=brand

    def move(self):
        print("flay")



car1=Car("Ford","mustang")
boat1=Boat("Ibiza","Touris 20")
plane1=Plane("Boeing","747")
for i in(car1,boat1,plane1):
    print(i.brand)
    print(i.model)
    i.move()
        
       

