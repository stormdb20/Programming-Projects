
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
     
#Class to create frisbee object and give it color and a string methods  
class Frisbee:
    def __init__(self, color):
        self.color = color
    #string method that returns a response
    def __str__(self):
        return "I'm a " + self.color + ' frisbee'
#subclass of dog class for frisbee dog    
class FrisbeeDog(Dog):
#setup the attributes from dog class and making a frisbee attribute setting it to none
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None
    #bark method to overwrite the dog class bark method 
    def bark(self):
        #compare to see if frisbee in dog mouth using not equal
        if self.frisbee != None:
            #print name of dog and string message
            print(self.name, 'Says', "can't bark frisbee in my mouth")
        else:
            #use original dog method from dog class
            Dog.bark(self)
    
    #catch method passing self and frisbee arguments to print string and frisbee color with dog name from the dog and frisbeee classes
    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, 'I caught the ', frisbee.color, 'frisbee')
        
    #method to return the frisbee
    def give(self):
#compare to see if dog has frisbee if it does set self. frisbee to none, print message , and return frisbee
        if self.frisbee != None:
           frisbee = self.frisbee
           self.frisbee = None
           print( self.name, "returns the", frisbee.color, 'frisbee')
           return frisbee
        #return none if dog doesnt have frisbee
        else:
            print(self.name, "doesn't have the frisbee")
            return None
#string method to return string depending on the compare to see if dog has frisbee
    def __str__(self):
        str = "I'm a dog named " + self.name
        if self.frisbee != None:
            str = str + ' and I have a frisbee'
        return str
#function to test the classes and methods for frisbee and frisbeedog classes    
def test_code():
    guy = FrisbeeDog('Guy', 7, 22)
    blue_frisbee = Frisbee('blue')
    print(guy)
    guy.bark()
    guy.catch(blue_frisbee)
    guy.bark()
    print(guy)
    frisbee = guy.give()
    print(frisbee)
    print(guy)
    
test_code()
    
    