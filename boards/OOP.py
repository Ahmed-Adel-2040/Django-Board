class Human:
    weight = 0
    length = 0
    color = ""
    age = 0

    def walk(self):
        self.age=30
        print("walk")

    def eat(self):
        print("Eat food")


class Doctor(Human):
    clincal="s"
    def examine_Patient(self):
        print("patient")

doc=Doctor()
print(isinstance(doc,Doctor))