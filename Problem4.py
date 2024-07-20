class Person:
    def __init__(self,name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return f"Name: {self.name}, age: {self.age}"
    
    def work(self) -> str:
        return 'Biror ish qiladi.'

class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str) -> None:
        super().__init__(name, age)
        self.subject = subject

    def work(self) -> str:
        return "Dars beradi."
    
class Student(Person):
    def __init__(self, name: str, age: int, grade: int) -> None:
        super().__init__(name, age)
        self.grade = grade

    def work(self) -> str:
        return "Ta'lim oladi."

person = Person("Firdavs",16)
print(person.get_info())

person = Teacher("Aziz",30,"Go")
print(person.work())

person = Student("Anvar",24,5)
print(person.work())