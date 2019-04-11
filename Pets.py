# A class that provided the pets name, species and age

class Pet:
    # Constructs a pets name, species and age
    
    def __init__(self, name, species, age):
        self._name = name
        self._species = species
        self._age = age

    # Sets the pets name
    
    def setName(self, name):
        if len(name) > 0:
            self._name = name
            
    # Sets the pets species
    
    def setSpecies(self, species):
        if len(species) > 0:
            self._species = species
    # Sets the pets age
    
    def setAge(self, age):
        self._age = age

    # Returns the pets name
    
    def getName(self):
        return self._name
    
    # Returns the pets species
    
    def getSpecies(self):
        return self._species
    
    # Returns the pets age
    
    def getAge(self):
        return self._age
    
    # Displays the pets name, species and age
    
    def display(self):
        print("%s is a %s who is %d years old." % (self._name, self._species, self._age))

# The program will display the entered pet's name, species and age
        
pet1 = Pet("Chester", "dog", 7)
pet2 = Pet("Dorthy", "cat", 9)
pet3 = Pet("Genie", "fish", 1)

pet1.display()
pet2.display()
pet3.display()



