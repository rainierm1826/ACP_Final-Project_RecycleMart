from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
from tkinter import filedialog
import io
from Database import close_database_connection, insert_user_data, get_database_connection
import mysql.connector


def RegistrationWindow():
    customtkinter.set_appearance_mode("dark")
    RegisterWindow = customtkinter.CTk()
    RegisterWindow.geometry("900x600")
    RegisterWindow.title("RecycleMart")
    RegisterWindow.resizable(False, False)
    RegisterWindow.config(bg="white")

    def openfilepath():
        global image_path
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                image = customtkinter.CTkImage(Image.open(file_path), size=(100, 100))
                Avatar.configure(image=image)

                image_path = file_path
            except Exception as e:
                print(f"Error: {e}")

    def Register():
        D_FName = FName.get()
        D_LName = LName.get()
        D_MName = MName.get()
        D_Age = Age.get()
        D_Email = Email.get()
        D_Mobile_Number = Mobile_Number.get()
        D_Current_Address = Current_Address.get()
        D_Username = Username.get()
        D_Password = Password.get()
        D_Sex_combobox = Sex_combobox.get()

        try:

            if (D_FName != "" and
                    D_LName != "" and
                    D_MName != "" and
                    D_Password != "" and
                    D_Sex_combobox != "" and
                    D_Email != "" and
                    D_Current_Address != "" and
                    D_Username != "" and
                    D_Mobile_Number != ""):

                if D_Age != "":
                    age = int(D_Age)
                    if age >= 0 and age <= 150:
                        connection = get_database_connection()
                        insert_user_data(connection, (
                        D_FName, D_LName, D_MName, D_Sex_combobox, D_Age, D_Email, D_Mobile_Number, D_Current_Address,
                        D_Username, D_Password, image_path))

                        messagebox.showinfo(title="Status", message="Registered Successfully")
                        close_database_connection(connection)
                    else:
                        messagebox.showerror(title="Error", message="Invalid Age")


            else:
                messagebox.showerror(title="Error", message="Complete your Information")

        except mysql.connector.errors.IntegrityError:
            messagebox.showerror(title="Error", message="There is already an existing username.")

        except ValueError:
            messagebox.showerror(title="Error", message="Invalid Age")

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror(title="Error", message="Insert a profile photo")

    class FrameClass(customtkinter.CTkFrame):
        def __init__(self, master, height, width, fg_color, bg_color, border_width, border_color, corner_radius, x, y):
            super().__init__(master=master,
                             height=height,
                             width=width,
                             fg_color=fg_color,
                             bg_color=bg_color,
                             border_width=border_width,
                             border_color=border_color,
                             corner_radius=corner_radius)
            self.place(x=x, y=y)

    RegisterFrame = FrameClass(RegisterWindow, 480, 650, 'white', 'white', 1, "#6c63ff", 20, 125, 60)


    class LabelClass(customtkinter.CTkLabel):
        def __init__(self):
            super().__init__(master=RegisterWindow,
                             text="Register Here!",
                             font=('Arial', 50, 'bold'),
                             bg_color="white",
                             text_color="#6c63ff")
            self.place(y=30, x=170)

    RegisterLabel = LabelClass()

    ProfileFrame = FrameClass(RegisterFrame, 110, 110, 'white', 'white', 2, "#6c63ff", 1, 275, 30)

    Default_Profile = customtkinter.CTkImage(Image.open("avatar.png"), size=(100, 100))

    class ProfileLabelClass(customtkinter.CTkLabel):
        def __init__(self):
            super().__init__(master=ProfileFrame,
                             height=100,
                             width=100,
                             text="",
                             image=Default_Profile)
            self.place(x=5, y=5)

    Avatar = ProfileLabelClass()

    class Entries(customtkinter.CTkEntry):
        def __init__(self, placeholder_text, x, y, show):
            super().__init__(master=RegisterFrame,
                             placeholder_text=placeholder_text,
                             corner_radius=5,
                             border_color="#6c63ff",
                             border_width=1,
                             width=200,
                             text_color="white",
                             placeholder_text_color="skyblue",
                             show=show)
            self.place(x=x, y=y)

    FName = Entries("First Name", 115, 200, None)
    Email = Entries("E-mail", 325, 200, None)
    LName = Entries("Last Name", 115, 240, None)
    Mobile_Number = Entries("Mobile Number", 325, 240, None)
    MName = Entries("Middle Name", 115, 280, None)
    Current_Address = Entries("Current Address", 325, 280, None)
    Age = Entries("Age", 115, 360, None)
    Username = Entries("Username", 325, 320, None)
    Password = Entries("Password", 325, 360, "•")

    #Encapsulation
    class CustomComboBox(customtkinter.CTkComboBox):
        def __init__(self, master, values, x, y):
            super().__init__(
                master=master,
                values=values,
                corner_radius=5,
                border_color="#6c63ff",
                border_width=1,
                width=200,
                variable=customtkinter.StringVar(value="Sex"),
                text_color="skyblue",
                dropdown_text_color="white",
                dropdown_hover_color="skyblue",
                state="normal"
            )
            self.place(x=x, y=y)

    Sex_combobox = CustomComboBox(master=RegisterFrame, values=["Male", "Female"], x=115, y=320)

    class CustomButton:
        def __init__(self, master, text, x, y, command):
            self.button = customtkinter.CTkButton(
                master=master,
                width=100,
                corner_radius=5,
                border_color="#6c63ff",
                border_width=1,
                text_color="skyblue",
                bg_color="white",
                fg_color="black",
                text=text,
                command=command
            )
            self.button.place(x=x, y=y)

    class Buttons:
        def __init__(self):
            self.buttons = [
                CustomButton(RegisterFrame, "Submit", 325, 420, Register),
                CustomButton(RegisterFrame, "Return", 215, 420, Register),
                CustomButton(RegisterFrame, "Upload Profile", 280, 145, openfilepath)
            ]
    button_instances = Buttons()

    RegisterWindow.mainloop()
