#create dog class with dog attributes 
class Dog:
    #def init to create in=bject and pass it the arguements to be used as attributes 
    #self is there to be a parameter that holds te newly created object in this case the dog object. The name self is common in programming 
    def __init__(self,name,age,weight):
        #Using the self parameter we can assign the arguments to their proper attribute in the object
        self.name = name
        self.age = age
        self.weight = weight
    #method for dog class to make the dog bark with the proper woof woof     
    def bark(self):
        if self.weight > 29:
            print(self.name, 'says', 'WOOF WOOF')
        else:
            print(self.name, 'says', 'woof woof')
    
    #method for dog class that calculates and print the dogs age in human years
    def human_years(self):
        human_age = int(self.age) * 7
        print(self.name, 'is', human_age, "in human year's")
    



def print_dog(dog):
    print(dog.name + "'s", 'age is', dog.age, 
                            'and weight is', dog.weight)
       
#Notice when using the dog object the d is uppercase to match te class that was created
#Then the attributes are passed to the init function as arguements and assigned to their proper position    
codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)
print_dog(codie)
#Use bark and human_years methods on the codie and jackson objects
codie.human_years()
codie.bark()
print_dog(jackson)
jackson.human_years() 
jackson.bark()
