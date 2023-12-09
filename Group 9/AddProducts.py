import customtkinter
import mysql.connector
from PIL import Image
import Database
from Database import get_database_connection, close_database_connection, insert_product
from tkinter import filedialog
from Widgets import *
from tkinter import messagebox
from Database import fetchid, fetchproducts
global ProductEntryName, ProductEntryQuantity, ProductEntryPrice, ProductCategoriesEntry


def user_id(value):
    global user_id
    user_id = value
def AddProducts():
    def InsertProduct():
        global user_id
        productname = ProductEntryName.get()
        productquantity = ProductEntryQuantity.get()
        productprice = ProductEntryPrice.get()
        productcategory = ProductCategoriesEntry.get()

        try:
            if productname and productquantity and productcategory and productprice:
                connection = get_database_connection()
                insert_data = (user_id, image_path, productname, productquantity, productcategory, productprice)

                cursor = connection.cursor()

                check_product_query = "SELECT * FROM `products` WHERE id = %s AND name = %s"
                cursor.execute(check_product_query, (user_id, productname))
                existing_product = cursor.fetchone()

                if existing_product:
                    messagebox.showerror(title="Error", message="You are already selling this product")
                else:
                    insert_product(connection, insert_data)
                    messagebox.showinfo(title="Status", message="Added Successfully")

                close_database_connection(connection)
            else:
                messagebox.showinfo(title="Status", message="All fields are required")
        except Exception as e:
            print(f"Error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            print(f"Error: {e}")


    def openfilepath():
        global image_path
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                image = customtkinter.CTkImage(Image.open(file_path), size=(114, 114))
                ProductImage.configure(image=image)

                image_path = file_path
            except Exception:
                print(f"Error: {e}")

    Add = customtkinter.CTkToplevel()
    Add.geometry("600x300")
    Add.title("Add Products")
    Add.resizable(False, False)

    AddProductsFrame = Frame(Add, 250, 550, "sky blue", "black", 3, 10, 25, 25)
    ProductsFrame = Frame(AddProductsFrame, 170, 470, "white", "black", 3, 10, 40, 20)
    AddProductBtn = Button(AddProductsFrame, 30, 100, None, "Add Product", "sky blue", "black", "gray", "black", 225,200, InsertProduct)

    UploadProductBtn = Button(ProductsFrame, 30, 100, None, "Upload Product", "white", "black", "gray", "black", 20,
                              133, openfilepath)

    ProductName = Label(ProductsFrame, 30, 100, "Product Name:", None, "white", "white", "black", ('Arial', 15, 'bold'),
                        140, 10)
    ProductName = Label(ProductsFrame, 30, 100, "Product Quantity:", None, "white", "white", "black",
                        ('Arial', 15, 'bold'), 140, 50)
    ProductName = Label(ProductsFrame, 30, 100, "Product Price:", None, "white", "white", "black",
                        ('Arial', 15, 'bold'), 140, 90)
    ProductName = Label(ProductsFrame, 30, 100, "Product Catagory:", None, "white", "white", "black",
                        ('Arial', 15, 'bold'), 140, 130)

    ItemFrame = Frame(ProductsFrame, 120, 120, "white", "black", 3, 0, 10, 10)
    DefaultProduct = customtkinter.CTkImage(Image.open("DefaultProduct.png"), size=(100, 100))
    ProductImage = Label(ItemFrame, 114, 114, "", DefaultProduct, "white", "white", "white", ('Arial', 0, 'bold'), 3, 3)

    ProductEntryName = Entry(ProductsFrame, 30, 150, "white", "black", "white", "black", "Product Name", "gray", 270,
                             10)
    ProductEntryQuantity = Entry(ProductsFrame, 30, 150, "white", "black", "white", "black", "Product Quantity", "gray",
                                 270, 50)
    ProductEntryPrice = Entry(ProductsFrame, 30, 150, "white", "black", "white", "black", "Product Price", "gray", 270,
                              90)
    ProductCategoriesEntry = Menu(ProductsFrame,
                                  ["All","Plastic Bottles", "Glass Bottles", "Newspaper", "Aluminum cans", "Hard Paper", "Metal", "Others"], 3,
                                  150, "black", "black", "white", "normal", "white", "white", 30, "black",
                                  customtkinter.StringVar(value="Categories"), 270, 130)






