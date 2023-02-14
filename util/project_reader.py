import os
from termcolor import colored

FILE = "file"
DIRECTORY = "directory"
UNKNOWN = "unknown"

class TreeNode:
    def __init__(self, path):
        self.path = path

        if os.path.isdir(self.path) == True:
            self.type = DIRECTORY
        elif os.path.isfile(self.path) == True:
            self.type = FILE
        else:
            self.type = UNKNOWN 
            
        self.next = []
        
    def __str__(self) -> str:
        return self.path

    def add_next(self, newNode):
        self.next.append(newNode)

class ProjectSourceTree:
    def __init__(self, path):
        self.directories = 0
        self.files = 0
        self.root = TreeNode(path)
        self.path = path
        self.maximum_depth = 0

        self.read_project_source_tree(self.root, self.path)
        self.compute_depth(self.root)
    
    def read_project_source_tree(self, root, path):
        if os.path.isfile(path) == True:
            self.files += 1
            return
        
        self.directories += 1
        for obj in os.listdir(path):
            root.add_next(TreeNode("{}/{}".format(path, obj)))
        
        for next_node in root.next:
            self.read_project_source_tree(next_node, next_node.path)

    def compute_depth(self, root, level = 1):
        if self.maximum_depth < level:
            self.maximum_depth = level
        
        for next_node in root.next:
            if next_node.type == DIRECTORY:
                self.compute_depth(next_node, level+1)           
    
    def _get_files_path(self, root):
        files = []
        for obj in root.next:
            if os.path.isfile(obj.path):
                files += [obj.path]
            elif os.path.isdir(obj.path):
                files += self._get_files_path(obj)
        return files
   
    def get_files_path(self):
        self._get_files_path(self.root)
    
    def _print_tree(self, root, level = 0):
        line_printed = "\t" * level + str(root)
        
        if root.type == DIRECTORY:
            print(colored(line_printed, 'green'))
        else:
            print(line_printed)
        
        for next_node in root.next:
            self._print_tree(next_node, level+1)
            
    def print_tree(self):
        self._print_tree(self.root)
    
p = ProjectSourceTree("test")
print(p._get_files_path(p.root))

    



