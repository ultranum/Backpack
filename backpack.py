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
        pass
    def moveItem(self):
        pass
    def getName(self):
        return self.name
class pens:
    def __init__(self, name):
        self.name = name

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
class menu:
    pass
locker = container('locker')
backpack = container('backpack')
pencilCase = container('pencilCase')

print(locker.getName())