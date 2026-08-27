class Smartphone :

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def sayBrand (self):
        print ("Бренд", self.brand)

    def sayModel (self):
        print ("Модель", self.model) 

    def sayNumber (self):
        print ("Абонентский номер («+79…»)", self.number)