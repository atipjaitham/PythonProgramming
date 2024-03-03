# Inheritance

# Class features
import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        "initialize attributes to be used in/available .........."
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))
    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now.".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little trired today".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))            
        else:
            print("{} is unconscious!".format(self.firstname))


# Using the class
Greg = Person("Greg","Chouu", 100 ,status=True)
Maria = Person("Maria","Gutierrez", 88 ,status=False)
Kay = Person("Kay","Williams", 50 ,status=True)

print("{} is my friend? {}".format(Maria.firstname,Maria.status))
print("{} is my friend? {}".format(Kay.firstname,Kay.status))

Greg.introduce()
Maria.introduce()
Kay.introduce()

Greg.emote()
Maria.emote()
Kay.emote()

Greg.status_change()
Maria.status_change()
Kay.status_change()


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!")
    
    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -= 5
        print (other.health)

    def insult(self, other):
        if other.health  <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status == False

Alex = Enemy("rock", "Alex", "Wayne", 75, status = False)
Alex.introduce()

Alex.hurt(Maria)
Alex.insult(Greg)
Alex.insult(Kay)
Alex.steal(Kay)   



'''
# Multiple Inheritance
# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku
    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type
    def print_garment(self):
        print("The garment is in section {}, {}. ".format(self.section, self.type))

# Child Class
class Shirts(Item, Garment):
    def __init__(self, sku,section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)
    def print_shirt(self):
        print("{} {} on sale!!".format(self.color, self.name))

Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()
'''