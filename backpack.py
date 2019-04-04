'''
title: backpack multiday project
author: garrett
date created: 2019-04-02
'''
class locker:
    def __init__(self, name):
        self.name = name
        self.contents = ['binder1', 'pen']
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
        self.contents = ['computer']
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
        self.contents = ['calc']
    def addItem(self):
        self.contents.append(input('new item > '))
    def moveItem(self):
        pass
    def getName(self):
        return self.name
    def getContents(self):
        print('%s: %s' %(self.name, self.contents))


class pens:
    def __init__(self):
        self.penList = []
    def addPen(self):
        return self.penList.append(input('color ') + ' pen')
    def getPens(self):
        print(self.penList)

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
        print('''
Add Item
1) stuff
2) other 
        ''')
        choice = input('> ')
        if choice == '1':
            locker.addItem()

pens = pens()
locker = locker('locker')
backpack = backpack('backpack')
pencilCase = pencilcase('pencil case')

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