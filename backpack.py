'''
title: backpack multiday project
author: garrett
date created: 2019-04-02
'''
class container:
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

class pens:
    def __init__(self):
        self.penList = []
    def addPen(self):
        return self.penList.append(input('color ') + ' pen')
    def getPens(self):
        print(self.penList)

def menu():
    print('1) add an item')
    action = input('2) move an item ')
    if action == '1':
        print('Add Item')
        print('1) pens')
        choice = input('2) dont use doesnt work')
        if choice == '1':
            pens.addPen()
            print(pens.getPens())
pens = pens()
locker = container('locker')
backpack = container('backpack')
pencilCase = container('pencilCase')


print(locker.getName())

locker.getContents()

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