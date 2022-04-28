
# class Student():
#     def __init__(self, firstName = "Anton", lastName = "Krishtal", groupNumber = "z24-onl", age = 25):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.groupNumber = groupNumber
#         self.age = age
#     def getFullName(self):
#         print(f"{self.firstName} {self.lastName}")
    
#     def getAge(self):
#         print(f"{self.age}")


#     def getGroupNumber(self):
#         print(f"{self.groupNumber}")
   
#     def setGroupNumber(self, groupNumber):
#         self.groupNumber = groupNumber
#         # self.groupNumber = input("Введите номер группы:")

        
#     def setNameAge(self, firstName, lastName, groupNumber, age):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.groupNumber = groupNumber
#         self.age = age
    

# student1 = Student("Anton", "Krishtal", "z24-onl" , "25")
# student2 = Student("grisha", "nekrasov", "123-onl", "29")
# student3 = Student("Kolya", "vishnev", "125-onl", "27")
# student4 = Student("vasya", "Pupkin", "130-onl", "21")
# student5 = Student("dasha", "yakovina", "114-onl", "19")

# student1.setNameAge("Anton", "Krishtal", "z24-onl" , "25")
# student1.setGroupNumber("z27-onl")
# student1.getFullName()
# student1.getAge()
# student1.getGroupNumber()

# student2.setNameAge("grisha", "nekrasov", "123-onl", "29")
# student2.setGroupNumber("z30-onl")
# student2.getFullName()
# student2.getAge()
# student2.getGroupNumber()

# student3.setNameAge("Kolya", "vishnev", "125-onl", "27")
# student3.setGroupNumber("z47-onl")
# student3.getFullName()
# student3.getAge()
# student3.getGroupNumber()

# student4.setNameAge("vasya", "Pupkin", "130-onl", "21")
# student4.setGroupNumber("z657-onl")
# student4.getFullName()
# student4.getAge()
# student4.getGroupNumber()

# student5.setNameAge("dasha", "yakovina", "114-onl", "19")
# student5.setGroupNumber("Необучаемая")
# student5.getFullName()
# student5.getAge()
# student5.getGroupNumber()


class Product():
    def __init__(self, price, weight, quality):
        self.price = price
        self.weight = weight
        self.quality = quality
        
    def value(self):
        print(f"Шоколад стоит {self.price}")

    def weighing(self):
        print(f"Шоколад весит {self.weight}")

    def assesment(self):
        print(f"Качество {self.quality}")

class Fruits(Product):
    def value(self):
        print(f"Яблоко стоит {self.price}")

    def weighing(self):
        print(f"Яблоко весит {self.weight}")

    def assesment(self):
        print(f"Яблоко качества {self.quality}")


class Vegetables(Product):
    def value(self):
        print(f"Картошка стоит {self.price}")

    def weighing(self):
        print(f"картошка весит {self.weight}")

    def assesment(self):
        print(f"Картошка качества {self.quality}")    

class Nuts(Product):
    def value(self):
        print(f"Миндаль стоит {self.price}")

    def weighing(self):
        print(f"Миндаль весит {self.weight}")

    def assesment(self):
        print(f"Миндаль качества {self.quality}")

    
Chocolate = Product("1.8 BYN", "90g", "High")
Chocolate.value()
Chocolate.weighing()
Chocolate.assesment()

Apple = Fruits("2 BYN", "1kg", "High")

Apple.value()
Apple.weighing()
Apple.assesment()

Potato = Vegetables("3 BYN", "3.5 kg", "High")
Potato.value()
Potato.weighing()
Potato.assesment()

Almonds = Nuts("3 BYN", "3.5 kg", "High")
Almonds.value()
Almonds.weighing()
Almonds.assesment()


