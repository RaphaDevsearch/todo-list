class List:
    def __init__(self, my_list):
        self.list = my_list
        self.status = False
        
    def is_done(self):
        return self.status == True
    
    def edit(self, update_list):
        self.list = update_list # edit the list
        
    def set_status(self):
        self.status = False if self.status == True else False #toggle
    
class TodoList:
    def __init__(self):
        self.lists      = []
        self.pending    = []
        self.done       = []

    def add(self, List):
        print("Add List to {lists}")
    
    def delet(self, List):
        print("Delet List from {list}")
        
    def show(self, lists):
        print("show each Object in lists")

    def analytics(self):
        print("Analitics and data visualisation")    
    
    