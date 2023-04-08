class Staff:
    dept = "operations"
    place = "island"

    def all(self):
        print("I am in", self.dept)
        print("I stay at the", self.place)

Ishmael = Staff()

print(Ishmael.dept)
Ishmael.all()