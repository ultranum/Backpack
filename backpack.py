'''
title: backpack multiday project
author: garrett
date created: 2019-04-02
'''

class locker:
    def __init__(self, name):
        self.name = name
        self.contents = []
    def addItem(self):
        self.contents.append(input('new item > '))
    def moveItem(self):
        pass
    def getName(self):
        return self.name
    def getContents(self):
        print('%s: %s' %(self.name, self.contents))

class backpack:
    def __init__(self, name):
        self.name = name
        self.contents = []
    def addItem(self):
        self.contents.append(input('new item > '))
    def moveItem(self):
        pass
    def getName(self):
        return self.name
    def getContents(self):
        print('%s: %s' %(self.name, self.contents))

class pencilcase:
    def __init__(self, name):
        self.name = name
        self.contents = []
    def addItem(self):
        self.contents.append(input('new item > '))
    def moveItem(self):
        pass
    def getName(self):
        return self.name
    def getContents(self):
        print('%s: %s' %(self.name, self.contents))


class items:
    def __init__(self):
        self.name = " "

    def addItem(self):
        self.name = input('add an item')

    def getName(self):
        return self.name

def menu():

    print(locker.getName())
    print('-----')
    for i in range(len(locker.contents)):
        print(locker.contents[i])
    print(' ')
    print(backpack.getName())
    print('-----')
    for i in range(len(backpack.contents)):
        print(backpack.contents[i])
    print(' ')
    print(pencilCase.getName())
    print('-----')
    for i in range(len(pencilCase.contents)):
        print(pencilCase.contents[i])
    print(' ')
    print('''
1) add an item
2) move an item
    ''')
    action = input('> ')
    if action == '1':
        newItem = items()
        newItem.addItem()
        allItems.append(newItem.getName())
        locker.contents.append(newItem.getName())
    if action == '2':
        count = -1
        for i in range(len(allItems)):
            if isinstance(allItems[i], list):
                for j in range(len(allItems[i])):
                    count += 1
                    print(str(count) + ": " + str(allItems[i][j]))
            else:
                count += 1
                print(str(count) + ": " + str(allItems[i]))

        itemchoice = int(input('what item number? '))
        if isinstance(allItems[itemchoice], list):
        print(allItems[itemchoice])
        print('move where?')



allItems = []
locker = locker('locker')
locker.contents = ['binders', 'jacket']
backpack = backpack('backpack')
backpack.contents = ['pencil case', 'laptop']
pencilCase = pencilcase('pencil case')
pencilCase.contents = ['pencil', 'pen']
allItems.append(locker.contents)
allItems.append(backpack.contents)
allItems.append(pencilCase.contents)

while True:
    menu()
















class binder:
    def __init__(self, name):
        self.name = name


class electronics:
    def __init__(self, name):
        self.name = name


class notebook:
    def __init__(self, name):
        self.name = name


class highlighter:
    def __init__(self, name):
        self.name = name