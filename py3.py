secret_number=8
max_guess=3
count_guess=0

while count_guess<max_guess:
    count_guess+=1
    guess=int(input("Guess: "))
    if guess==secret_number:
        print("You are correct")
        break
if count_guess==max_guess:
    print("You have failed")

# use the break statement to terminate the loop

#below is more efficient method 
secret_number=8
max_guess=3
count_guess=0

while count_guess<max_guess:
    count_guess+=1
    guess=int(input("Guess: "))
    if guess==secret_number:
        print("You are correct")
        break
else:
    print("You have failed")

#game

command="" # the "" means any value can be here
while True: 
    command=input("> ").lower()
    if command=="start":
       print("Car started...Ready to go!")
    elif command=="stop":
        print("Car stopped.")
    elif command=="help":
       print(''' 
       start- to start the car
       stop- to stop the car
       quit- to quit''')
    elif command=="quit":
        break
    else: 
        print("I don't understand....")



# The"While true" statement means that the code under while stament keeps on going the code under the while statement until
# the "break"  statement executed

#paused at 1:38:45
# if the condition on line 35 is true, then the program will
# print "Car started...Ready to go!", 
# #then the program goes back to beginning (line 34) of the code under while
#statement and exectes that line 34
# but if the condition in line 44 is true, then programme executes 
# break statement, and the programes stops and does not execute the code under while statement

# improved programme:
command="" 
started=False
stopped= False
while True:
    command=input("> ").lower()
    if command=="start":
       if started: # here, "if started" means if value of started is True, then print "Car already started!", else print 
          print("Car already started!")
       else:
          print("Car started!")
          start=True
    elif command=="start":
        if stopped: # 
          print("Car already stopped!")
        else:
            print("Car stopped.")
            stopped=True
    elif command=="help":
       print(""" 
    start- to start the car
    stop- to stop the car
    quit- to quit""")
    elif command=="quit":
        break
    else: 
        print("I don't understand....")






