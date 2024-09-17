
from tkinter import *




class DeleteToDoListItemWindow(Toplevel):
    def __init__(self, pParent):
        super().__init__(pParent)
        # to do list window settings
        self.title("Delete to-do list item")
        self.resizable(False, False)
        self.configure(bg="#e3bcd5")

        self.width=250
        self.height=150

        self.posX=(pParent.posX) - (self.width)
        self.posY=(pParent.posY) + (self.height//2) + 25

        self.geometry(f"{self.width}x{self.height}+{self.posX}+{self.posY}")

        # title frame
        self.TitleFrame = Frame(master=self)

        # title label
        self.TitleLabel = Label(master=self.TitleFrame, text="Delete to-do list item",
                                                             bd=0, font=("Arial", 20), bg="#e3bcd5")
        self.TitleLabel.pack()

        # main frame
        self.MainFrame = Frame(master=self)

        # delete item entry
        self.DeleteItemEntry = Entry(master=self.MainFrame,
                                  bd=0, bg="#f7d5eb")
        self.DeleteItemEntry.pack()

        self.DeleteItemEntry.focus_set()

        # confirm delete button
        self.ConfirmDeleteButton = Button(master=self.MainFrame, text="Confirm",
                                       bd=0, bg="#f7d5eb", command=lambda: self.deleteToDoListItem(self.DeleteItemEntry.get(), pParent))
        self.ConfirmDeleteButton.pack()


        self.TitleFrame.configure(bg="#e3bcd5")
        self.TitleFrame.pack()

        self.MainFrame.configure(bg="#e3bcd5")
        self.MainFrame.pack()

    def deleteToDoListItem(self, pItemNumberToDelete, pParent):
        if pParent.deleteToDoListItem(pItemNumberToDelete):
            self.destroy()
