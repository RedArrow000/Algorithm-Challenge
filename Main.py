#This code takes a credit number and allows the person to choose to go through a certain number of doors according to their credit number
#Then the person can choose which door to go through according to their number of credits
#Each door has a certain number of points to get, and if the user gets that number of points, they get a medal

points1=5
points2=10
points3=0
points4=15

print("Write all answers in lowercase.")
creditNum=int(input("How many credits do you want? Pick a number between 1 and 4: "))
#The line of code below is just double checking the number of credits put in
credit= int(input("Enter the number of credits you chose: "))
if credit==creditNum:
    if credit == 1:
        print("You can choose one door.")
    if credit ==2:
        print("You can choose two doors.")
    if credit ==3:
        print("You can choose three doors.")
    if credit ==4:
        print("You can choose four doors.")
        #If the user does not put in a number between 1 and 4, this line of code will tell them what they did wrong
    if credit != 4 or credit != 3 or credit !=2 or credit !=1:
        print("Not a number between 1 and 4.")
else:
    #This code is only used if creditNum and credit are not equal
    print("That's wrong, check your inputs again")
    ######################################################################################

#This code block is seeing which door to go through if the person has one credit
#The credit == creditNum is put here again so that the whole code doesn't run if the user puts in two different numbers
if credit == creditNum and credit ==1:
    dd1=input("Would you like to go through door one? ")
    if dd1=="yes":
        print("You go through door one")
        #The code below gives the person a certain number of points
        print("You get "+str(points1)+" points!")
    else:
        #This line of code is there for if the user inputs "no"
        print("You cannot go through any other doors")
#This code is the shortest as it only has one door

    ######################################################################################

#This code block is seeing which door to go through if the person has two credits
if credit == creditNum and credit ==2:
    ans2=input("Would you like to go through door two? ") 
    if ans2 == "yes":
        print("You go through door two")
        print("You get "+str(points2)+" points!")
    if ans2 != "yes":
        ans1=input("Would you like to go through door one? ") 
        if ans1 == "yes":
            print("You go through door one")
            print("You get "+str(points1)+" points!")
    #The line of code uses an and statement to figure out if the user puts in no both times 
    if ans2 != 'yes' and ans1 != "yes":
        print("You cannot go through any other doors")
# There is a separate if block instead of an else block for the "cannot go through any other doors" as it has to have two conditions
    ######################################################################################

#This code block is seeing which door to go through if the person has three credits
if credit == creditNum and credit ==3:
    dr3=input("Would you like to go through door three? ")
    if dr3=="yes":
        print("You go through door three.")
        print("You get "+str(points3)+" points :(")
    if dr3!= "yes":
        dr2=input("Would you like to go through door two? ") 
        if dr2 == "yes":
            print("You go through door two")
            print("You get "+str(points2)+" points!")
        elif dr2 != "yes":
            dr1=input("Would you like to go through door one? ")
            if dr1 == "yes":
                print("You go through door one")
                print("You get "+str(points1)+" points!")
    if dr3 != "yes" and dr2 != "yes" and dr1!="yes":
        print("You cannot go through any other doors")
    ######################################################################################

#This code block is seeing which door to go through if the person has four credits
if credit == creditNum and credit ==4:
    door4=input("Would you like to go through door four? ")
    if door4=="yes":
        print("You go through door four.")
        print("You get "+str(points4)+" points!")
    if door4 != "yes":
        door3=input("Would you like to go through door three? ")
        if door3=="yes":
            print("You go through door three.")
            print("You get "+str(points3)+" points :(")
        elif door3 != "yes":
            door2=input("Would you like to go through door two? ")
            if door2=="yes":
                print("You go through door two.")
                print("You get "+str(points2)+" points!")
            if door2!="yes":
                door1=input("Would you like to go through door one? ")
                if door1=="yes":
                    print("You go through door one.")
                    print("You get "+str(points1)+" points!")
    if door4!="yes" and door3!="yes" and door2!="yes" and door1!="yes":
        print("You cannot go through any other doors. ")
#This is the largest block as it has to check all doors individually before it can decide anything
    ######################################################################################
 
#This section tells the user what place they got
total_points=int(input("How many points did you earn? (Be honest) "))
if total_points ==15:
    print("You won!")

if total_points==10:
    print("You got second place!")

if total_points==5:
    print("You got third place!")

if total_points==0:
    print("You lost :(")

    ######################################################################################

#This section decides if the user gets a medal
if total_points==15:
    gold=input("Would you like a medal? ")
    if gold=="yes":
        print("You get a gold medal!")
    if gold !="yes":
        print("Alright")

if total_points==10:
    silver=input("Would you like a medal? ")
    if silver=="yes":
        print("You get a silver medal!")
    if silver !="yes":
        print("Alright")

if total_points==5:
    bronze=input("Would you like a medal? ")
    if bronze=="yes":
        print("You get a bronze medal!")
    if bronze !="yes":
        print("Alright")

if total_points==0:
    print("You get no medal.")

    ######################################################################################

#This section asks the user if they want to leave a review
review=input("Would you like to leave a review? ")
if review=="yes":
    input("Enter your review: ")
else:
    print("Okay.")
