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
        return ('%s'%(self.name))

    def __repr__(self):
        return ('%s' % (self.name))

tempval = None
locker = holding('locker')
bag = holding('bag')
pencilCase = holding('pencil case')

locker.addItem(pens('blue'))
bag.addItem(notebook('english'))
bag.addItem(pens('red'))

print(locker.getItems())
print(bag.getItems())

for i in range(len(bag.getItems())):
    print('%s: %s'%(i, bag.getItems()[i]))

tempval = bag.getItems()[1]
bag.removeItems(1)
locker.addItem(tempval)

print(locker.getItems())
print(bag.getItems())