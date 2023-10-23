name=input('what is your name? ')

print('Hi ' + name)

Q1=input('What is your name? ')
Q2=input('what is your favorate colour? ')

print(Q1 + ' likes ' + Q2)


#e.g. 
h='"Pyython" is good language'
print(h)

# below shows that a string can have index i.e., if there is the string: course= " Hello world" then course[0] is the 1st character of that  of the string course, so course[0] is the character "H", so if you run print(course[0]) it gives Hello, shown below
course = 'Hello World'
print(course[0])
# here note that blank spaces is also a character, and index starts from 0
# below shows that the -1 index of the string course, is 1st character starting from the right handside of the string so e.g. course[-1] is the chracter d, course[-2] is the character l and so on,
print(course[-1])
# below shows how to extract characters from a string from range
course="hello world"
print(course[0:3])
# here in the above, the code "print(course[0:3])", gets the 0th, 1st and 2nf characters of the "course" string 
print(course[3:])

# here "print(course[0:])" gives the 0th index, then the rest of the index, so 
############## print(course[0:]) gives "o world"
print(course[:])
print(course[:4])
#here print(course[:]) gives all the index and print(course[:4]) gives all the index up and not including the 4th index

another=course[:]

# here "course[:]" gives all the characters in course string

##### challenge 1 start#####
name='Jennifer'
print(name[1:-1])
#question: what would the result be in terminal?
#answer from Aliah: the terminal would could show eJ
# checking if answer is correct: aliah your answer is wrong, the terminal shows "ennife"
# explanation from instructor: note that in print(name[1:-1]), index -1 is the last characters of the string name, so 
#print(name[1:-1]) returns all characters from index 1 so index 1, index 2, index 3 etc, up intil but not including the last chracater which is r, so this returns ennife
a="my name is blue"
print(a[0])

# the float  fucntion converts a string like '198' to a decimal value i.e. 198.0
# example of this shown below:
b='1984'
c=float(b)
print(c)
# here the variable b is a string not a number or integer or a decimal number, but the variable "c" has the variable "b" which is a string, converted to a decimal number so c has value 1980.0 instead of '1980'

# below shows three astrophe ''' used to store long multiline strings in a variable,

space= '''
Hi Aliah,

here is the first email you got,

thanks,
team recruitment

'''

print(space)

course= 'python for beginners'


#### Formatted string: generate text with variables e.g:
first='John'
last='Smith'
 #we want to print the text "John [Smith] is a coder" on the terminal, below is how to do it:
msg=f'{first} [{last}] is a coder'
print(msg)
# the place holder in the string msg=f'{first} [{last}] is a coder' is {first}  and  {last}, 
# and msg=f'{first} [{last}] is a coder' is an exampel of a formatted string
message= first + ' [' + last + '] is a coder'

print(message)

# the method above is not great for long complicated text, its harder to visualize long text on terminal
# formatted strings makes it easier to visualixse the output
###################### String methods ############

course= 'Python for beginners'
## to count the number of characters in a string can use "len()" function e.g. below
print(len(course))
# the len() function is good for user input, as you can assign a length allowed fro user input
# there are functions specific for strings e.g.
course.upper()
# the upper function belongs to strings so is called method
print(course.upper())
# note that upper function does not change the course variable permanently
# i.e. course is still the original value of course
# print(course.lower()) converts all letters in course to lower case

###### to find an index character on a string use find() function e.g.

course= 'Python for beginners'
print(course.find('o'))
#here print(course.find('o')) gives 4, which is the index of the "o" character in the string

print(course.find('m'))
#here print(course.find('m')) gives -1 which means the character "m" is not in the string
# find function is case sensitive, i.e print(course.find('p')) gives -1 as, p is not in string but P is in string
#To get the index aprint(course.find('beginners'))
# here print(course.find('beginners')) gives 11, because the 1st character of "beginners" which is b, is the 11th index of cousrse string
# method to replace a character in a string: use replace() function:
print(course.replace('beginners', 'Beginners'))
# here 1st argument of replace function is the peice of the string character you want to replace, and the 2nd
# argument is the string or character you want to put instead
# note that replace() is case sensitive
# to check if a string is inside another string use "in":
'Python' in course

#the expression "'Python' in course" is boolean expression becuase it returns either Ture or False
print('Python' in course)


######################## Arithmetic Operations ###########


# there two types of numbers intergers (whole number) with "int" sign they have no decimal point, and float numbers which are decimal
#numbers
print(10/3) #division
print(10+3) #addition

print(10 % 3)
print(10**3) # the ** sign is to the power of, so 10**3 gives 1000

#here operator % is the modular sign so 10 % 3 is the value left when we constantly take awa
# away 3 from 10 until we get a whole number less that 3 but greater than or equal to zero

# augmented assignment operators

x=10
x=x+3 # here the value of x starts from 10, then it is incremented by 3 once
print(x)


# augmented assignment operators write the code x=10
# x=x+3 in a shorter form i.e. the operator +=, in x+=3 does the exact same this as
# x=10
#x=x+3 
x=10
x+=3 # here a new value of x is asigned which is the old value of x which is 10 plus 
# 3
print(x)

x=10
x-=3
print(x) # here x-=3 assigns the value of x to value of x minus 3, so the new value of x is 7

################### operator precedence ####


### math function ####

x= 2.9

print(round(x)) # here round() function rounds up the number 2.9 to nearest integer, so
# print(round(x)) gives 3

# abs() function (absolute) always gives the magintude of the number or positive part of the number, so e.g. abs(-245) gives 245

# and abs(245) gives 245

print(abs(-245))

# to use complicated function import math module, use "import math" so you can access functions 
# math module

import math

print(math.ceil(2.9)) #here ceil gives the rounds up 2.9 to whole number, so math.ceil(2.9)
# gives 3, and 3.1 gives 4
#
import math
print(math.ceil(2.9))

print(math.ceil(3.2))

print(math.floor(5.7682)) # floor() function gives the integer part of a number (either whole or decimal)
# so print(math.floor(5,7682)) gives 5
print(math.floor(4.5678856))


##################  if statement ##############

#make decisions based on conditions e.g:

is_hot = False
is_cold=False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold: 
    print("it's a cold day")
else:
    print("Enjoy your day")
#here if is_hot holds boolean value "True" then if statement prints "It's a hot day"
# If is_hot holds value "False" then if statement does not print "It's a hot day"

# elif means 2nd condition
# here, since both is_hot  and is_cold have "False " value then if statement only prints
# the "Enjoy your day"


############### challenge 2 #################

# Price of a house is $1M 
# If buyer has good credit,
# they need to put down 10 percent
# otherwise they need to put down 20%
# print the down payment

#Aliah's solution below:
good_credit=False
hprice=1000000
if good_credit:
    down1=hprice-(0.1*hprice)
    print(down1)
else:
    down2=hprice-(0.2*hprice)
    print(down2)

# Instructors solution
good_credit=True
hprice=1000000
if good_credit:
    down1=0.1*hprice
else:
    down1=0.2*hprice
print(f"Down payment: ${down1}")
################### logical operators ###################


########## date: Thursday 9th feb 2023, time: 7:36pm,
# # the time video Python tutorial was paused at 1:06:15

################### logical operators ###################
# used for multiple conditions in and if statement
# e.g. If applicant has high income AND good credit then Eligible for Loan
# AND  is a logical operator e.g:

has_high_income=False
has_good_credit= False

if has_high_income and has_good_credit:
    print("Eligible for loan")
# both operators must be true

#  logical or operator: e.g  If applicant has high income OR good credit then Eligible for Loan
# AND  is a logical operator e.g:
has_high_income=False
has_good_credit= True

if has_high_income or has_good_credit:
    print("Eligible for loan")
#at least one variable must be True then would print if statement

# NOT is logical operator:
# e.g. if applicant has good credit AND does not have criminal record 
# then ELIGIBLE FOR loan e.g
criminal_rec=True
has_good_credit= True

if has_good_credit and not criminal_rec:
    print("Eligible for loan")


# here as criminal_rec holds True value, then not criminal_rec means criminal_rec should hold False values in order for the
# if statement to print 


# Comparison Operator e.g
# if temperature is greater than 30, its a hot day,
# otherwise if it's less than 10, its a cold day,
# otherwise it's neither hot nor cold. If statement of this shown below:

Temperature = 20

if Temperature>30:
    print("it's a hot day")
elif Temperature<10:
    print("it's a cold day")
else: 
    print("it's neither hot nor cold ")

#e.g: if name is less than 3 characters long, then name must be at least 3 charachters long,
# otherwise if it's more than 50 characters then name can be a mamaximum of 50 characters
# otherwise name looks good
name="g"

if len(name)<3:
    print("name must be atleast 3 characters long")
elif len(name)>50:
    print("name must not exceed 50 characters")
else:
    print("name looks good")
#########################  project weight converter  ##################

# allow user to enter thier weight in kilograms or pounds, then convert that weight to the other unit.


### while loops 
###### used to execute a block of codes multiple times

# while condition: # as long as the this condition is true, the code belowwould be 
# executed
    ......
i=1
while i<=5:
    print(i)
    i+=1
print("Done")

guess_1=input("Guess: ")
guess_2=input("Guess: ")
guess_3=input("Guess: ")
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
      if guess_1==secret_number:
        print("Your guess is correct.")
      elif guess_2==secret_number:
        print("Your guess is correct.")
      if guess_3==secret_number:
        print("Your guess is correct.")
      else:
        print("Sorry you failed")
    guess_count= guess_count+1


    
      








    












 








