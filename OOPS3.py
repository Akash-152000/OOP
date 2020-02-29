class car:
    wheels=4
    def __init__(self):
         self.model="BMW"
         self.milege=10



c1=car()
c1.model="Audi"
car.wheels=6
c2=car()

print(c1.model,c1.milege,c1.wheels)
print(c2.model,c2.milege,c2.wheels)