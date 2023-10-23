########### return statement ##########

### keyword arguments come after positional argument:e.g:
# greet_user("john", last_name="smith")
# if keyword argument is used before positional argument then an error is
# given

################### return statements ##################

# how to create function that return values 

def square(number):
    return number*number # this "return" statment returns something from a function
# allods the square function to have a value, so "square(3)" has value 9
  
square(3) # 

print(square(3))
# what happens if the "return" statement is not in the square function?
# and the print square(3), what would happen?
def square(number):
    number*number # this "return" statment returns something from a function
# allods the square function to have a value, so "square(3)" has value 9
# 

print(square(3))
# here we get "none", if a function does not have return statement returns "none".


################ creating reusable functions #################
 ## this gives way for the user to input some text or numbers etc
def char_text_converter(message1): # here a function is being created
    words=message1.split(' ')  # here the text "message" is being cut up wheneevr the is a space " ", i.e. whenever there is a space
    # " " in message1, then split function will cut the text message at that point, so e.g.
 # message1= How are you ? , then split function cuts up the text meassage 1, at places where 
 # " " is located so message1.split(' ') gives 4 peices which are "How", "are", "you" and "?"
 # but then it puts these peices in a list, so message1.split(' ') gives:
 #      ["How", "are", "you", "?"]
    char_text={
        ":)": "happy",
        ":(": "sad"
    }
    # here char_text is a 
    output="" ### here "output" has an empty character, so "" is nothing
    for word in words: # "words" is a list or pieces from messages1
        output += char_text.get(word,word) + " " #here char_text.get(word,word) has value of the
        # key variable word in :): happy
    return output

message=input(">") 
print(char_text_converter(message))


    
################# Exeption ###############


## handling errors
try: 
   age = int(input('Age: '))
   print(age)        # try running these two lines of code
except ValueError: # if you encounter "Value error", then programme print "Invalid value"
    print("Invalid value") 
# this prevents programme crashing

#"if you encounter"
# exeption is kind oferror that crashes programme
# if we type a text in input it gives error:
# exit code 1 means programme crashed


### handling different errosrs

try: 
   age = int(input('Age: '))
   income=20000
   risk=income/age   # try running these two lines of code
except ValueError: # if you encounter "Value error", then programme print "Invalid value"
    print("Invalid value") 

# the above gives zero div error, but the above code cannot catch "Value error"
#  value error:
# so let the above rror also catch "ZerDev Error" the code velow is cretaed:

try: 
   age = int(input('Age: '))
   income=20000
   risk=income/age
except ZeroDivisionError:
    print("Age cannot be zero")  # try running these two lines of code
except ValueError: # if you encounter "Value error", then programme print "Invalid value"
    print("Invalid value") 

# comments
################# classes ######

################## paused 3:00:00 ######
# classes are ised to define new types, e.g. 
# basic types in python such as numbers, strings and booleans, there are other types
# such as lists and dictionary there is another type called "point",
# class Point # pascals naming convention, where you the first letter of every 
# word is a capital letter.

class Point: #104
    def move(self):
        print("move")


    def draw(self):
        print("draw") # 105
# from new line 104 to line 105, the class creates a new type which is "Point",
# and with in the point there is new objects which are the two functions "move" and "draw"
# a class is a template where objects are created.

point1=Point()
point1.draw

# object is created 

point1.x=10 # x coordinate of point1 is 10
point1.y= 40  # y coordinate of point1 is 40, here the value must be a number , it must not be a text or string
print(point1.x)

point2=Point() # this is an object of the class called "Point".

################### constructors ########################

point=Point() # here "point" is an object

print(point)

# when we run this programme, thre is an attribute error which says "Point" Object has no attribute "x" "
# 
 
# object is a collection of variables and/or functions, the object can represent
# anything e.g. a person, a robot or a pet.

# variables such as e.g. height, age, x coordinate etc, are called attributes,
# methods


# class is like a template to create objects.
# class is like a template or a "application" form e.g, where the attributes
# # have no value, but to create object you need to give a vlaue to the attributes, 
#  it is like, e.g the "LLoyds job application form is a "class", and the name of the class is
# called "LLoyds bank job application form", and the objects are the job applicants who fill the form in,
# # e.g the jobs applicants say ellen, racheal each fill the "Lloyds job form", so they are objects, and thier attributes are in thier
# form, 


x=56
L=[2,5]

M={
    "w": "wed",
    "m": "mon" 
}
    
# Here "Numbers", "Strings", and "Booleans" and "lists",
""

 















