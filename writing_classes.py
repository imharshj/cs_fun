# Writing classes

# First some work with scopes and namespaces
def scope_test():
    def do_local():
        spam = "local spam"
        print ("Printing non-local value of spam: ", spam)

    # Not available in Python 2.x
    # def do_nonlocal():
    #     nolocal spam
    #     spam = "nonlocal_spam"


    def do_global():
        global spam
        spam = "global_spam"

    spam = "test_spam"

    print("Before local assignment: ", spam)
    do_local()
    print("After local assignment: ", spam)
    #do_nonlocal()
    # print("After nonlocal assignment: ", spam)
    do_global()
    print("After global assignment: ", spam)

scope_test()
print("In global scope: ", spam)


# Class definition
class TvShows:
    """
    Simple class example

    Statements inside classes are usually function def
    Class objects support two types of operations:
        - Attribute references and Instantiation

    Two kinds of valid attribute references
        Data attributes (variables) and methods

    """


    def __init__(self, name):
        """This is a TV Shows class.\n"""
        self.name = name
        self.attributes = {"name": self.name, "genre": None, "location": None, "runtime": None, "seasons": None}


    def genre(self, genre):
        all_genre = ['drama', 'comedy', 'thriller', 'sitcom', 'talkshow']
        if genre in all_genre:
            print (self.name + " is a " + genre + "!")
            self.attributes["genre"] = genre
        else:
            print("Sorry this is not a valid genre. Please try one of the following: ")
            print all_genre


    def show_loc(self, city):
        self.attributes["location"] = city

        
    def runtime(self):
        show_runtime = 60 if self.attributes["genre"] == 'drama' or self.attributes["genre"] is None else 30
        self.attributes["runtime"] = show_runtime


    def showonair(self, s):
        self.attributes["seasons"] = s


# Testing w/ Inputs

# Built in Class methods
print("Class documentation: " + TvShows.__doc__)

# Instantiate some objects using the class definition
sienfeld = TvShows("Seinfeld")
friends = TvShows("Friends")
satc = TvShows("Sex and the City")
himym = TvShows("How I met your mother")
suits = TvShows("Suits")

# Call the name from the __init__ method
print(sienfeld.name)
print(friends.name)
print(satc.name)
print(himym.name)
print(suits.name)

# Assigning attributes to each instance of the class
sienfeld.genre('comedy')
friends.show_loc('New York City')
himym.showonair(9)
suits.genre('drama')
suits.runtime()

# Check to see each class has attributes as assigned
print(himym.attributes)
print(friends.attributes)
print(sienfeld.attributes)
print(suits.attributes)

# Instantiate a new object with no attributes
td = TvShows("True Detective")
print(td.attributes)
