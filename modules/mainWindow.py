
from tkinter import *
import random
import pygame
import threading
import os

from modules.toDoListWindow import ToDoListWindow


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        print("Starting Minato Aqua Maid...")
        # instance variables

        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.soundsNameList = [file for file in os.listdir("sounds") if file.endswith(".mp3")] # store the name of all mp3 files in "sounds" folder

        # settings
        pygame.mixer.init()

        # main window
        self.BackgroundImage = PhotoImage(file="img/minato-aqua-excited-blue256.png") # main window background label image
        self.BackgroundLabel = Label(master=self, image=self.BackgroundImage) # main window background label
        self.BackgroundLabel.config(cursor="hand2")
        self.BackgroundLabel.bind("<Button-1>", lambda event: self.prepareToPlaySound())

        self.BackgroundLabel.pack()

        # main window settings
        self.title("Minato Aqua Maid") # window title bar text
        self.resizable(False, False) # window size can't be changed
        self.overrideredirect(True) # delete window borders
        self.configure(bg="#acdfe6")

        self.width=self.BackgroundImage.width()
        self.height=self.BackgroundImage.height()

        self.posX=(self.screenWidth)-(self.width)
        self.posY=((2 * self.screenHeight)//3)-(self.height)

        self.geometry(f"{self.width}x{self.height}+{self.posX}+{self.posY}")




        # app control frame settings
        self.AppControlFrame = Frame(master=self)

        # exit button
        self.ExitButtonImage = PhotoImage(file="img/minato-aqua-greeting-blue64.png") # exit button image
        self.ExitButton = Button(master=self.AppControlFrame, image=self.ExitButtonImage, command=self.exitApp,
                                             bd=0, cursor="hand2") # exit button
        
        # exit button settings
        self.ExitButton.width=self.ExitButtonImage.width()
        self.ExitButton.height=self.ExitButtonImage.height()

        self.ExitButton.pack()
        


        # main menu frame settings
        self.MainMenuFrame = Frame(master=self)

        # show to do list button
        self.OpenToDoListButtonImage = PhotoImage(file="img/minato-aqua-crying64.png") # to do list window button image
        self.OpenToDoListButton = Button(master=self.MainMenuFrame, image=self.OpenToDoListButtonImage, command=self.openToDoListWindow,
                                                  bd=0, cursor="hand2") # to do list button
        
        # show to do list button settings
        self.OpenToDoListButton.width=self.OpenToDoListButtonImage.width()
        self.OpenToDoListButton.height=self.OpenToDoListButtonImage.height()

        self.OpenToDoListButton.pack()



        # adding frames
        self.MainMenuFrame.posX=0
        self.MainMenuFrame.posY=0
        self.MainMenuFrame.place(x=self.MainMenuFrame.posX, y=self.MainMenuFrame.posY)


        self.AppControlFrame.posX=(self.width) - (self.ExitButton.width)
        self.AppControlFrame.posY=0
        self.AppControlFrame.place(x=self.AppControlFrame.posX, y=self.AppControlFrame.posY)

    def runApp(self):
        # after is to execute after the mainloop started, 0 is the time to wait before executing (in ms)
        self.after(0, lambda: print("Minato Aqua Maid started."))
        self.mainloop()
    
    def exitApp(self):
        print("Exiting Minato Aqua Maid...")
        self.destroy()
        print("Minato Aqua Maid exited.")


    def prepareToPlaySound(self):
        threading.Thread(target=self.playRandomSound()).start()

    def playRandomSound(self):
        print("Playing random sound...")

        randomNumber = random.randint(0, 4) # choose random number from 0 to 4
        print(f"Playing sound: {self.soundsNameList[randomNumber]} ({randomNumber}).")
        # play random sound
        pygame.mixer.music.load(f'sounds/{self.soundsNameList[randomNumber]}')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.15)


    def openToDoListWindow(self):
        print("Opening to-do list window...")
        todoWindow = ToDoListWindow(self)
