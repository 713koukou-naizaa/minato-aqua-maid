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

        self.initMainWindow()

    def initMainWindow(self):
        print("Starting Minato Aqua Maid...")

        # main window
        self.MainWindow.BackgroundImage = PhotoImage(file="img/minato-aqua-excited256.png") # main window background label image
        self.MainWindow.BackgroundLabel = Label(master=self.MainWindow, image=self.MainWindow.BackgroundImage) # main window background label
        self.MainWindow.BackgroundLabel.bind("<Enter>", lambda event: self.MainWindow.BackgroundLabel.config(cursor="hand2"))
        self.MainWindow.BackgroundLabel.bind("<Button-1>", lambda event: self.prepareToPlaySound())

        self.MainWindow.BackgroundLabel.pack()

        # main window settings
        self.MainWindow.title("Minato Aqua Maid") # window title bar text
        self.MainWindow.resizable(False, False) # window size can't be changed
        self.MainWindow.overrideredirect(True) # delete window borders

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

        # to do list button
        self.MainWindow.ToDoListButtonImage = PhotoImage(file="img/minato-aqua-crying64.png") # to do list window button image
        self.MainWindow.ToDoListButton = Button(master=self.MainWindow.MainMenuFrame, image=self.MainWindow.ToDoListButtonImage, command=self.showToDoListWindow,
                                                  bd=0, cursor="hand2") # to do list button
        
        # to do list button settings
        self.MainWindow.ToDoListButton.width=self.MainWindow.ToDoListButtonImage.width()
        self.MainWindow.ToDoListButton.height=self.MainWindow.ToDoListButtonImage.height()

        self.MainWindow.ToDoListButton.pack()




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


    def showToDoListWindow(self):
        print("Showing to-do list window...")


    





