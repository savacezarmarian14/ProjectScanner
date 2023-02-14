class TodoParser:
    def __init__(self, filename):
        self.handler = open(filename, "r")
    
    def getNumbersOfTodo(self):
        counter = 0
        for line in self.handler.readlines():
            for case in ["todo", "to do"]:
                if case in line.lower():
                    counter += 1
        return counter




