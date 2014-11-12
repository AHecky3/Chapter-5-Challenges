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
namesDB = {}
names = ["Frank", "Nathan", "James", "Tim", "Jim", "Bob", "Gary", "Kyle", "A.J.", "Patrick", "Henry", "Sam", "Walter", "Ian",
        "Logan", "Shane", "Soloman", "Dan", "Brandon", "Jake", "Carson", "Collin", "Dominic", "David", "Fredrick", "Michael",
        "Joseph", "Withan", "Ethan", "William", "Billy", "Curt", "Chuck", "Kirk", "Lucas", "Shane", "Luke", "Phillip", "Phil",
        "Dale", "Scott", "Matthew", "Andrew", "Ben", "Benjamin", "Hunter", "Trey", "Zach", "Zachry", "Matt", "Ridley", "Steve", 
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
4 - Edit Son-Father Pair
5 - Delete Son-Father Pair
---------------------------
""")

def printDict():
        global namesDB
        count = 1
        print()
        print("Son-Father Pairs: ")
        for key in namesDB:
                for name in namesDB[key]:
                        print("   " + str(count) + ") Son: '" + name + "'")
                        print("      Father: '" + key + "'")
                        count += 1
                        
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
                fatherName = ""
                valid_Son = False
                while valid_Son == False:
                    sonName = input("Your Name: ").title()
                    if sonName.isalpha() :
                       valid_Son = True
                    else :
                        print("\nPlease enter your name. ")
                for key in namesDB:
                        if sonName in namesDB[key]:
                                fatherName = key
                if fatherName == "" :
                        fatherName = random.choice(names)
                        namesDB[fatherName] = [(sonName)]
                print("Your fathers name is... '" + fatherName + "'")
                input("\n\t <press enter to continue>\n")
                valid_Choice = False

        #Printing Son-Father Pairs
        if userChoice == 2:
                printDict()

        #Adding Son-Father Pairs
        if userChoice == 3:
                print()
                valid_Add = False
                valid_Father = False
                valid_Son = False
                while valid_Add == False:
                        while valid_Son == False:                                     
                                sonName = input("Your Name: ").title()
                                if sonName.isalpha():
                                        for key in namesDB:
                                                if sonName in namesDB[key]:
                                                        valid_Son = True
                                                        valid_Father = True
                                                        need_Confirm = False
                                                        valid_Add = True
                                                        print("\n That name is already in a pair! \n")
                                                        input("\n\t<press enter to exit>")
                                                else :
                                                        name_Search = True
                                                        valid_Son = True                                                        

                                else:
                                        print('\nPlease enter your name. ')
                        while valid_Father == False:
                                fatherName = input("Your Fathers Name: ").title()
                                if fatherName.isalpha():
                                        valid_Father = True
                                        need_Confirm = True
                        while need_Confirm == True:
                                print("\n    Please confirm the pair below. ")
                                print("\tSon Name: " + sonName)
                                print("\tFather Name: " + fatherName)
                                isCorrect = input("\tCorrect: ")
                                if isCorrect.isalpha():
                                        if isCorrect[0].lower() == "y":
                                                namesDB[fatherName] = [(sonName)]
                                                valid_Add = True
                                                break
                                        elif isCorrect[0].lower() == "n":
                                                valid_Add = True
                                                break
                                        else:
                                                print("\n\t** Please Enter 'Yes' or 'No' ** ")
                                else:
                                        print("\n\t** Please Enter 'Yes' or 'No' ** ")
                

        #Editing Son-Father Pairs
        if userChoice == 4 :
                print()
                valid_Change = False
                valid_Father = False
                valid_Son = False
                valid_NameChange = False
                while valid_Change == False:
                        while valid_Son == False:
                                fathNam = []
                                editSon = input("Your Name: ").title()
                                if editSon.isalpha():
                                        valid_Son = True
                                        for key in namesDB :
                                                if editSon in namesDB[key]:
                                                        fathNam.append(key)
                                        print("Current Son-Father Pair: ")
                                        for father in fathNam:
                                                editFather = father
                                                print("    -  Son: " + editSon)
                                                print("       Father: " + father)
                                else :
                                        print("\nThere are no Son-Father pairs with that info. ")
                        while valid_NameChange == False:
                                editName = input("New Father Name: ")
                                if editName.isalpha():
                                        valid_NameChange = True
                                else :
                                        print("\nThat's not a valid name. ")
                        while True:
                                print("\n    Please confirm the pair edit below. ")
                                print("\tSon Name: " + editSon)
                                print("\tOld Father Name: " + editFather)
                                print("\tNew Father Name: " + editName)
                                isCorrect = input("\tCorrect: ")
                                if isCorrect.isalpha():
                                        if isCorrect[0].lower() == "y":
                                                namesDB[editName] = [(editSon)]
                                                if editSon in namesDB[editFather]:
                                                        del namesDB[editFather]
                                                valid_Change = True
                                                break
                                        elif isCorrect[0].lower() == "n":
                                                valid_Change = True
                                                break
                                        else:
                                                print("\n\t** Please Enter 'Yes' or 'No' ** ")
                                else:
                                        print("\n\t** Please Enter 'Yes' or 'No' ** ")
                                
                

        #Removing Son-Father Pairs
        if userChoice == 5:
                print()
                valid_Remove = False
                valid_Son = False
                valid_Father = False
                while valid_Remove == False :
                        print("Please enter the name of the Son and Father in the pair you wish to remove. ")
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
                                print("\n    Please confirm the pair below. ")
                                print("\tSon Name: " + removeSon)
                                print("\tFather Name: " + removeFather)
                                isCorrect = input("\tCorrect: ")
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
        elif (userChoice > 5) or (userChoice < 0):
                print("\n\t** That Is Not A Valid Choice **")

print("\n\n")
input("\t<press enter to exit>")
