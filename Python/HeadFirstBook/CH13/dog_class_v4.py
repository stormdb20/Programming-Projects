
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
    
    #method for printing the name passed to the dog class
    def __str__(self):
        return "I'm a dog named " + self.name
        
#Create class that inherits attributes and methods from the first class dog
class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        #set is_working to false
        self.is_working = False
     #method for service_dog class to help handler walk using methods from dog class and service_dog class   
    def walk(self):
        print(self.name, 'is helping their handler', self.handler, 'walk')
       
    #bark method for service dog to print cant bark when is_working = True
    def bark(self):
        if self.is_working:
            
            print(self.name, 'says, "I can\'t bark, I\'m working"')
        else:
            Dog.bark(self)
     

class Frisbee:
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return "I'm a " + self.color + 'frisbee'
    

    
    
    
    
     
       
#Notice when using the dog object the d is uppercase to match the class that was created
#Then the attributes are passed to the init function as arguements and assigned to their proper position    
codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)

#Use bark and human_years methods on the codie and jackson objects
codie.human_years()
codie.bark()

jackson.human_years() 
jackson.bark()

rody = ServiceDog('Rody', 8, 38, 'Joseph')
print("This dog's name is", rody.name)
print("This dog's handler is", rody.handler)
print(codie)
print(jackson)
print(rody)
# bark whil is_working is false
rody.bark()
#Set is_working to True then invoke bark method on rody again
rody.is_working = True
rody.bark()
