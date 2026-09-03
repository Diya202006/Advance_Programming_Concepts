class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Puppy(Dog):
    def play(self):
        print("Puppy plays with a ball")
 
obj = Puppy()

obj.eat()
obj.bark()
obj.play()