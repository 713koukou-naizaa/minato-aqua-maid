import tkinter as tk



class MinatoAquaMaidApp:
    def __init__(self, pMainWindow: tk.Tk):
        self.aMainWindow = pMainWindow
        self.aMainWindow.aToDoListWindow = tk.Toplevel(self.aMainWindow)

        self.initApp()

    def initApp(self):
        print("Starting Minato Aqua Maid...")
        
        # screen dimensions
        self.aScreenWidth = self.aMainWindow.winfo_screenwidth()
        self.aScreenHeight = self.aMainWindow.winfo_screenheight()

        # main window image dimensions
        self.aMainWindow.aImage=tk.PhotoImage(file='minato-aqua-excited256.png')
        self.aMainWindow.aImageWidth=self.aMainWindow.aImage.width()
        self.aMainWindow.aImageHeight=self.aMainWindow.aImage.height()

        # main window settings
        self.aMainWindow.aPosX=self.aScreenWidth - self.aMainWindow.aImageWidth
        self.aMainWindow.aPosY=((2 * self.aScreenHeight) // 3)  - self.aMainWindow.aImageHeight

        self.aMainWindow.geometry(f"{self.aMainWindow.aImageWidth}x{self.aMainWindow.aImageHeight}+{self.aMainWindow.aPosX}+{self.aMainWindow.aPosY}")
        self.aMainWindow.overrideredirect(True)

        #populating main window
        self.aMainWindow.aFrame = tk.Frame(self.aMainWindow)
        self.aMainWindow.aFrame.grid()  # using grid

        self.aMainWindow.ExitButton = tk.Button(self.aMainWindow.aFrame, image=self.aMainWindow.aImage, command=self.exitApp).grid(column=0, row=0)

        self.aToDoListWindowShowButton = tk.Button(self.aMainWindow.aFrame, command=self.showToDoListWindow).grid(column=0, row=0)

        self.initToDoListWindow()

    def runApp(self):
        # after is to execute after the mainloop started, 0 is the time to wait before executing (in ms)
        self.aMainWindow.after(0, lambda: print("Minato Aqua Maid started."))
        self.aMainWindow.mainloop()
    
    def exitApp(self):
        print("Exiting Minato Aqua Maid...")
        self.aMainWindow.destroy()
        print("Minato Aqua Maid exited.")

    def showToDoListWindow(self):
        print("Showing to-do list...")
        self.aMainWindow.aToDoListWindow.deiconify()
        self.showToDoList()
    
    def hideToDoListWindow(self):
        print("Hiding to-do list...")
        self.aMainWindow.aToDoListWindow.withdraw()
    
    def initToDoListWindow(self):
        # to do list window image dimensions
        self.aMainWindow.aToDoListWindow.aWidth=256
        self.aMainWindow.aToDoListWindow.aHeight=384

        # to do list window settings
        self.aMainWindow.aToDoListWindow.aPosX=self.aMainWindow.aPosX - self.aMainWindow.aToDoListWindow.aWidth
        self.aMainWindow.aToDoListWindow.aPosY=self.aMainWindow.aPosY - self.aMainWindow.aToDoListWindow.aHeight

        # populating to do list window
        self.aMainWindow.aToDoListWindow.aFrame = tk.Frame(self.aMainWindow.aToDoListWindow)
        self.aMainWindow.aToDoListWindow.aFrame.grid()  # using grid

        self.aMainWindow.aToDoListWindow.geometry(f"{self.aMainWindow.aToDoListWindow.aWidth}x{self.aMainWindow.aToDoListWindow.aHeight}+{self.aMainWindow.aToDoListWindow.aPosX}+{self.aMainWindow.aToDoListWindow.aPosY}")
        self.aMainWindow.aToDoListWindow.overrideredirect(True)

        self.aMainWindow.aToDoListWindow.aHideButton = tk.Button(self.aMainWindow.aToDoListWindow.aFrame,
                                                                 command=self.hideToDoListWindow).grid(column=1, row=0)

        # creating to do list
        self.aMainWindow.aToDoListWindow.aToDoList = list()

        self.hideToDoListWindow()

    def addToDoListItem(self, pToDoItem: str):
        print(f"Adding '{pToDoItem}' to to-do list.")
        self.aMainWindow.aToDoListWindow.aToDoList.append(pToDoItem)
        print(f"'{pToDoItem}' added to to-do list.")
        
    def showToDoList(self):
        print("Showing to-do list...")
        self.addToDoListItem("omae, yowai, atishi, tsuyoi")
        self.addToDoListItem("atishi")

    





