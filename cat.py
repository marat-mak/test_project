class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def get_name(self):
        return self.name
    def get_gender(self):
        return self.gender
    def get_age(self):
        if self.age >= 5:
            return self.age, 'лет'
        else:
            return self.age, 'года'
class Dog(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
    def get_pet(self):
       return f'{self.name}  {self.age}'
    def __repr__(self):
       return f'{self.name}  {self.age}'

cat_1 = Cat('Котофей', 'boy', 5)
cat_2 = Cat('Нера','girl',3)
dog_1 = Dog('Barbos','boy',7)
print(cat_1.get_name(), cat_1.get_gender(), cat_1.get_age())
print(cat_2.get_name(),cat_2.get_gender(),cat_2.get_age())
print(dog_1.get_pet())
print(dog_1)
print(dog_1.get_gender())