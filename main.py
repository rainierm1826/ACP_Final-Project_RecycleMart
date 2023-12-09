import customtkinter
from tkinter import messagebox, PhotoImage
from PIL import Image
import Database
from Registration import RegistrationWindow
from Home import home
from Database import loginvalidator, get_database_connection, close_database_connection

def LoginGUI():
	customtkinter.set_appearance_mode("light")
	LoginWindow = customtkinter.CTk()
	LoginWindow.geometry("1200x600")
	LoginWindow.title("RecycleMart")
	LoginWindow.resizable(False, False)

	bg_image = PhotoImage(file="bg3.png")
	bg = customtkinter.CTkLabel(master=LoginWindow,
								image=bg_image)
	bg.pack()

	def RegisterWindow():
		LoginWindow.destroy()
		RegistrationWindow()

	def Login():
		connection = get_database_connection()

		D_Username = UserEntry.get()
		D_Password = PassEntry.get()

		data = Database.loginvalidator(connection, (D_Username, D_Password))

		if data:
			messagebox.showinfo(title="Status", message="Login Succesfully")
			LoginWindow.destroy()
			home(D_Username)
		else:
			messagebox.showerror(title="Error", message="Incorrect Username or Password")

	#Inheritance
	class FrameClass(customtkinter.CTkFrame):
		def __init__(self):
			super().__init__(master=LoginWindow,
							 width=400,
							 height=500,
							 border_width=0.5,
							 corner_radius=10,
							 border_color="black",
							 fg_color="#6dbc9b",
							 bg_color="#092C28")
			self.place(y=50, x=400)

	LoginFrame=FrameClass()

	#Inheritance
	class LabelClass(customtkinter.CTkLabel):
		def __init__(self, text, width, height, font, x, y):
			super().__init__(master=LoginFrame, #Abstraction
							 text=text,			#Abstraction
							 width=width,		#Abstraction
							 height=height,
							 font=font,
							 text_color='#114028')
			self.place(x=x, y=y)

	RecycleMartLabel=LabelClass("RecycleMart", 200, 75, ('Arial', 40, 'bold'), 95, 20 )
	QuoteLabel=LabelClass("Where Sustainability Meets Convenience", 200, 50, ('Helvetica', 20, 'italic'), 10, 75)

	#Parent Class
	from customtkinter import CTkEntry

	#Child who inherit the attributes of CTkEntry
	class Entries(customtkinter.CTkEntry):
		def __init__(self, placeholder_text, x, y, show):
			super().__init__(master=LoginFrame,
							 width=325,
							 height=50,
							 corner_radius=20,
							 placeholder_text=placeholder_text,
							 show=show)
			self.place(x=x, y=y)

	UserEntry = Entries("Username", 37.5, 175, None)
	PassEntry = Entries("Password", 37.5, 250, "•")

	class Buttons(customtkinter.CTkButton):
		def __init__(self, text, x, y, command):
			super().__init__(master=LoginFrame, 	#Abstraction
							 width=100,				#Abstraction
							 height=50,				#Abstraction
							 text=text,				#Abstraction
							 corner_radius=10,		#Abstraction
							 bg_color="#6dbc9b",	#Abstraction
							 fg_color="#092C28",	#Abstraction
							 hover_color="black",	#Abstraction
							 command=command)
			self.place(x=x, y=y)

	LoginBtn = Buttons("Login", 90, 325, Login)
	Register = Buttons("Register", 210, 325, RegisterWindow)


	LoginWindow.mainloop()


LoginGUI()