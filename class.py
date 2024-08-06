class Person:
    def __init__(self, name, age, gender, city):
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        
    def hello(self):
        print("hello people!")
        
    def in_fifty_years(self):
        new_age = self.age + 50
        print(f"In fifty years I'm going to be {new_age} years old")
        
    def __str__(self):
        return f"Hi my name is {self.name}, my age is: {self.age}, I'm {self.gender}, from {self.city}. Nice to meet you!"

class Student(Person):
    def __init__(self, name, age, gender, city, grade_class, avg_score):
        super().__init__(name, age, gender, city)
        self.grade_class = grade_class
        self.avg_score= avg_score
    
    def angry(self):
        print("Studying is so hard")
    
    


guy = Person(name="guy guzman",age=26,gender="male",city="Ramat gan")
waga = Student("waga",20,"female","baga","יא",90)

print(guy.angry())
# print(waga)