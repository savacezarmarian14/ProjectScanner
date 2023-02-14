from constants import *
import os

from tkinter import Tk
from tkinter.filedialog import askdirectory

class TreeNode:
    def __init__(self, path, object_type):
        self.path = path
        self.type = object_type
        self.next = []

    def add_next(self, newNode):
        self.next.append(newNode)



class ProjectSourceTree:
    def __init__(self, path):
        self.directories = 0
        self.files = 0
        self.root = None
        self.path = path

path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)
