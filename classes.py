from tkinter import *
import random
import pygame
import threading
import os



class MinatoAquaMaidApp:
    def __init__(self, pMainWindow: Tk):
        self.MainWindow = pMainWindow
        self.screenWidth = self.MainWindow.winfo_screenwidth()
        self.screenHeight = self.MainWindow.winfo_screenheight()
        pygame.mixer.init()
        self.soundsNameList = [file for file in os.listdir("sounds") if file.endswith(".mp3")] # store the name of all mp3 files in "sounds" folder
        self.toDoListItemsList = []

        self.initMainWindow()

    def initMainWindow(self):
        print("Starting Minato Aqua Maid...")

        # main window
        self.MainWindow.BackgroundImage = PhotoImage(file="img/minato-aqua-excited256.png") # main window background label image
        self.MainWindow.BackgroundLabel = Label(master=self.MainWindow, image=self.MainWindow.BackgroundImage) # main window background label
        self.MainWindow.BackgroundLabel.bind("<Return>", lambda event: self.MainWindow.BackgroundLabel.config(cursor="hand2"))
        self.MainWindow.BackgroundLabel.bind("<Button-1>", lambda event: self.prepareToPlaySound())

        self.MainWindow.BackgroundLabel.pack()

        # main window settings
        self.MainWindow.title("Minato Aqua Maid") # window title bar text
        self.MainWindow.resizable(False, False) # window size can't be changed
        self.MainWindow.overrideredirect(True) # delete window borders
        self.MainWindow.configure(bg="#acdfe6")

        self.MainWindow.width=self.MainWindow.BackgroundImage.width()
        self.MainWindow.height=self.MainWindow.BackgroundImage.height()

        self.MainWindow.posX=(self.screenWidth)-(self.MainWindow.width)
        self.MainWindow.posY=((2 * self.screenHeight)//3)-(self.MainWindow.height)

        self.MainWindow.geometry(f"{self.MainWindow.width}x{self.MainWindow.height}+{self.MainWindow.posX}+{self.MainWindow.posY}")




        # app control frame settings
        self.MainWindow.AppControlFrame = Frame(master=self.MainWindow)

        # exit button
        self.MainWindow.ExitButtonImage = PhotoImage(file="img/minato-aqua-greeting64.png") # exit button image
        self.MainWindow.ExitButton = Button(master=self.MainWindow.AppControlFrame, image=self.MainWindow.ExitButtonImage, command=self.exitApp,
                                             bd=0, cursor="hand2") # exit button
        
        # exit button settings
        self.MainWindow.ExitButton.width=self.MainWindow.ExitButtonImage.width()
        self.MainWindow.ExitButton.height=self.MainWindow.ExitButtonImage.height()

        self.MainWindow.ExitButton.pack()
        


        # main menu frame settings
        self.MainWindow.MainMenuFrame = Frame(master=self.MainWindow)

        # show to do list button
        self.MainWindow.ToDoListButtonImage = PhotoImage(file="img/minato-aqua-crying64.png") # to do list window button image
        self.MainWindow.ToDoListButton = Button(master=self.MainWindow.MainMenuFrame, image=self.MainWindow.ToDoListButtonImage, command=self.showToDoList,
                                                  bd=0, cursor="hand2") # to do list button
        
        # show to do list button settings
        self.MainWindow.ToDoListButton.width=self.MainWindow.ToDoListButtonImage.width()
        self.MainWindow.ToDoListButton.height=self.MainWindow.ToDoListButtonImage.height()

        self.MainWindow.ToDoListButton.pack()

        # add to do list item button
        self.MainWindow.AddToDoListItemButton = PhotoImage(file="img/minato-aqua-crying64.png") # add to do list item window button image
        self.MainWindow.AddToDoListItemButton = Button(master=self.MainWindow.MainMenuFrame, image=self.MainWindow.ToDoListButtonImage, command=self.initAddToDoListItemWindow,
                                                  bd=0, cursor="hand2") # add to do list item button
        
        # add to do list item button settings
        self.MainWindow.AddToDoListItemButton.width=self.MainWindow.ToDoListButtonImage.width()
        self.MainWindow.AddToDoListItemButton.height=self.MainWindow.ToDoListButtonImage.height()

        self.MainWindow.AddToDoListItemButton.pack()

        # delete to do list item button
        self.MainWindow.DeleteToDoListItemButton = PhotoImage(file="img/minato-aqua-crying64.png") # delete to do list item window button image
        self.MainWindow.DeleteToDoListItemButton = Button(master=self.MainWindow.MainMenuFrame, image=self.MainWindow.ToDoListButtonImage, command=self.initDeleteToDoListItemWindow,
                                                  bd=0, cursor="hand2") # delete to do list item button
        
        # delete to do list item button settings
        self.MainWindow.DeleteToDoListItemButton.width=self.MainWindow.ToDoListButtonImage.width()
        self.MainWindow.DeleteToDoListItemButton.height=self.MainWindow.ToDoListButtonImage.height()

        self.MainWindow.DeleteToDoListItemButton.pack()



        # adding frames
        self.MainWindow.MainMenuFrame.posX=0
        self.MainWindow.MainMenuFrame.posY=0
        self.MainWindow.MainMenuFrame.place(x=self.MainWindow.MainMenuFrame.posX, y=self.MainWindow.MainMenuFrame.posY)


        self.MainWindow.AppControlFrame.posX=(self.MainWindow.width) - (self.MainWindow.ExitButton.width)
        self.MainWindow.AppControlFrame.posY=0
        self.MainWindow.AppControlFrame.place(x=self.MainWindow.AppControlFrame.posX, y=self.MainWindow.AppControlFrame.posY)



    def runApp(self):
        # after is to execute after the mainloop started, 0 is the time to wait before executing (in ms)
        self.MainWindow.after(0, lambda: print("Minato Aqua Maid started."))
        self.MainWindow.mainloop()
    
    def exitApp(self):
        print("Exiting Minato Aqua Maid...")
        self.MainWindow.destroy()
        print("Minato Aqua Maid exited.")


    def prepareToPlaySound(self):
        threading.Thread(target=self.playRandomSound()).start()

    def playRandomSound(self):
        print("Playing random sound...")

        randomNumber = random.randint(0, 4) # choose random number from 0 to 4
        print(f"Playing sound: {self.soundsNameList[randomNumber]} ({randomNumber})")
        # play random sound
        pygame.mixer.music.load(f'sounds/{self.soundsNameList[randomNumber]}')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.15)


    def initAddToDoListItemWindow(self):
        # to do list item query window
        self.MainWindow.AddToDoListItemWindow = Toplevel(self.MainWindow)

        # to do list item query window settings
        self.MainWindow.AddToDoListItemWindow.title("Add new to-do list item")
        self.MainWindow.AddToDoListItemWindow.resizable(False, False)
        self.MainWindow.AddToDoListItemWindow.configure(bg="#e3bcd5")

        self.MainWindow.AddToDoListItemWindow.width=300
        self.MainWindow.AddToDoListItemWindow.height=100

        self.MainWindow.AddToDoListItemWindow.posX=(self.screenWidth)//2 - (self.MainWindow.AddToDoListItemWindow.width)//2
        self.MainWindow.AddToDoListItemWindow.posY=(self.screenHeight)//2 - (self.MainWindow.AddToDoListItemWindow.height)//2

        self.MainWindow.AddToDoListItemWindow.geometry(f"{self.MainWindow.AddToDoListItemWindow.width}x{self.MainWindow.AddToDoListItemWindow.height}+{self.MainWindow.AddToDoListItemWindow.posX}+{self.MainWindow.AddToDoListItemWindow.posY}")

        # add frame
        self.MainWindow.AddToDoListItemWindow.AddFrame = Frame(master=self.MainWindow.AddToDoListItemWindow)
        
        # title label
        self.MainWindow.AddToDoListItemWindow.TitleLabel = Label(master=self.MainWindow.AddToDoListItemWindow.AddFrame, text="Add new to-do list item",
                                                                 bd=0, bg="#e3bcd5")
        self.MainWindow.AddToDoListItemWindow.TitleLabel.pack()

        # item entry
        self.MainWindow.AddToDoListItemWindow.AddEntry = Entry(master=self.MainWindow.AddToDoListItemWindow.AddFrame,
                                                                 bd=0, bg="#f7d5eb")
        self.MainWindow.AddToDoListItemWindow.AddEntry.pack()
        self.MainWindow.AddToDoListItemWindow.AddEntry.focus_set()

        # add button
        self.MainWindow.AddToDoListItemWindow.AddButton = Button(master=self.MainWindow.AddToDoListItemWindow.AddFrame,
                                                                 text="Add", command=lambda:self.addToDoListItem(self.MainWindow.AddToDoListItemWindow.AddEntry.get()),
                                                                 bd=0, bg="#dba4c8", activebackground="#dba4c8")
        self.MainWindow.AddToDoListItemWindow.AddButton.pack()


        self.MainWindow.AddToDoListItemWindow.AddFrame.configure(bg="#e3bcd5")
        self.MainWindow.AddToDoListItemWindow.AddFrame.pack()

    def showToDoList(self):
        print("Showing to-do list...")
        for index in range(len(self.toDoListItemsList)):
            print(f"[{index}] | {self.toDoListItemsList[index]}")

    def addToDoListItem(self, pItemToAdd):
        print("Validating to-do list item...")
        self.toDoListItemsList.append(pItemToAdd)
        print(f"Added to-do list item: {pItemToAdd}")
        self.MainWindow.AddToDoListItemWindow.destroy()


    def initDeleteToDoListItemWindow(self):
        # to do list item query window
        self.MainWindow.DeleteToDoListItemWindow = Toplevel(self.MainWindow)

        # to do list item query window settings
        self.MainWindow.DeleteToDoListItemWindow.title("Delete to-do list item")
        self.MainWindow.DeleteToDoListItemWindow.resizable(False, False)
        self.MainWindow.DeleteToDoListItemWindow.configure(bg="#e3bcd5")

        self.MainWindow.DeleteToDoListItemWindow.width=300
        self.MainWindow.DeleteToDoListItemWindow.height=100

        self.MainWindow.DeleteToDoListItemWindow.posX=(self.screenWidth)//2 - (self.MainWindow.DeleteToDoListItemWindow.width)//2
        self.MainWindow.DeleteToDoListItemWindow.posY=(self.screenHeight)//2 - (self.MainWindow.DeleteToDoListItemWindow.height)//2

        self.MainWindow.DeleteToDoListItemWindow.geometry(f"{self.MainWindow.DeleteToDoListItemWindow.width}x{self.MainWindow.DeleteToDoListItemWindow.height}+{self.MainWindow.DeleteToDoListItemWindow.posX}+{self.MainWindow.DeleteToDoListItemWindow.posY}")

        # delete frame
        self.MainWindow.DeleteToDoListItemWindow.DeleteFrame = Frame(master=self.MainWindow.DeleteToDoListItemWindow)
        
        # title label
        self.MainWindow.DeleteToDoListItemWindow.TitleLabel = Label(master=self.MainWindow.DeleteToDoListItemWindow.DeleteFrame, text="Delete to-do list item",
                                                                 bd=0, bg="#e3bcd5")
        self.MainWindow.DeleteToDoListItemWindow.TitleLabel.pack()

        # item number entry
        self.MainWindow.DeleteToDoListItemWindow.DeleteEntry = Entry(master=self.MainWindow.DeleteToDoListItemWindow.DeleteFrame,
                                                                 bd=0, bg="#f7d5eb")
        self.MainWindow.DeleteToDoListItemWindow.DeleteEntry.pack()
        self.MainWindow.DeleteToDoListItemWindow.DeleteEntry.focus_set()

        # delete button
        self.MainWindow.DeleteToDoListItemWindow.DeleteButton = Button(master=self.MainWindow.DeleteToDoListItemWindow.DeleteFrame,
                                                                 text="Delete", command=lambda:self.deleteToDoListItem(self.MainWindow.DeleteToDoListItemWindow.DeleteEntry.get()),
                                                                 bd=0, bg="#dba4c8", activebackground="#dba4c8")
        self.MainWindow.DeleteToDoListItemWindow.DeleteButton.pack()


        self.MainWindow.DeleteToDoListItemWindow.DeleteFrame.configure(bg="#e3bcd5")
        self.MainWindow.DeleteToDoListItemWindow.DeleteFrame.pack()
    
    def deleteToDoListItem(self, pItemNumberToDelete):
        # convert string parameter to int
        pItemNumberToDelete=int(pItemNumberToDelete)
        print(f"Deleting item number : {pItemNumberToDelete}")
        deletedItem=self.toDoListItemsList.pop(pItemNumberToDelete)
        print(f"Successfully deleted : '{deletedItem}")
        self.MainWindow.DeleteToDoListItemWindow.destroy()

    





