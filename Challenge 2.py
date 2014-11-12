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
charName = ""
errorMessage = ["\n    ** Please enter 'Yes' or 'No' ** \n", "\n    ** That is not a valid input. **\n"]
create_Char = False

def getPoints() :
    global skillPoints, skillsDB, charName, skillChange, tofrom, editSkill, addPoints, removePoints
    print("How many points do you want to " + skillChange.lower(), tofrom, editSkill)
    if whileAdd == True :
        addPoints = int(input("Add: "))
        removePoints = 0
        skillPoints -= addPoints
        if skillPoints < 0 :
            print("\nYou don't have that many points to spend. ")
            skillpoints += addPoints
    if whileRemove == True:
        removePoints = int(input("Remove:   "))
        addPoints = 0
        skillPoints += removePoints
        if skillPoints > 30 :
            print("\nYou cannot do that! ")
            skillPoints -= removePoints
    
def toDictionary() :
    global skillsDB, editSkill, addPoints, removePoints
    keyPull = skillsDB[editSkill] #Pulling List from Dictionary
    skillPull = keyPull[0] #Pulling Key Value from List
    editDict = int(skillPull) + addPoints - removePoints #Setting Value to change Dict
    if (int(editDict) > 0) and (int(editDict) < 31):
        del skillsDB[editSkill][0]
        skillsDB[editSkill] += [str(editDict)] #Assigning Value to Dict
    else :
        editDict = 0
        print(errorMessage[1])

def printSkills():
    global skillsDB, charName, skillPoints
    print("")
    print("You have '" + str(skillPoints) + "' free skill points. ")
    print("Current Stats | " + charName)
    for i in skillsDB :
        for j in skillsDB[i] :
          print("    - " + i + " : " + j[:])
    print('')

def programQuit():
    global nameChar, end_Program, qyon, whileAdd, whileRemove, charName, create_Char, valid_Name, chos_Skill, needInfo
    while True :
        print("\nAre you sure you want to quit? ")
        if skillPoints > 0:
            print('You still have ' + str(skillPoints) + " left to spend. ")
        qyon = input("Quit?: ")
        if charName == "Done" :
            charName = ""
        if qyon.isalpha() == True :
            if qyon[0].lower() == "y" :
                print("")
                end_Program = True
                nameChar = False
                create_Char = True
                valid_Name = True
                chos_Skill = False
                needInfo = False
                break
            elif createChar[0].lower() == "n" :
                print("")
            else :
                print(errorMessage[0])
        else :
            print(errorMessage[0])
    
#for i in ListOfKeys :
#    print(i)

#Asking if create character
while create_Char == False :
    createChar = input("Do you wish to create a character? ")
    if createChar.isalpha() == True :
        if createChar[0].lower() == "y" :
            needInfo = True
            nameChar = True
            addPoints = False
            removePoint = False
            valid_Name = False
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
        charName = charName.title()
        if charName == "Done" :
            programQuit()
        charName1 = charName.replace(" ", "")
        if charName1.isalpha() :
            while valid_Name == False:
                correct = input("\nYour name is, " + charName + ", Correct? ")
                if correct.isalpha():
                    if correct[0].lower() == "y" :
                        nameChar = False
                        valid_Name = True
                        chos_Skill = True
                        break
                    elif correct[0].lower() == "n" :
                        print("\nPlease enter your characters name. ")
                        break
                    elif correct[0].lower() == "d" :
                        programQuit()
                    else:
                        print(errorMessage[0])
                else:
                    print(errorMessage[0])

        else:
            print("\n    ** That is not a valid name ** \n")

#### CREATE SKILL SELECTION / POINT USE LOOP ####
while chos_Skill == True:
    printSkills()
    print("What skill do you wish to edit? ")
    editSkill = input("Skill: ").title()
    print("")
    if editSkill in ListOfKeys :
        print("Do you want to add or remove points from " + editSkill + "?")
        while True:
            skillChange = input("Add or Remove: ").title()
            if skillChange.isalpha():
                break
        print("")
        if skillChange == "Add" :
            whileAdd = True
            whileRemove = False
            tofrom = "to"
        elif skillChange == "Remove" :
            whileAdd = False
            whileRemove = True
            tofrom = "from"
        elif skillChange == "Done" :
            programQuit()
        getPoints()
        if (skillPoints > -1) and (skillPoints < 31) :
            toDictionary()
    elif editSkill == "Done" :
        programQuit()
    else :
        print("That is not a valid stat. ") 


while end_Program == True :
    print("\n")
    print("Chacter Information | " + charName)
    for i in skillsDB :
        for j in skillsDB[i] :
          print("    - " + i + " : " + j[0])

    input("\n\n\t <press enter to exit> ")
    end_Program = False
