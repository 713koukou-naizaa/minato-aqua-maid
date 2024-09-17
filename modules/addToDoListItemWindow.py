
from tkinter import *




class AddToDoListItemWindow(Toplevel):
    def __init__(self, pParent):
        super().__init__(pParent)
        # to do list window settings
        self.title("Add to-do list item")
        self.resizable(False, False)
        self.configure(bg="#e3bcd5")

        self.width=250
        self.height=150

        self.posX=(pParent.posX) - (self.width)
        self.posY=(pParent.posY) - (self.height//2) - 25

        self.geometry(f"{self.width}x{self.height}+{self.posX}+{self.posY}")

        # title frame
        self.TitleFrame = Frame(master=self)

        # title label
        self.TitleLabel = Label(master=self.TitleFrame, text="Add to-do list item",
                                                             bd=0, font=("Arial", 20), bg="#e3bcd5")
        self.TitleLabel.pack()

        # main frame
        self.MainFrame = Frame(master=self)

        # add item entry
        self.AddItemEntry = Entry(master=self.MainFrame,
                                  bd=0, bg="#f7d5eb")
        self.AddItemEntry.pack()

        self.AddItemEntry.focus_set()

        # confirm add button
        self.ConfirmAddButton = Button(master=self.MainFrame, text="Confirm",
                                       bd=0, bg="#f7d5eb", command=lambda: self.addToDoListItem(self.AddItemEntry.get(), pParent))
        self.ConfirmAddButton.pack()


        self.TitleFrame.configure(bg="#e3bcd5")
        self.TitleFrame.pack()

        self.MainFrame.configure(bg="#e3bcd5")
        self.MainFrame.pack()

    def addToDoListItem(self, pItemToAdd, pParent):
        if pParent.addToDoListItem(pItemToAdd):
            self.destroy()
