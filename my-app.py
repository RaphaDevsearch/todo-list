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
        self.my_item    = ""
        self.lists      = []
        self.pending    = []
        self.done       = []

    def add(self):
        description = "My first List"
        list = List(description)
        self.lists.append(list)
        print("Add List to {lists}")
    
    def delet(self):
        index = 0
        self.lists.remove(index)
        print("Delet List from {list}")
        
    def show(self):
        for Ob in self.lists:
            print(Ob)
        print("show each Object in lists")

    def analytics(self):
        print("Analitics and data visualisation")    
    


def show_menu():
    print("Our menu")

def chose_menu():
    inputUser = int(input("Choce menu : "))
    
    return inputUser
            

if __name__ == "__main__":
    tdl = TodoList()
    
    while True:
        # show menu
        show_menu()
        # uer choose meu
        inputUser = chose_menu()
        if inputUser == 0:
            print("Bay ....")
            break
        else :
            print("Action")
            # actions
            
            match inputUser:
                case 0:
                    print("Bay ....")
                    break
                case 1:
                    tdl.add()
                case 2 :
                    tdl.delet()
                case 3:
                    tdl.show()
                case 4:
                    tdl.analytics()