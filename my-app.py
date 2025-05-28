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
    
    
    
    