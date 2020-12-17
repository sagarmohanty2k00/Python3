class Car:
    def __init__(self, n="generic", w="alloy", e="v8", c="white"):
        self.wheels = w
        self.engine = e
        self.color = c
        self.name = n


    def name_modification(self, name):
        self.name = name



maruti = Car(n="maruti")
print(maruti.name + maruti.wheels+ maruti.engine + maruti.color)

audi = Car(c="black", n="audi")
print(audi.name + audi.wheels+audi.engine+audi.color)

g = Car()
g.name = "amba"

print(g.name)

g.name_modification("nua car")
print(g.name)