

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
    
    #method for dog to walk
    def walk(self):
        print(self.name, 'is walking')
    
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
        #check if working to see if to use regular walk or service walk
        if self.is_working:
            print(self.name, 'is helping their handler', self.handler, 'walk')
        else:
            Dog.walk(self)
       
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
    
    #walk method for frisbee dog to check if playing frisbee and to make the proper walk action
    def walk(self):
        if self.frisbee != None:
            print(self.name, "says I can't walk i'm playing frisbee")
        else:
            Dog.walk(self)
            
    
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

#Claas for dog hotel with check in and out methods
class Hotel:
#Name attribute for the hotel that is passed when hotel is instaniated and create dictionary for dog objects with dog objects as the key
    def __init__(self, name):
        self.name = name
        self.kennel = {}
#check in method passing self and dog     
    def check_in(self, dog):
#compare to make sure it is a dog object then add dog object to the dictionary with dog name as key with messages for both outcomes
        if isinstance(dog, Dog):
            self.kennel[dog.name] = dog
            print(dog.name, 'is checked into', self.name)
        else:
            print('Sorry only dogs are allowed in', self.name)
#method to check out that compares name arguement with dictionary and deletes the entry from the dictionary if the compare is true 
    def check_out(self, name):
        if name in self.kennel:
            dog = self.kennel[name]
         #print message, del dog from dictionary, and return dog object
            print(dog.name, 'is checked out of', self.name)
            del self.kennel[dog.name]
            return dog
        #print and return None for dogs
        print('Sorry', name, 'is not boarding at', self.name)
        return None
    #method for letting the dogs bark by checking through all the dogs in the kennel dictionary and call the bark method for them
    def barktime(self):
        for dog_name in self.kennel:
            dog = self.kennel[dog_name]
            dog.bark()

    #method to walk all the dogs in the kennel by delegating the job to the hired walker
    def walking_service(self):
        if self.walker != None:
            self.walker.walk_the_dogs(self.kennel)
        
        #for dog_name in self.kennel:
            #dog = self.kennel[dog_name]
            #dog.walk()
            
    #method for hiring dog ealker by checking if the instaniated object is a dogwalker object
    def  hire_walker(self, walker):
        if isinstance(walker, DogWalker):
            self.walker = walker
        else:
            print('Good try', walker.name, "ain't no damn dog walka")
                    
    
            
#person class that creates person objects and returns string
class Human:
    def __init__(self, name):
        self.name = name
    #method that returns string message
    def __str__(self):
        return "Hello i'm a human and my name is " + self.name
    
#sub class of human for dogwalker wwith method for walking dogs
class DogWalker(Human):
    def __init__(self, name):
        Human.__init__(self, name)
    #method to iterate through the dogs and call the walk method on them 
    def walk_the_dogs(self, dogs):
        for dog_name in dogs:
            dogs[dog_name].walk()


#cat class with self and name arguements and a meow method        
class Cat:
    def __init__(self, name):
        self.name = name
        
    def meow(self):
        print(self.name, 'says Meow')


                    
        

#function to test the classes and methods for hotel and cat classes    
def test_code():
    #create dogs and cat object
    cody = Dog('Codie', 12, 38)
    jackson = Dog('Jackson', 9, 12)
    tommy = Dog('Tommy', 7, 20)
    rody = ServiceDog('Rody', 8, 38, 'Joseph')
    rody.is_working = True
    #frisbee = Frisbee('blue')
    guy = FrisbeeDog('Guy', 7, 22)
    #guy.catch(frisbee)
    hotel = Hotel('Doggie Hotel')
    hotel.check_in(cody)
    hotel.check_in(jackson)
    hotel.check_in(tommy)
    hotel.check_in(rody)
    hotel.check_in(guy)
    #create dog walker and hire them
    joe = DogWalker('Joe')
    hotel.hire_walker(joe)
    #delegate the responsibility to joe
    hotel.walking_service()
    
    
test_code()
    
    