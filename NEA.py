import tkinter as tk
import customtkinter as ctk

class NEAGui:
    
    def __init__(self):
        
        ctk.set_appearance_mode("System")
        
        self.root = ctk.CTk()
        self.windowheight = 480
        self.windowwidth = 720
        self.root.geometry(f"{self.windowwidth}x{self.windowheight}")
        
        # Container stores the pages
        self.container = ctk.CTkFrame(self.root) # To hold the central frame
        self.container.place(relx=0.5, rely=0.2, anchor="center", y = 50)
        
        self.pages = {}
        
        # add pages
        self.AddPage(StartPage)
        self.AddPage(LoginPage)
        
        # show starting page
        
        self.HidePage(LoginPage)
        self.ShowPage(StartPage)
        
        self.root.mainloop()
    
    def GetPage(self,pagename):
        return self.pages.get(pagename)
        
    def AddPage(self, pagename):
        # Adds a new page to a dictionary for the UI to show when a button is clicked
        page = pagename(self.container, self)
        self.pages[pagename] = page
        page.grid(row=0, column=0, sticky="nsew")

    def ShowPage(self, pagename):
        page = self.GetPage(pagename)
        if page:
            page.tkraise()
            
    def HidePage(self, pagename):
        page = self.GetPage(pagename)
        if page:
            page.lower()
                        
class LoginPage(tk.Frame):
        
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.controller = controller
                
        self.logintext = ctk.CTkLabel(self, text = "Login", font = ('Arial', 40))
        self.logintext.pack()
        # email entry
        
        self.emailentrylabel = ctk.CTkLabel(self, text = "Enter Email Address", font = ('Arial', 15))
        self.emailentrylabel.pack()
        
        self.emailentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 45,)
        self.emailentry.pack()
        
        # password entry
        
        self.passwordentrylabel = ctk.CTkLabel(self, text = "Enter Password", font = ('Arial', 15))
        self.passwordentrylabel.pack()

        self.passwordentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 45, show = "*")
        self.passwordentry.pack()
        
        # login button
        
        self.loginbutton = ctk.CTkButton(self, font = ('Arial', 30), width = 5, text = "Login", fg_color = "light grey", command = lambda: self.CheckLoginConditions(self.emailentry.get(),self.passwordentry.get()))
        self.loginbutton.pack(pady = 10)
        
    def CheckLoginConditions(self,email,password):
        print(email,password)
        if email == "susburger21@gmail.com" and password == "sussy21":
            # Login Test
            pass
            
        
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.controller = controller
        
        self.title = ctk.CTkLabel(self, text = "Hot Stuff", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "center")
        
        self.loginbutton = ctk.CTkButton(self, text = "Log In", command = lambda: controller.ShowPage(LoginPage))
        self.loginbutton.pack()
        
NEAGui()

