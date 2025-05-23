import tkinter as tk
import customtkinter as ctk
import sqlite3
import hashlib

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
        self.AddPage(MainMenu)
        
        # show starting page
        
        self.HidePage(LoginPage)
        self.HidePage(SignUpPage)
        self.HidePage(MainMenu)
        self.ShowPage(StartPage)
        
                
        self.root.mainloop()
        
    # 
    # PAGES MANAGER
    #
    
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
            
    #
    # DATABASE MANAGER
    #
    
    def GetHighestUserID(self):
        database = sqlite3.connect("NEADatabase.db")
        cursor = database.cursor()
        cursor.execute("SELECT MAX(UserID) FROM AccountInformation")
        userid = cursor.fetchone()[0]
        database.close()
        return userid
    
    #
    # ENCRYPTION AND DECRYPTION
    #
    
    def EncryptData(self,data):
        hasheddata = hashlib.sha512(data.encode()).hexdigest()
        return hasheddata
    
    # Can't decrypt due to SHA512 restrictions, can only compare hashes
    def CheckEncryptedData(self,foundhash,data):
        if self.EncryptData(data) == foundhash:
            return True
        else:
            return False
    
class LoginPage(tk.Frame):
        
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller
                
        self.logintext = ctk.CTkLabel(self, text = "Sign In", font = ('Arial', 40))
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
        
        # back button
        
        self.BackButton = ctk.CTkButton(self, font = ('Arial', 15), width = 3, text = "Back", fg_color = "red", command = lambda: controller.HidePage(LoginPage))
        self.BackButton.place(x = 55, y = 10)
                                         
    def MakeErrorMessage(self,error):
        try:
            if self.errormessage:
                pass
        except:
            self.errormessage = ctk.CTkLabel(self, text = error, font = ('Arial',15), text_color = "red")
            self.errormessage.pack(pady = 5)
        else:
            # cannot just pass because error text may change unfortunately
            self.errormessage.destroy()
            self.errormessage = ctk.CTkLabel(self, text = error, font = ('Arial',15), text_color = "red")
            self.errormessage.pack(pady = 5)
                                         
        
    def CheckLoginConditions(self,email,password):
        database = sqlite3.connect("NEADatabase.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM AccountInformation WHERE EmailAddress=?", (email,))
        if cursor.fetchone() == None:
            print("Email is not registered in system")
            # add error later
        else:
            cursor.execute("SELECT Password FROM AccountInformation where EmailAddress = ?", (email,))
            dbpass = cursor.fetchone()[0]
            issamepass = self.controller.CheckEncryptedData(dbpass,password)
            if issamepass == True:
                print("Password is correct, login successful")
                if self.errormessage:
                    self.errormessage.destroy()
                
                self.controller.ShowPage(MainMenu)
                self.controller.HidePage(LoginPage)
                # probably add more stuff later
            else:
                print("Password is incorrect, login unsuccessful")
                self.MakeErrorMessage("Password is incorrect.")
                
        database.close()
        
class SignUpPage(tk.Frame):
        
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller
        
        self.logintext = ctk.CTkLabel(self, text = "Register", font = ('Arial', 40))
        self.logintext.pack()
        
        # enter name
        
        self.enterfirstnamelabel = ctk.CTkLabel(self, text = "Enter your first name", font = ('Arial', 15))
        self.enterfirstnamelabel.pack()
        
        self.enterfirstnameentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.enterfirstnameentry.pack()
        
        self.enterlastnamelabel = ctk.CTkLabel(self, text = "Enter your last name", font = ('Arial', 15))
        self.enterlastnamelabel.pack()
        
        self.enterlastnameentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.enterlastnameentry.pack()
        
        # email entry
        
        self.emailentrylabel = ctk.CTkLabel(self, text = "Enter Email Address", font = ('Arial', 15))
        self.emailentrylabel.pack()
        
        self.emailentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.emailentry.pack()
        
        # password entry
        
        self.passwordentrylabel = ctk.CTkLabel(self, text = "Enter Password", font = ('Arial', 15))
        self.passwordentrylabel.pack()

        self.passwordentry = ctk.CTkEntry(self, font = ('Arial', 15), width = 250, corner_radius = 7)
        self.passwordentry.pack()
        
        # sign up button
        
        self.createaccountbutton = ctk.CTkButton(self, font = ('Arial', 30), width = 5, text = "Create Account", fg_color = "red", command = lambda: self.CreateAccount(self.enterfirstnameentry.get(),self.enterlastnameentry.get(),self.emailentry.get(),self.passwordentry.get()))
        self.createaccountbutton.pack(pady = 10)
        
        # back button
        
        self.BackButton = ctk.CTkButton(self, font = ('Arial', 15), width = 3, text = "Back", fg_color = "red", command = lambda: controller.HidePage(SignUpPage))
        self.BackButton.place(x = 55, y = 10)
        
        
    def CreateAccount(self,firstname,lastname,email,password):
        # name = firstname.strip() + " " + lastname.strip()
        highestuserid = self.controller.GetHighestUserID()
        if highestuserid == None:
            highestuserid = 1
        
        # encrypt password
        encryptedpass = self.controller.EncryptData(password)
        
        database = sqlite3.connect("NEADatabase.db")
        cursor = database.cursor()
        cursor.execute("INSERT INTO AccountInformation (EmailAddress, FirstName, LastName, Password) VALUES (?, ?, ?, ?)", (f"{email}", f"{firstname}",f"{lastname}",f"{encryptedpass}"))
        database.commit()
        database.close()
        

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller
        
        self.title = ctk.CTkLabel(self, text = "Hot Stuff", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "center")
        
        self.loginbutton = ctk.CTkButton(self, text = "Sign in", command = lambda: controller.ShowPage(LoginPage))
        self.loginbutton.pack(pady = 5)
        
        self.signupbutton = ctk.CTkButton(self, text = "Register", command = lambda: controller.ShowPage(SignUpPage))
        self.signupbutton.pack(pady = 5)
        
        
class MainMenu(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller
        
        self.title = ctk.CTkLabel(self, text = "Hot Stuff Main Menu", font = ('Arial', 50), anchor = "center")
        self.title.pack(anchor = "center",pady = 5)
    
    
NEAGui()


