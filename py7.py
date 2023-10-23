################## Constructors ########### 


###  we can create an object with out its with out an x nd y cppr


# constructor is a function that gets called when creating an object 


### creating  class called "Sandwich"

class Sandwich:
    def test(self):
        print("how are you?")
    x=1
## now creating an object called "bread" from the class called "Sandwich":

bread=Sandwich()
bread.x=100
print(bread.x)

# here we get an "Attribute Error" which says that the "Sandwich" class deos not contain the variable 
##  "mayo", to add "variable "mayo" into the object "bread", need to do this:
## to fix this:
#bread.mayo=10
#print(bread.mayo)
##### prroblem,

#can create point object with "x" and y coordinate, i.e. it does not contain x or y variables
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point=Point()
print(point.x) # when running this line of code we get and "AttributeError", which says point "Point" object has
# no attribute x, which means the object "point" does not contain variable x

### so we can have an object of class "Point", that does not contain the "x" and "y" variable, 
## but we need all objects of the class point "Point" to at least contain the "x" and "y" variables,
#  and those "x" and "y" variables will have a starting value,
### to fix this, we use a constructor
### a constructor is a function which is called when creating an object:
# we want the object to have varibale x and y, and putt them in the function
#i.e., get point=Point(10,20), where "10" is x value, and "20" is y value


## to do this:


### 
class Point:
    def __init__(self,x,y): ## here function called  "_init_" is being created
        self.x=x # here x in "self.x" is a variable so here "x" cannot be 10
        self.y=y # and x on the right hand side of self.x=x is a parameter which means it can be a constant and/or can take a value like 10 etc,
## here "self" is a reference to the current object
    def move(self):
        print("move")
    def draw(self):
        print("draw")
## the function "_init_" is called a constructor it is used to create an object
#now:
point=Point(10, 20) # here what happens, is that the 2nd and 3rd argument in
## in any function of in the class "_init_"has value "10" and "20" repspectively,

print(point.x)


## Challenge
# define class called person, it should contain name variable and also a talk function (called method)
##
class Person:
    def __init__(self, name): ## here the init function has double underscore on both sides.
        self.name=name
    def talk(self):
        print("How are you?")

person1=Person("Aliah")
print(person1.name)
# 
#now: lets try

class Person:
    def __init__(self, name): ## here the init function has double underscore on both sides.
        self.name=name
    def talk(self):
        print("Hi, I am",self.name) # or you can write "print(f"Hi, I am {self.name}")"

person1=Person("Aliah")
person1.talk()
# creating another Person object

bob=Person("Bob")
bob.talk()





## every function in a class must have an argument called self, which is a reference to the current object, i.e. it represents the current object

# #here the 1st argument of the function "Point()" is the name of the object of Point which is point,
# and that argument is also the fisrt argument of  the functions "move" and "draw " in the class called "Point".
# now, point=Point(10) , here 10 is the 2nd argument, and if there is any function in the class called "point" that has a 2nd argument then 10 would equal the sencond argument of that function, so e.g.
#### 


#### inheritence ######

# inheritence is a method for reusing code, it can be used for more than one language.
## see how inheritence work:
## suppose we have created a class called " Dog" shown below:
class Dog:
    def walk(self):
        print("walk")  

## lets say  we needs 10 lines of code under the "walk" function:, what
# if in future we want to define another class lets say "Cat"
# and we want to add the walk function inside it, but we would need to also add 10 line of code, to create the walk function, tnhis is bad technique,7
## to fix this:
# use inheritence:
# define a new class called "mamo" and move the "walk()" function into that class, then the "dog" and "cat" classes, takes (or inherit) the "walk" function from thier parent class called "Mamo".
## this is shown below:

class Mammal:
    def walk(self):
        print("walk")  

class Dog(Mammal): # here the class called "Dog" will take in (inherit)" all the functions (and maybe variables) in the "Mammal" class
     pass # here "pass" tells python to do nothing, which this the class "Dog" is not an empty class
## we can add a fucntion to the Dog class, that is only in Dog class, and then we do not need to put in the the pass statment, as thier is 
# already something there so e.g.
class Dog(Mammal): # here the class called "Dog" will take in (inherit)" all the functions (and maybe variables) in the "Mammal" class
     def bark(self):
         print("bark")
         
 # here "pass" tells python to do nothing, which this the class "Dog" is not an empty class
## we can add a fucntion to the Dog c
class Cat(): # but here the is red wiggly line under keyword class, this is because python does not like empty class, because the "Dog" class deos not have anything under it, to fix this write "pass" statement under the 
    # class called "Dog"
    def walk(self):
        print("walk") 

# NOW CAN DO:
class Cat(Mammal): # but here the is red wiggly line under keyword class, this is because python does not like empty class, because the "Dog" class deos not have anything under it, to fix this write "pass" statement under the 
    # class called "Dog"
    pass

#now can create object of say Dog class:

dog1=Dog()
dog1.walk()

################## Modules ###### 


# A Module is a file with some python code,
# # use modules to organise code into multiple files,
# just like sections in a supermarket, when going to a supermarketing, thetere different sections like food, clothes, skincare products etc.


### instead of writing all class and functions and code in one python file,
## we want to braek upt the code in one orginal python file, into multiple files,
# i.e. we want to create multiple files, where each file contains a section of the code in the orginal file:

# each file is a module, this gives a better structore to the code, and allows section of the code to be reused:
# consider the file py71.py, here created two functions called "lbs_to_kg" and 
# "kg_to_lbs", we want to create two files (i.e. two modules), where one file contains the "lbs_to_kg" function and the
# other file contains the  "kg_to_lbs" function.
# then in a programming use code in any of the module, into any programme.
## check how this is done in py71.py file
### 


##### paused on 3:22:18 #################################


### challenge###
## here creating function called findmax, which takes an array of whole numbers, and then gives out the largest number in that array

import util


from util import findmax
findmax([1,2])


### or you can do this way:
import util

###################### packages #####################
# packages are another way to organise code

## real project can contain hundred or thousand of modules (files containing code)
# we do not want to add all those modules under the main file, because overtime, the main file or directory is going to bloated
# with alot of files,

## to fix this need to create package where each package contain related modules, 
# # A package is a folder (or directory) that contains multiple modules
## so under project file, can create a folder (directory), that contains miltiple module (file).


# below shows how to create news packages in python

## how to import a function from module (file) called "shipping.py",
# we cannot use the file "shipping.py" directly because it is inside another file in project "Python 2023" which is "ecommerce.py", so need to do this:
# to ways to import the module "shipping.py"
## one way is import entire module:
import ecommerce.shipping
ecommerce.shipping.calc_shipping()


# another way is import the function from module "shipping"

from ecommerce.shipping import calc_shipping

calc_shipping()

# if want to import mulfiple functions fromshipping, can do this:

from ecommerce.shipping import calc_shipping, cal_1 # here cal_1 can be another function in shipping file
# or import entire module, then acces all funcytion and classies:

# to import the entire shipping module, we do:
from ecommerce import shipping

shipping.calc_shipping



### generating random values #######

# built in modules in python, python contains libraries contaisn several modules for common task like,
# sending emails, generating randoms values, working with date and time:, we do not have to code from scratch:

### builtin module for generating random values :
# since random is already in python, then do not need the file "random.py" under the project file, because python already knows that
# random is a module file, because it already exists in python:

import random
for i in range(3):
    print(random.random()) # here random.random() (random() is a function which gives random value between 0 and 1, and random is a file containing the function random())

## what we want random value between 10 to 20 then we do:

import random
for i in range(3):
    print(random.randint(10,20))

    ## another function that can randomly pick a number from a list of numbers:
# to do this:
import random
members=["al", "red", "blue"]
leader=random.choice(members) # the choice() function randomly picks an element from a list of elements
print(leader)

## create a function that roles two dice and gives the numbers at the top of two dices like this (x,y)
# but  define class called dice, and in class "dice" there is a method (function) called roll(), every time we call the method
#"roll()" we get a tupple, a tupple is a list of values that we cannot cha ge we cannot add or remover values from it, nor can we change it.

import random
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return (first, second) # this (first, second) is called a tuple in python, we do not need to add round brackets we
    # just have "first, second", 

    
dice=Dice()
print(dice.roll())



################ files and directories '#########

############# working with directories #########

# python contains a module called "pathlib", which contains classes, that can used to create objects of those classes also it has "object-oriented file system paths" this means it can provide classes that we can use to create object:
# here the class name has a capital letter at the beginning of the name:
#### 
#below we are getting the Path class from the "pathlib" file (module)
from pathlib import Path
# now need to create a "Path" object to reference a file or directory in a computer:
# i.e. it would represent a file or directory in a computer i.e. the object of path would represent a file or directory in a computer
# there are two ways which are:
#Absolute path
#Relative path  
# Relative path which means a path starting from the current directory,
# e.g. want tor egeference ecommerce directory can use "relative path", because eccomerce is in the 
# the current project called "Python 2023" that we are currently in:

# Absolute paths is a path to the file we want that starts from the root of hard disk disk
# e.g. in windows if we have the disk c drive , then program files etc, so the absolute path would be:
# c:\Program Files\Microsoft , here Program files and Microsoft are directories (folders).
### work with relative paths now:
#Path() # the Path class contains function which gives a string of characketers that are used to get to a file, or shows python where a file is:
# ifwe do not put an argument in Path() then it would give a path (string of files, disk and characters, which tells us the location of a folder or file) to the current folder (difrectory)


#path=Path("ecommerce") #here "ecommerce" is a file
# we can check if a path object exists by typing:
#print(path.exists())

# if we put a file in "Path()" that does not exist then print(path.exists())
# would give false because that file or folder does not exist
# find
## we can create a directory or folder by using "mkdir" function so e.g:
#path1=Path("emails")
#print(path1.exist())
# now when we run "path1=Path("emails") and print(path1.exist) it gives "false" in terminal, because "email" file or folder does not exist in python,
# so to create email file , we use function "mkdir". this is shown below
#path1=Path("emails")
#print(path1.mkdir())
## we can delete a folder (directory) or file, by doing the below:

# so to create email file , we use function "mkdir". this is shown below
#path1=Path("emails")
#print(path1.rmdir()) # here rmdir stands for "remove directory" and "mkdir" stands for "make directory"

## we can iterate (go through) each file (module) in a directory (folder), open them
#To do this we do:

#path=Path() # path object contains a path to the current folder (directory) which is "Python 2023"

#print(path.glob('*')) #here the object "path" has a function called
# "glob", this function we can search for files and directories in current path (object)
# also "*" in "glob("*")" means get all files and all fodlers (directories) in the path of the current folder that we are in (and this path is in object path):
# we can use an extension which tels what type of file or folder we want so we can do 
#"glob("*.*")" the "*" after the dot . , means that get all types of files (but not folders or directories, because it has an extension, and folders dont have extension), so e.g. 
# a python file, or video file or image file etc . # also can search for all "python" files or "excel" files
# by typing in "glob("*.py") or "glob("*.xls") respectively.

# lets search for all "python files" in our current directory (folder) which is "Python 2023"

path=Path() # path object contains a path to the current folder (directory) which is "Python 2023"

#print(path.glob('*.py')) 
 # when we run the above "line 336" and line 338, we get "generator object Path.glob at
# 0x000001D35F938EB0" 

# genereator object is an advanced topic and beyond the scope of beginners scoope of course
# we can iterate or loop through generator objects so:

#for file in path.glob('*.py'): #here "path.glob('*.py')" is a generator object
    #print(file)

# we can get all folders (directories) and files in our current folder called "Pyhton 2023" by doing:

for file in path.glob('*'): #here "path.glob('*.py')" is a generator object
    print(file)


################### pypi and pip #############



###### paused on automation with python project 1 #####




