"""
2. Write a Character Creator program for a role-playing game. The player should be given a pool of 30 poitns to spend
   on four attributes: Strength, Health, Wisdom, and Dexterity. The player should be able to spend points from the pool 
   on any attribute and should also be able to take points from an attribute and put them back into the pool.
"""
#Setting Initial Values
skillPoints = 30
skillsDB = {'Strength':[(0)],
            'Health':[(0)],
            'Wisdom':[(0)],
            'Dexterity':[(0)]}
ListOfKeys = skillsDB.keys()

errorMessage = ["\n    ** Please enter 'Yes' or 'No' ** \n", "\n    ** That is not a valid input. **\n"]

def test():
    print("\
        ** This is a test ** \
        ")
    
#for i in ListOfKeys :
#    print(i)

#Asking if create character
while True:
    createChar = input("Do you wish to create a character? ")
    if createChar.isalpha() == True :
        if createChar[0].lower() == "y" :
            needInfo = True
            nameChar = True
            addPoints = False
            removePoint = False
            print("")
            break
        elif createChar[0].lower() == "n" :
            needInfo = False
            print("\n\nOh... Okay... *sad face* :'(")
            break
        else :
            print(errorMessage[0])
    else :
        print(errorMessage[0])

#Getting Character Name
while nameChar == True :
        charName = input("Character Name: ")
        charName1 = charName.replace(" ", "")
        if charName1.isalpha() :
            charName = charName.title()
            while True:
                correct = input("\nYour name is, " + charName + ", Correct? ")
                if correct.isalpha():
                    if correct[0].lower() == "y" :
                        nameChar = False
                        break
                    elif correct[0].lower() == "n" :
                        print("\nPlease enter your characters name. ")
                        break
                print(errorMessage[0])
                
        else:
            print("\n    ** That is not a valid name ** \n")

#### CREATE SKILL SELECTION / POINT USE LOOP ####

