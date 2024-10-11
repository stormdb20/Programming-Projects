#create dog class with dog attributes 
class Dog:
    #def init to create in=bject and pass it the arguements to be used as attributes 
    #self is there to be a parameter that holds te newly created object in this case the dog object. The name self is common in programming 
    def __init__(self,name,age,weight):
        #Using the self parameter we can assign the arguments to their proper attribute in the object
        self.name = name
        self.age = age
        self.weight = weight
        
def print_dog(dog):
    print(dog.name + "'s", 'age is', dog.age, 
                            'and weight is', dog.weight)
    
#Notice when using the dog object the d is uppercase to match te class that was created
#Then the attributes are passed to the init function as arguements and assigned to their proper position    
codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 9, 12)
print_dog(codie)
print_dog(jackson)
