
from tkinter import *
from modules.addToDoListItemWindow import AddToDoListItemWindow
from modules.deleteToDoListItemWindow import DeleteToDoListItemWindow



class ToDoListWindow(Toplevel):
    def __init__(self, pParent):
        super().__init__(pParent)
        # instance variables
        self.toDoList=self.initToDoList()
        
        # to do list window settings
        self.title("To-do list")
        self.configure(bg="#e3bcd5")

        self.width=350
        self.height=350

        self.posX=(pParent.posX) - (self.width)
        self.posY=(pParent.posY) - (self.height)

        self.geometry(f"{self.width}x{self.height}+{self.posX}+{self.posY}")


        # list frame
        self.ListFrame = Frame(master=self)

        # list title label
        self.ListTitleLabel = Label(master=self.ListFrame, text="To-do list",
                                                             bd=0, font=("Arial", 20), bg="#e3bcd5")

        self.ListTitleLabel.pack()

        # to do list list box
        self.ToDoListListBox = Listbox(master=self.ListFrame, listvariable=self.toDoList,
                               bd=0, activestyle="dotbox", font=("Arial", 15), bg="#f7d5eb")
        self.initToDoListListBox()

        self.ToDoListListBox.pack()

        # list box scrollbar
        self.ListBoxScrollBarX=Scrollbar(master=self.ListFrame, orient="horizontal", command=self.ToDoListListBox.xview)

        # list box scrollbar settings
        self.ListBoxScrollBarX.pack(side="bottom", fill="x")

        # list box settings
        self.ToDoListListBox.config(xscrollcommand=self.ListBoxScrollBarX.set)

        # list frame settings
        self.ListFrame.pack()


        # main menu frame
        self.MainMenuFrame = Frame(master=self)



        # add to do list item button
        self.AddToDoListItemButtonImage = PhotoImage(file="img/minato-aqua-crying64.png") # add to do list item button image
        self.AddToDoListItemButton = Button(master=self.MainMenuFrame, image=self.AddToDoListItemButtonImage, command=self.openAddToDoListItemWindow,
                                             cursor="hand2", bd=0, bg="#dba4c8", activebackground="#dba4c8") # add to do list item button

        # add to do list item button settings
        self.AddToDoListItemButton.width=self.AddToDoListItemButtonImage.width()
        self.AddToDoListItemButton.height=self.AddToDoListItemButtonImage.height()

        self.AddToDoListItemButton.pack()



        # delete to do list item button
        self.DeleteToDoListItemButtonImage = PhotoImage(file="img/minato-aqua-crying64.png") # delete to do list item button image
        self.DeleteToDoListItemButton = Button(master=self.MainMenuFrame, image=self.DeleteToDoListItemButtonImage, command=self.openDeleteToDoListItemWindow,
                                             cursor="hand2", bd=0, bg="#dba4c8", activebackground="#dba4c8") # delete to do list item button
        
        # delete to do list item button settings
        self.DeleteToDoListItemButton.width=self.DeleteToDoListItemButtonImage.width()
        self.DeleteToDoListItemButton.height=self.DeleteToDoListItemButtonImage.height()

        self.DeleteToDoListItemButton.pack()


        # show console to do list button
        self.ShowConsoleDoListButtonImage = PhotoImage(file="img/minato-aqua-crying64.png") # show console to do list button image
        self.ShowConsoleDoListButton = Button(master=self.MainMenuFrame, image=self.ShowConsoleDoListButtonImage, command=self.showConsoleToDoList,
                                             cursor="hand2", bd=0, bg="#dba4c8", activebackground="#dba4c8") # show console to do list button
        
        # delete to do list item button settings
        self.ShowConsoleDoListButton.width=self.ShowConsoleDoListButtonImage.width()
        self.ShowConsoleDoListButton.height=self.ShowConsoleDoListButtonImage.height()

        self.ShowConsoleDoListButton.pack()


        self.ListFrame.configure(bg="#e3bcd5")
        self.ListFrame.posX=0
        self.ListFrame.posY=0
        self.ListFrame.place(x=self.ListFrame.posX, y=self.ListFrame.posY)

        self.MainMenuFrame.configure(bg="#e3bcd5")
        self.MainMenuFrame.posX=(self.width) - (self.AddToDoListItemButton.width) 
        self.MainMenuFrame.posY=0
        self.MainMenuFrame.place(x=self.MainMenuFrame.posX, y=self.MainMenuFrame.posY)

    def destroy(self):
        self.updateToDoListFile()
        Tk.destroy(self)


    def initToDoList(self):
        print("Initializing to-do list...")
        toDoListFile=open("to-do-list.txt", "r")
        toDoListFileLinesList=toDoListFile.readlines()
        print("To-do list initialized.")
        toDoListFile.close()

        return toDoListFileLinesList
    
    def initToDoListListBox(self):
        print("Initializing to-do list listbox...")
        for index in range(len(self.toDoList)):
            item=f"[{index}] | {self.toDoList[index]}"
            self.ToDoListListBox.insert(END, item)
        print("To-do list listbox initialized.")

    def updateToDoListFile(self):
        print("Saving to-do list...")
        toDoListFile=open("to-do-list.txt", "w")
        for index in range(len(self.toDoList)):
            toDoListFile.write(f"{self.toDoList[index]}")
        toDoListFile.close()

        with open("to-do-list.txt", "r") as toDoListFile:
            toDoListFileLines = toDoListFile.readlines()
        
        if not(toDoListFileLines[-1].endswith("\n")):
            with open("to-do-list.txt", "a") as toDoListFile:
                toDoListFile.write("\n")
        print("To-do list saved.")

    def showConsoleToDoList(self):
        print("Showing to-do list..")
        # verifications
        if(len(self.toDoList) == 0):
            print("To-do list is empty.")

        for index in range(len(self.toDoList)):
            print(f"[{index}] {self.toDoList[index]}")

    def openAddToDoListItemWindow(self):
        print("Opening add to do list item window...")
        addWindow = AddToDoListItemWindow(self)
        

    def openDeleteToDoListItemWindow(self):
        print("Opening delete to do list item window...")
        deleteWindow = DeleteToDoListItemWindow(self)

    def addToDoListItem(self, pItemToAdd):
        print("Checking to-do list item..")
        # verifications
        if(pItemToAdd in self.toDoList):
            print(f"{pItemToAdd} already exists in to-do list.")
        else:
            self.toDoList.append(pItemToAdd)
            print(f"Added to-do list item: {pItemToAdd}.")
            self.addToDoListListBoxItem(pItemToAdd)
    
    def addToDoListListBoxItem(self, pItemToAdd):
        pItemToAdd=f"[{len(self.toDoList)-1}] {pItemToAdd}"
        self.ToDoListListBox.insert(END, pItemToAdd)

    def deleteToDoListItem(self, pItemNumberToDelete):
        # convert string parameter to int
        pItemNumberToDelete=int(pItemNumberToDelete)
        print(f"Checking item number : {pItemNumberToDelete}.")
        # verifications
        if(len(self.toDoList) == 0):
            print(f"To-do list is empty, couldn't remove item {pItemNumberToDelete}.")
        elif(pItemNumberToDelete < 0 or pItemNumberToDelete > len(self.toDoList)):
            print(f"Invalid item number : {pItemNumberToDelete}.")
        else:
            deletedItem=self.toDoList.pop(pItemNumberToDelete)
            print(f"Successfully deleted : '{deletedItem}.")

        self.deleteToDoListListBoxItem(pItemNumberToDelete)

    def deleteToDoListListBoxItem(self, pItemNumberToDelete):
        self.ToDoListListBox.delete(pItemNumberToDelete)