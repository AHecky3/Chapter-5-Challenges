#!/usr/local/bin/python3.3
"""
2. Write a Character Creator program for a role-playing game. The player should be given a pool of 30 poitns to spend
   on four attributes: Strength, Health, Wisdom, and Dexterity. The player should be able to spend points from the pool
   on any attribute and should also be able to take points from an attribute and put them back into the pool.
"""
#Setting Initial Values
skillPoints = 30
skillsDB = {'Strength':[('0')],
            'Health':[('0')],
            'Wisdom':[('0')],
            'Dexterity':[('0')]}
ListOfKeys = skillsDB.keys()

errorMessage = ["\n    ** Please enter 'Yes' or 'No' ** \n", "\n    ** That is not a valid input. **\n"]

def toDictionary() :
    global skillPoints
    print("How many points do you want to " + skillChange.lower(), tofrom, editSkill)
    if whileAdd == True :
        addPoints = int(input("Add:   "))
        print("points")
        removePoints = 0
        skillPoints -= addPoints
    if whileRemove == True:
        addPoints = int(input("Remove:   "))
        print("points")
        addPoints = 0
        skillPoints += removePoints
    keyPull = skillsDB[editSkill] #Pulling List from Dictionary
    skillPull = keyPull[0] #Pulling Key Value from List
    editDict = int(skillPull) + addPoints - removePoints #Setting Value to change Dict
    skillsDB[editSkill] = str(editDict) #Assigning Value to Dict

def printSkills():
    print("")
    print("You have '" + str(skillPoints) + "' free skill points. ")
    print("Current Stats: " + charName)
    for i in skillsDB :
        for j in skillsDB[i] :
          print("    - " + i + " : " + j[0])
    print('')

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
while True:
    printSkills()
    print("What skill do you wish to edit? ")
    editSkill = input("Skill: ").title()
    print("")
    print("Do you want to add or remove points from " + editSkill + "?")
    skillChange = input("Add or Remove: ").title()
    print("")
    if skillChange == "Add" :
        whileAdd = True
        whileRemove = False
        tofrom = "to"
    elif skillChange == "Remove" :
        whileAdd = False
        whileRemove = True
        tofrom = "from"
    toDictionary()




