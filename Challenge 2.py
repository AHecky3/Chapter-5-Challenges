"""
2. Write a Character Creator program for a role-playing game. The player should be given a pool of 30 poitns to spend
   on four attributes: Strength, Health, Wisdom, and Dexterity. The player should be able to spend points from the pool 
   on any attribute and should also be able to take points from an attribute and put them back into the pool.
"""
skillPoints = 30
skillsDB = {'Strength':[(0)],
            'Health':[(0)],
            'Wisdom':[(0)],
            'Dexterity':[(0)]}
ListOfKeys = skillsDB.keys()

#for i in ListOfKeys :
#    print(i)