class Person:
    demo="Helo"
    def _init_(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("my name is{}:".format(self.name))
class Employee(Person):
    def _init_(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person._init_(self,name,idnumber)
    def details(self):
         print("my name is{}:".format(self.name))
         print("my name post{}:".format(self.post))
a=Employee()
print(a.__class__.demo)
a._init_("subash",233,45000,"sinor")
a.details()
