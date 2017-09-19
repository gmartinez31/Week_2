#1 Basics
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
    def add_friend(self, friends):
        self.friends.append(friends)
    def num_friend(self):
        print(len(self.friends))    
    def greet(self, other_person):
        self.greeting_count += 1
        print(self.greeting_count)
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
    def print_contanct_info(self):
        print("{}'s email: {}, {}'s phone number: {}".format(self, self.email, self, self.phone))
    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)


#variable sonny, which is also our obj, is equal to the class: Person with the following 3 parameters.
sonny = Person('Sonny','sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

#so obj.function in class is also
#class.function being executed(arg or parameter)
sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.email)
print(sonny.phone)
print(jordan.name, jordan.email, jordan.phone)
jordan.add_friend(sonny)
jordan.num_friend()
sonny.greeting_count
print(sonny)

############################################################################################################################################################## 

#2 Make your own class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print(self.year, self.make, self.model)
momscar = Vehicle('Chevy', '1500', '95')
momscar.print_info()