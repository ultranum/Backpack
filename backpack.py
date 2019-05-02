'''
title: backpack multiday project
author: Garrett Chen
date created: 2019-04-02
'''

class holding:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def addItem(self, obj):
        self.contents.append(obj)

    def getItems(self):
        return self.contents

    def removeItems(self, num):
        self.contents.pop(num)

    def getName(self):
        return self.name

class notebook:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('%s notebook'%(self.name))

    def __repr__(self):
        return ('%s notebook' % (self.name))

class pens:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ('%s pen'%(self.color))

    def __repr__(self):
        return ('%s pen' % (self.color))

class binder:
    def __init__(self, subject):
        self.subject = subject

    def __str__(self):
        return ('%s binder'%(self.subject))

    def __repr__(self):
        return ('%s binder' % (self.subject))

class highlighter:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ('%s highlighter'%(self.color))

    def __repr__(self):
        return ('%s highlighter' % (self.color))

class misc:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

def menu():
    #Prints the names of the containers and their contents
    print(locker.name)
    print('-----')
    for i in range(len(locker.getItems())):
        print(locker.getItems()[i])
    print('')
    print(bag.name)
    print('-----')
    for i in range(len(bag.getItems())):
        print(bag.getItems()[i])
    print('')
    print(pencilCase.name)
    print('-----')
    for i in range(len(pencilCase.getItems())):
        print(pencilCase.getItems()[i])
    print('')
    print('''
Options:    
1) Add an item
2) Move an item
    ''')
    choice = int(input('> ')) # User input choice of action

## Adding Items section
    if choice == 1:
        print('''
Add what?
1) notebook
2) pen
3) binder
4) highlighter
5) other
''')
        item = int(input('>'))
        if item in (1, 3): # Gets options from dictionary below
            return locker.addItem(addOptions[item](input('Subject: ')))
        elif item in (2, 4):
            return locker.addItem(addOptions[item](input('Color: ')))
        elif item == 5:
            return locker.addItem(addOptions[item](input('Name: ')))
        else:
            print('invalid item')

### Moving items section
    elif choice == 2:
        temp = locker.getItems() + bag.getItems() + pencilCase.getItems() # Collects all the items from the three containers
        holdingitem = None # The item being held temporarily
        for i in range(len(temp)):
            print('%s: %s'%(i, temp[i]))
        numb = int(input('number '))

        ## IF ITEM IS IN LOCKER
        if temp[numb] in locker.getItems():
            print('%s is in %s'%(temp[numb], locker.getName()))
            print('''
To where?
1) Bag
2) Pencil Case
            ''')
            moving = int(input('> '))

            # Moving from Locker to Bag
            if moving == 1:
                for i in range(len(locker.getItems())):
                    if temp[numb] == locker.getItems()[i-1]:
                        holdingitem = locker.getItems()[i-1]
                        locker.removeItems(i-1)
                        bag.addItem(holdingitem)

            # Moving from Locker to Pencil Case
            elif moving == 2:
                for i in range(len(locker.getItems())):
                    if temp[numb] == locker.getItems()[i-1]:
                        holdingitem = locker.getItems()[i-1]
                        locker.removeItems(i-1)
                        pencilCase.addItem(holdingitem)

        ## IF ITEM IS IN BAG
        elif temp[numb] in bag.getItems():
            print('%s is in %s'%(temp[numb], bag.getName()))
            print('''
To where?
1) Locker
2) Pencil Case
                                    ''')
            moving = int(input('> '))

            # Moving from Bag to Locker
            if moving == 1:
                for i in range(len(bag.getItems())):
                    if temp[numb] == bag.getItems()[i-1]:
                        holdingitem = bag.getItems()[i-1]
                        bag.removeItems(i-1)
                        locker.addItem(holdingitem)

            # Moving from Bag to Pencil Case
            elif moving == 2:
                for i in range(len(bag.getItems())):
                    if temp[numb] == bag.getItems()[i-1]:
                        holdingitem = bag.getItems()[i-1]
                        bag.removeItems(i-1)
                        pencilCase.addItem(holdingitem)

        ## IF ITEM IS IN PENCIL CASE
        elif temp[numb] in pencilCase.getItems():
            print('%s is in %s'%(temp[numb], pencilCase.getName()))
            print('''
To where?
1) Locker
2) Bag
                        ''')
            moving = int(input('> '))

            # Moving from Pencil Case to Locker
            if moving == 1:
                for i in range(len(pencilCase.getItems())):
                    if temp[numb] == pencilCase.getItems()[i-1]:
                        holdingitem = pencilCase.getItems()[i-1]
                        pencilCase.removeItems(i-1)
                        locker.addItem(holdingitem)

            # Moving from Pencil Case to Bag
            elif moving == 2:
                for i in range(len(pencilCase.getItems())):
                    if temp[numb] == pencilCase.getItems()[i-1]:
                        holdingitem = pencilCase.getItems()[i-1]
                        pencilCase.removeItems(i-1)
                        bag.addItem(holdingitem)


### CODE STARTS HERE
# Creates the container objects
locker = holding('Locker')
bag = holding('Bag')
pencilCase = holding('Pencil case')

# Dictionary is used for adding items
addOptions = {
     1 : notebook,
     2 : pens,
     3 : binder,
     4 : highlighter,
     5 : misc
}

# Preset items
locker.addItem(pens('blue'))
locker.addItem(binder('math'))
bag.addItem(notebook('english'))
bag.addItem(pens('red'))
pencilCase.addItem(misc('ruler'))
pencilCase.addItem(pens('green'))
while True:
    menu()