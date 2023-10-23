#Defining or creating dictionaries in python

# Name: John Smith
# Email: john@gmail.com
# Phone: 1234

# here, "Name", "Email" and "Phone" each are called "Key", and "John Smith"
# john@gmail.com, and 1234 are values paired with those keys, also 
#"Name: John Smith" is called a key value pair.

# Dictictionary is something that stores key value pairs.

# below shows how to create dictionary
customer={
   "name":"John Smith",
   "age":30, 
   "is_verified":True
}
# note that, the keys have to be unique in a dictionary, so not same keys in a ductionary,
# value assigned to key can by anything,

# To get each item in the dictionary, need to use square brackets,
#customer["name"] # here "name" is the key in dictionary customer, this gives the value
#assigned to the key "name" which is "John Smith", so 
# print(customer["name"]) gives output "John Smith"
#print(customer["name"])


# what if we put something in the square bracket in customer[], such that it is
# not a key in the customer dictionary?, then if we run the below:
#print(customer["birthdate"])
# then is gives "KeyError: 'birthdate'" in the terminal because "birthdate"
#is not a key in customer dictionary.
# # Also, keys are case sensative, so print(customer["Name"]) gives an error.

# To fix this, can use get method,shown below:
#print(customer.get("birthdate"))
# this gives "None" in terminal, which is a object which represents the abscenec of a value,
# Also, if a variable inside square bracket of "customer[]" is not a key in customer,
# we can assign a defalt value to to it, e.g. 

#print(customer.get("birthdate", "Jan 1 1980"))
# you can change the value that is paired with the key in a dictionary, shown below:
#customer["name"]="Jack Smith"
#print(customer["name"])
# This gives "Jack Smith" in the terminal, hence value of the key "name" changed from 
#"John Smith" to "Jack Smith",

# Also we can create a new key value pair in a dictionary called customer, shown below:
customer["Birthdate"]="13 Dec 1997"
# so now we can check if the key value pair "Birthdate": "13 Dec 1997" exits in customer:
print(customer["Birthdate"])
# yes it does, in terminal it gives "13 Dec 1997".

########################## challenge py6.1########
## the program asks for phone number 
# phone:    
# then after putting phone number in , the programm puts each number in the phone
# number as words, this is given in terminal, so if the phone number input was "1234", then program gives "
# one two thre four" in terminal.

numbers={
    "0": "Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}


def num_word_convert(message1):
   output=""
   for num in message1:
       output += numbers.get(num, "!") + " "
   return output


message=input("Phone: ")


print(num_word_convert(message))
## better solution:

phone=input("Phone: ")
numbers={
    "0": "Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output=""
for num in phone:
    output += numbers.get(num, "!") + " "
print(output)
    

######################## paused at 2:26:31 ### on python prgramming video,,

### Challenge emoji converter:

## if input is  I am sad , then output should be I am :(.
message=input("How are you ? : ")
emotion_char={
    "happy":":)",
    "sad":":(",
    "shocked": ":o",
}

message_split=message.split(" ")
output=""
for word in message_split:
    output+= emotion_char.get(word,word) +" "
print(output)



################# functions ###############

##by default all functions return value "none" ( which means nothing)

############# paused on 2:54:00


############## How to handle errors in python programmes #######
### 
age= int(input("Age: ")) # here the "int()" function converts the value of "
# " input("Age: ")" into a whole number, because in python input("Age: ") is considered as a
#  string not a number 
print(age)

# when running line 137 and 140 there is message in terminal which says
#'### " Process finished with exit code 0" which means the programme ran sucessfully there 
## were no errors.
### but what if we run line 137 and 140, but in the input function, but a non numerical value 
## like a text, then we get the following error message in terminal:
### "ValueError: invalid literal for int() with base 10: 'Hi' "
## this means 'Hi' does not contain whole number that can be converted to an interger.
### in terminal it says "shed with exit code 1", here "exit code 1" means the programme crashed
## because there were errors.


### look at the type of error which is "ValueError" :

#### lets see how to handle this:
### In python there is a construct called "try except", we use this to handle errors.
# below shows how this is used to handle errors.
try:
    age= int(input("Age: "))
    print(age) ### here is what the computer should run through
except ValueError: # below this statement is what message or what should computer do
    # when it finds a "ValueError" in the programme in line 159 and 160 
    #also in line 161 "ValueError" is the type of error the computer may find when 
    ### running through  line 159 and 160
    print('Invalid value')
# In python an "exception Error" is a type of error that can crash a programme, i.e. stops the computer from
# the task .
## when you run line 158 to 165, and give a text or non numerical value, in 
## in input value, then in terminal is says " exit code 0", which means programme has not crashed, or got messed up,
##
### 
### can handle different kind of errors:
#e.g.

try:
    age= int(input("Age: "))
    income=20000
    risk=income/age
    print(age) 
except ValueError: 
    print('Invalid value')

# lets run line 175 to 181, and put age as 0, then we get the "ZeroDivisionError", which
# because there is  "risk=income/age" in line 178, and if age=0, then "risk=income/age"
# cannot have value because we cannot divide any number by zero.

### how to handle both "ValueError" and "ZeroDivisionError"
try:
    age= int(input("Age: "))
    income=20000
    risk=income/age
    print(age) 
except ValueError: 
    print('Invalid value')
except ZeroDivisionError:
    print("Age cannot be 0.")

######## classes


####   e.g. the classs we want to create is called robot
 # and it has 3 varables or characteristsics like name color weight,
 # contains a function, when the function is run prints ut my name in "name".

 ### from the class called "Robot", we want to create objects, 
 # that contain the same variables as the class called robot "robot", but those variables are assigned a value,
 # so the variabl "name" in class "robot has not value assigned to it, but in the object called "object 1", the variable "name" has 
 # value "Aliah", and so on,

 ## Class is a collection of varibiales, sush as age , name, height, colout etc,
 # that are not assigned to any value, and class can contain functions.
 # from the class called "robot", an object of a class is a collection of all variables and functions
 # from the class "robot", but a value is assigned to the variables, so e.g an object of class "robot" contains variable "age " which would have a value such as 24,
 # but in the class "robot", age does not have a value
 # a variable can be assigned to an object.



 ### how to create a class "robot" and two objects#######

### How to create class "robot" ####
class Robot:
    def introduce_self(self): #here creating a function called "intrduce_self"
        print("My name is ",self.name)

# here since the function introdice_self is within the class
## called Robot, then then you need to put an argument in the bracket
# introdice_self() which is going to be the name of the object created from the class "Robot".
# so in this case the argument in bracket of introdice_self() is "self", which would represent the
# name of an object, then in the function "self.name" is the value of variable "name" that is in the
# object called "self". Also "self.weight" would the value of "weight" in the object called "self"
## etc.
### how to create and object out of the class " Robot" 
r1=Robot()
# to add variables (and assigne a value to them) into the object called "r1"
r1.name="Tom"
r1.weight=56
r1.color="blue" # this says create new object using class Robot
# to include a function into object "r1", (which uses variables and/or function from r1 object) you need to type:
### How to create class "robot" ####
class Robot:
    def introduce_self(self):
        print("My name is",self.name)
r1=Robot()
## below I am adding variables in the object "r1"
r1.name="Aliah"
r1.introduce_self()


