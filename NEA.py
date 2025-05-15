import tkinter as tk
import customtkinter as ctk

class NEAGui:
    
    def __init__(self):
        
        ctk.set_appearance_mode("System")
        
        self.root = ctk.CTk()
        self.windowheight = 480
        self.windowwidth = 720
        self.root.geometry(f"{self.windowwidth}x{self.windowheight}")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Container stores the pages
        self.container = ctk.CTkFrame(self.root) # To hold the central frame
        self.container.grid(row = 0, column = 0, sticky = "nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.pages = {}
        
        # add pages
        self.AddPage(StartPage)
        self.AddPage(LoginPage)
        self.AddPage(SignUpPage)
        
        # show starting page
        
        self.HidePage(LoginPage)
        self.HidePage(SignUpPage)
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
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller
                
        self.logintext = ctk.CTkLabel(self, text = "Login", font = ('Arial', 40))
        self.logintext.pack()
        # email entry
        
        self.emailentrylabel = ctk.CTkLabel(self, text = "Enter Email Address", font = ('Arial', 15))
        self.emailentrylabel.pack()
        
        self.emailentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.emailentry.pack()
        
        # password entry
        
        self.passwordentrylabel = ctk.CTkLabel(self, text = "Enter Password", font = ('Arial', 15))
        self.passwordentrylabel.pack()

        self.passwordentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, show = "*", corner_radius = 7)
        self.passwordentry.pack()
        
        # login button
        
        self.loginbutton = ctk.CTkButton(self, font = ('Arial', 30), width = 5, text = "Login", fg_color = "red", command = lambda: self.CheckLoginConditions(self.emailentry.get(),self.passwordentry.get()))
        self.loginbutton.pack(pady = 10)
        
class SignUpPage(tk.Frame):
        
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller
            
        
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller
        
        self.title = ctk.CTkLabel(self, text = "Hot Stuff", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "center")
        
        self.loginbutton = ctk.CTkButton(self, text = "Log In", command = lambda: controller.ShowPage(LoginPage))
        self.loginbutton.pack()
        
        self.signupbutton = ctk.CTkButton(self, text = "Sign up", command = lambda: controller.ShowPage(SignUpPage))
        self.signupbutton.pack()
        
NEAGui()


