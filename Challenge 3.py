#!/usr/local/bin/python3.3
"""
3. Write a "Who's Your Daddy?" program that lets the user enter the name of a male and produces the name of his father.
   (You can use celebrities, fictional characters, or even hitorical figures for fun.) Allow the user to add, replace
   and delete son-father pairs.
"""
#Andrew Hecky
#Last Edit: 11/12/14

#Initial Values
import random
namesDB = {
           }
names = ["Frank", "Nathan", "James", "Tim", "Jim", "Bob", "Gary", "Kyle", "A.J.", "Patrick", "Henry", "Sam", "Walter", "Ian",
        "Logan", "Shane", "Soloman", "Dan", "Brandon", "Jake", "Carson", "Collin", "Dominic", "David", "Fredrick", "Michael",
        "Joseph", "Withan", "Ethan", "William", "Billy", "Curt", "Chuck", "Kirk", "Lucas", "Shane", "Luke", "Phillip", "Phil",
        "Dale", "Scott", "Matthew", "Andrew", "Ben", "Benjamin", "Hunter", "Trey", "Zach", "Zachry", "Matt", "Ridley",
        "T.J.", "Doug", "Don"]
valid_Choice = False
run_Program = True

#Setting Function Definitions
def printMenu():
        print("""
     WHO'S YOUR DADDY?
---------------------------
0 - Quit
1 - Enter Name
2 - Print Son-Father Pairs
3 - Add Son-Father Name
4 - Delete Son-Father Pair
5 - Edit Son-Father Pair
---------------------------
""")

def printDict():
    global namesDB
    for key in namesDB:
        for name in namesDB[key]:
            print(" - Son: '" + name + "' | Father: '" + key + "'")

#Actual Program
#Program Intro
print("""         **!! Welcome to "Who's Your Daddy?" !!**""")
print("     Please enter your name, and we'll find your father.      ")
print("You can add, edit, and remove son-father pairs from the menu. ")
print("  To select an item, pick the number next to your choice." )

while run_Program == True :
    valid_Choice = False
    printMenu()

    #Player Chooses from Menu
    while valid_Choice == False:
        try:
            userChoice = int(input("Choice: "))
            valid_Choice = True
        except ValueError :
            print("\n\t** That's Not A Valid Option **\n")

    #If user wants to exit
    if userChoice == 0:
        run_Program = False

    #Computer Making Son-Father Pair
    if userChoice == 1 :
        print()
        valid_Son = False
        while valid_Son == False:
            sonName = input("Your Name: ").title()
            if sonName.isalpha() :
               valid_Son = True
            else :
                print("\nPlease enter your name. ")
        fatherName = random.choice(names)
        namesDB[fatherName] = [(sonName)]
        print("Your fathers name is... '" + fatherName + "'")
        input("\n\t <press enter to continue>\n")
        valid_Choice = False

    #Printing Son-Father Pairs
    if userChoice == 2:
        printDict()
        print(namesDB)
        valid_Choice = False

    #Adding Son-Father Pairs
    #if userChoice == 3:
        #Code Here

    #Removing Son-Father Pairs
    if userChoice == 4:
        print()
        valid_Remove = False
        valid_Son = False
        valid_Father = False
        while valid_Remove == False :
            print("Please enter the name of the Father and Son")
            print("name in the pair you wish to remove. ")
            while valid_Father == False :
                removeFather = input("Father Name: ")
                if removeFather in namesDB :
                    for name in namesDB[removeFather]:
                        print("    - " + name)
                    valid_Father = True
                else :
                    print("\nThere is no pair with that father name. ")
            while valid_Son == False :
                removeSon = input("Son Name: ")
                if removeSon in namesDB[removeFather]:
                    valid_Son = True
                else :
                    print("\nThat name is not paired with the father name. ")
            while True :
                print("\nPlease confirm the pair below. ")
                print("\tSon Name: " + removeSon)
                print("\tFather Name: " + removeFather)
                isCorrect = input("Correct: ")
                if isCorrect.isalpha():
                    if isCorrect[0].lower() == "y":
                        del namesDB[removeFather]
                        valid_Remove = True
                        break
                    elif isCorrect[0].lower() == "n":
                        valid_Remove = True
                        break
                    else:
                        print("\n\t** Please Enter 'Yes' or 'No' ** ")
                else:
                    print("\n\t** Please Enter 'Yes' or 'No' ** ")
