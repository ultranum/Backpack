'''
title: backpack multiday project
author: garrett
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
        if item is 1 or 3:
            return locker.addItem(addOptions[item](input('Subject: ')))
        elif item is 2 or 4:
            return locker.addItem(addOptions[item](input('Color: ')))
        elif item is 5:
            return locker.addItem(addOptions[item](input('Name: ')))
        else:
            print('invalid item')
### Moving items section

    elif choice == 2:
        temp = []
        temp2 = []
        temp.append(locker.getItems())
        temp.append(bag.getItems())
        temp.append(pencilCase.getItems())
        print(temp)
        count = 0
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                temp2.append(temp[i][j])
            count += 1
            print('%s: %s'%(count, temp2[i]))
        numb = int(input('number'))-1
        if temp2[numb] in locker.getItems():
            print('%s is in %s'%(temp2[numb], locker.getName()))

        elif temp2[numb] in bag.getItems():
            print('%s is in %s'%(temp2[numb], bag.getName()))

        elif temp2[numb] in pencilCase.getItems():
            print('%s is in %s'%(temp2[numb], pencilCase.getName()))

        print('''move where
        1) locker
        2) bag
        3) pencil case''')


#         print('' From where?
# 1) Locker
# 2) Bag
# 3) Pencil Case
#         ''')
#         moveLocation = int(input('> '))
#         if moveLocation == 1:
#             print('Move What?')
#             for i in range(len(locker.getItems())):
#                 print('%s: %s' %(i, locker.getItems()[i]))
#                 tempNum = int(input('> '))
#                 tempval = locker.getItems()[tempNum] # when moving an item, the item being moved is placed here
#                 print('''
# To where?
# 1) Bag
# 2) Pencil Case
#                         ''')
#                 moving = int(input('> '))
#                 if moving == 1:
#                     locker.removeItems(tempNum)
#                     bag.addItem(tempval)
#
#                 elif moving == 2:
#                     locker.removeItems(tempNum)
#                     pencilCase.addItem(tempval)
#
#         elif moveLocation == 2:
#
#             print('Move What?')
#             for j in range(len(bag.getItems())):
#                 print('%s: %s' % (j, bag.getItems()[j]))
#                 tempNum = int(input('> '))
#                 tempval = bag.getItems()[tempNum]  # when moving an item, the item being moved is placed here
#                 print('''
# To where?
# 1) Locker
# 2) Pencil Case
#                         ''')
#                 moving = int(input('> '))
#                 if moving == 1:
#                     bag.removeItems(tempNum)
#                     locker.addItem(tempval)
#
#                 elif moving == 2:
#                     bag.removeItems(tempNum)
#                     pencilCase.addItem(tempval)
#
#         elif moveLocation == 3:
#             print('Move What?')
#             for k in range(len(pencilCase.getItems())):
#                 print('%s: %s' % (k, pencilCase.getItems()[k]))
#                 tempNum = int(input('> '))
#                 tempval = pencilCase.getItems()[tempNum]  # when moving an item, the item being moved is placed here
#                 print('''
# To where?
# 1) Locker
# 2) Bag
#                         ''')
#                 moving = int(input('> '))
#                 if moving == 1:
#                     pencilCase.removeItems(tempNum)
#                     locker.addItem(tempval)
#
#                 elif moving == 2:
#                     pencilCase.removeItems(tempNum)
#                     bag.addItem(tempval)



### CODE STARTS HERE
locker = holding('Locker')
bag = holding('Bag')
pencilCase = holding('Pencil case')

addOptions = {
     1 : notebook,
     2 : pens,
     3 : binder,
     4 : highlighter,
     5 : misc
}


locker.addItem(pens('blue'))
bag.addItem(notebook('english'))
bag.addItem(pens('red'))
while True:
    menu()

# for i in range(len(bag.getItems())):
#     print('%s: %s'%(i, bag.getItems()[i]))
#
# tempval = bag.getItems()[1]
# bag.removeItems(1)
# locker.addItem(tempval)
#
# print(locker.getItems())
# print(bag.getItems())