 # for loop iterate over items in a collection e.g
# then do somthing to each item

for item  in 'Python': 
    print(item)
    
            # here "item" is the "loop"
                               # where it says "for item  in 'Python': "
                               #here "item" variable will hold each character in the string
                               # 'Python'   

prices=[20,10,30] 
total=0 # want to calculate the sum of the whole numbers (which are prices) in the "prices" array
for price in prices:
    total+=price
print("total= ", total)
# total=20
# total=30
#total=60

########## nested loop  - adding one loop inside another loop  ###########
### using nested loop can easily generate list of coordinates coordinate (x,y)

# e.g want to generate list of coordinates which is: (x,y), (0,0)
# (0,1), (0,2), (1,0), (1,1), (1,2)

for x in range(2):
    for y in range(3):
        print(f'({x},{y})')


# creating a x pattern e.g.  
# xxxxx
# xx
# xxxxx
# xx
# xx

for x in [1,2,3,4,5]:
    print(x*" x")
# above code is corrrect


# challenge write a program to find a largest number in a list

def large_num(A):
    current_val=0
    for i in range(len(A)):
         if current_val < A[i]:
             current_val=A[i]
    print(current_val)
    return current_val

large_num([0,1,8,908,6])
            

# 2:00:00
######################### 2D list #######################

# e.g matrix, can create matrix using 2D list, which

 # within a list there is another list, so matrix is written as:

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ]
# here, all elements including yellow brackets forms a list, and each element 
# is a list, so this is a 2D list, which is a list containg lists as it's elements.
print(matrix)

# matrix[0] returns the 1st item in the whole list containing yellow brackets,
# so  matrix[0]  gives [1,2,3].
# Also, matrix[0][1] gives item with 1st index in the list [1,2,3].
# so matrix[i][j] gives the jth indexed item in the list that is the ith index of the list with
# yellow brackets

# you can change item in matrix by e.g
matrix[0][1]=35
print(matrix)

# can use nested loops i.e. loop within a loop: e.g.
matrix=[
    [1,2,3],
    [4,4729,6],
    [7,5,9]
 ]

for row in matrix: # here, takes in each element in the list with yellow brackets
    for item in row:  
        print(item)


################## list methods #######################
numbers= [5,2,1,7,4]
numbers.append(40)
# here the append function adds the number 40 to the end of the list
print(numbers)

numbers.insert(3,7) # here insert(3,7) function, allows the number 7 to be 
# placed at the 3rd index of the list numbers= [5,2,1,7,4] and all numbers are pushed.

# remove function alllows an item from list to be removed, eg.

numbers.remove(5) # here 5 is the item in numbers list that needs to
# removed.

print(numbers)

# if want to remove all items in list use clear function:

# e.g.:
numbers.clear()
# thefunction pop removes last item in list e.g.
numbers=[1,2,5,6]
numbers.pop()
print(numbers)

# to check existence of item in a list call the index method: e.g:
numbers=[1,2,3,4,5]
numbers.index(5)  # gives the index pof the 1st occurence of the item 5 in the list
print(numbers.index(5))

print(numbers.index(78))

# to check if item is in a list, can use the in operator: e.g
numbers=[1,2,3,5,6]
50 in numbers
print(50 in numbers)
# get False in terminal , which means 50 is not in the list.
numbers.sort() # sort function, sorts the items in list in asscending order
# here, numbers.sort() it does'nt print anything out.
print(numbers)
# reverse function, puts the the list numbers in reverse order.

# using copy function, allows a lost to be copied.
numbers=[1,4,5,8,9,0]
numbers2=numbers.copy()
print("numbers= ", numbers, "numbers2= ", numbers2)

def dup_remove(A):
    emp= []
    for num in A:
        if num not in emp:
           emp.append(num)
    return emp

print(dup_remove([1,2,2,2,2,2,5,7,3]))

 ################################# tuples ############################
 # paused at 2:13:35

numbers= (1,2,3) # this is a tuple 
# cannot remove, or add or replace any items in a tuple, you can check which index
# tuples cannot be changed.
# tuple is a good thing to use if you don't want any acha
 

  ############################## unpacking #################

coordinates=(1,2,3) # want to use values in this tuple in complex expression
# in programme, but need to use coordinate[1], coordinate[2], coordinate[3]
# in the formula which is long, instead create 3 variables each variable is assigned to
# one of the items in tuple e.g.
# x=coordinate[0]
# y=coordinate[1]
# z=coordinate[2]
# this is called unpacking.]
# the code below does the same this as the codes from line 166 
x,y,z=coordinates # here when python sees this state ment, it makes the 1st item in "coordinates"
# equal 1st variable on the left hand side of the equal sign which is "x."
# this preocedure is known as unpacking the tuple "coordinates" into 3 variables.
# unpacking

################## dictionary ########################

# below is an example of customer attributes e.g.
name: Holly
Email: holly@gmail.com
phone: 1538392476
# here the attributes on the left of the semicolon are called "keys"
# also, the values on the right of the semicolon are known as variablesbelow is defining dictionary in python:
customer={
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# here " customer" the dictionary and name, age, i_verified are the keys
# also cannot use same keys, i.e. keys have to be unique.
# below shows how to get the values from the dictionary "customer":
#customer["name"] # here this has value that is asigned to "name" key, so this has value "John Smith".

#print(customer["name"]) 


#print(customer["age"])

 # key is case sensative, so e.g. customer["Name"] gives an error.
# can also use "get function" so,
#print(customer.get("name")) 
# also can supply default value for a key that does not exist e.g:
#customer.get("birthdate", "Jan 1 1980")
#customer.get("history", "hello")
#print(customer("history"))

# Can change key values, e.g:
customer["name"]= "Harret Sparrow"
print(customer["name"])
# can add new key into the dictionary by e.g.:
customer["birthdate"]="jan 1 1876"
print(customer["birthdate"])
################## challenge ##############
Number={ 
       "0":"Zero",
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
Phone=input("Phone: ") # correct
for i in Phone:
    print(Number[i]) # here when putting "i", in "Number["i"]", the code gives error,
    # because i is already a string, it is not an
    # integer, so doing "Number[i]" is enough.


# here the reason the above worked is because "i" in "phone" is not an integer its
#string, so 
################# solution #################

Number={ 
       "0":"Zero",
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
Phone=input("Phone: ") # correct
output=""
for i in Phone:
    output += Number.get(i,"!")+ " "
print(output)

####################### emoji converter ##################

# to convert emoji ca use a diction which maps characters to emoji faces.
message=input(">")
# want to break input up
words=message.split(' ') # split('') here the "split" function geos through the string and 
# cuts the string up where there is a space " ", then it puts the peices of the string in a list
# e.g:
print(words)
emojis={
    ":)"
}

####################### function #####################

# parameters are the place holders in a function for receiving information.

#  an "argument" is the value that we supply to a function,

# positional arguments, are arguments where there position matters, so if there positions are changed
# the result changes.
## keyword arguments e.g:

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print("Welcome aboard")

greet_user(last_name="smith", first_name="Smith")

# keyword arguments are used to allow other poeple see what each argument of a function represents
# e.g. defining a function:
#sale(2,4,6) # here another person looking at this function would not know what the arguments "2", "4" and "6" represents, e.g the 1st argument respresnts anual sales, 2nd argument represents costs
# 3rd arguments represents total sales., so its better to use keyword arguments showne below:
# sale(anual_sale=2,total_sale=4, house_cost=6)

############# paused on 2:43:13 on  python youtube video 


