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
