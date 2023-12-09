import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import base64
import io
import Database
from Database import fetchproducts, get_database_connection, close_database_connection, searchproducts, deleteproducts, users_fetchproducts, Checkout, update_name, update_quantity, update_price, update_category
from AddProducts import AddProducts
import AddProducts
from decimal import Decimal
def home(D_Username):
    customtkinter.set_appearance_mode("dark")
    SellerBuyerWindow = customtkinter.CTk()
    SellerBuyerWindow.geometry("1200x600")
    SellerBuyerWindow.title("RecycleMart")
    SellerBuyerWindow.resizable(False, False)

    class Label(customtkinter.CTkLabel):
        def __init__(self, master, height, width, text, image, fg_color, bg_color, text_color, font, x, y):
            super().__init__(master=master,
                             height=height,
                             width=width,
                             text=text,
                             image=image,
                             fg_color=fg_color,
                             bg_color=bg_color,
                             text_color=text_color,
                             font=font)
            self.place(x=x, y=y)

    class ScrollableFrame(customtkinter.CTkScrollableFrame):
        def __init__(self, master, height, fg_color, width, orientation, bg_color, corner_radius, border_color,
                     border_width, scrollbar_button_color, scrollbar_fg_color, x, y):
            super().__init__(master=master,
                             height=height,
                             fg_color=fg_color,
                             width=width,
                             orientation=orientation,
                             bg_color=bg_color,
                             corner_radius=corner_radius,
                             border_color=border_color,
                             border_width=border_width,
                             scrollbar_button_color=scrollbar_button_color,
                             scrollbar_fg_color=scrollbar_fg_color)
            self.place(x=x, y=y)

    class Menu(customtkinter.CTkOptionMenu):
        def __init__(self, master, values, corner_radius, width, text_color, dropdown_text_color, dropdown_hover_color,
                     state, fg_color, button_color, height, bg_color, variable, x, y):
            super().__init__(
                master=master,
                bg_color=bg_color,
                values=values,
                corner_radius=corner_radius,
                width=width,
                variable=variable,
                text_color=text_color,
                height=height,
                dropdown_text_color=dropdown_text_color,
                dropdown_hover_color=dropdown_hover_color,
                fg_color=fg_color,
                state=state,
                button_color=button_color
            )
            self.place(x=x, y=y)

    class Button(customtkinter.CTkButton):
        def __init__(self, master, height, width, image, text, bg_color, command, fg_color, hover_color, border_color,
                     x, y):
            super().__init__(master=master,
                             height=height,
                             width=width,
                             image=image,
                             text=text,
                             bg_color=bg_color,
                             fg_color=fg_color,
                             hover_color=hover_color,
                             border_color=border_color,
                             command=command)
            self.place(y=y, x=x)

    class Entry(customtkinter.CTkEntry):
        def __init__(self, master, height, width, fg_color, border_color, bg_color, text_color, placeholder_text, placeholder_text_color, x, y):
            super().__init__(master=master,
                             height=height,
                             width=width,
                             fg_color=fg_color,
                             border_color=border_color,
                             bg_color=bg_color,
                             text_color=text_color,
                             placeholder_text=placeholder_text,
                             placeholder_text_color=placeholder_text_color)
            self.place(x=x, y=y)

    class CustomTabView(customtkinter.CTkTabview):
        def __init__(self, master, height, width, fg_color, segmented_button_fg_color, segmented_button_unselected_color, segmented_button_selected_color, segmented_button_selected_hover_color, text_color, border_color, border_width, x, y):
            super().__init__(
                master=master,
                height=height,
                width=width,
                fg_color=fg_color,
                segmented_button_fg_color=segmented_button_fg_color,
                segmented_button_unselected_color=segmented_button_unselected_color,
                segmented_button_selected_color=segmented_button_selected_color,
                segmented_button_selected_hover_color=segmented_button_selected_hover_color,
                text_color=text_color,
                border_color=border_color,
                border_width=border_width)
            self.place(x=x, y=y)

    class Frame(customtkinter.CTkFrame):
        def __init__(self, master, height, width, fg_color, border_color, border_width, corner_radius, x, y):
            super().__init__(master=master,
                             height=height,
                             corner_radius=corner_radius,
                             width=width,
                             border_color=border_color,
                             border_width=border_width,
                             fg_color=fg_color)
            self.place(x=x, y=y)


    All_In = CustomTabView(SellerBuyerWindow, 600, 1200, "black", "green", "white", "yellow", "white", "green", "white", 0, 0, 0, )
    AboutTab = All_In.add("About")
    Recyclemart = All_In.add("Buy Materials")
    SellandRecycle = All_In.add("Sell Materials")
    All_In.set("About")

    def refresh_sframe():
        for widget in SFrame.winfo_children():
            widget.destroy()

        BuyMaterials()




    def BuyMaterials():

        def search_products():
            product_name = SearchBar.get()
            product_category = Categories.get()
            product_sort = Sort.get()

            search_result = Database.searchproducts(product_name, product_category, product_sort)

            if search_result:

                for widget in SFrame.winfo_children():
                    widget.destroy()

                for index, BuyersProductDetails in enumerate(search_result):
                    row = index // 4
                    col = index % 4

                    BuyersItemFrame = customtkinter.CTkFrame(master=SFrame, fg_color="#8bd3dd", height=200, width=190)
                    BuyersItemFrame.grid(row=row, column=col, pady=10, padx=10)

                    YourProductImage = BuyersProductDetails[0]

                    if YourProductImage:

                        try:
                            ItemImage = Image.open(YourProductImage)
                            YourDefaultProduct = customtkinter.CTkImage(ItemImage, size=(150, 140))

                            ProductFrame = customtkinter.CTkFrame(master=BuyersItemFrame, fg_color="#8bd3dd")
                            ProductFrame.grid(row=0, column=0, pady=3, padx=3)

                            ProductImageLabel = customtkinter.CTkLabel(master=ProductFrame, height=140, width=150,
                                                                       image=YourDefaultProduct, text="")
                            ProductImageLabel.grid(row=0, column=0)

                            BuyerProductName = customtkinter.CTkLabel(master=BuyersItemFrame, height=10, width=150,
                                                                      text=f"Name: {BuyersProductDetails[1]}",
                                                                      text_color="#001858",
                                                                      font=('Arial', 10, 'bold'))
                            BuyerProductName.grid(column=0, row=1, pady=1, padx=2)

                            BuyerProductQuantity = customtkinter.CTkLabel(master=BuyersItemFrame, height=10, width=150,
                                                                          text=f"Quantity: {BuyersProductDetails[2]} Pieces",
                                                                          text_color="#001858",
                                                                          font=('Arial', 10, 'bold'))
                            BuyerProductQuantity.grid(column=0, row=2, pady=1, padx=2)

                            BuyerProductCategory = customtkinter.CTkLabel(master=BuyersItemFrame, height=10, width=150,
                                                                          text=f"Category: {BuyersProductDetails[3]}",
                                                                          text_color="#001858",
                                                                          font=('Arial', 10, 'bold'))
                            BuyerProductCategory.grid(column=0, row=3, pady=1, padx=2)

                            BuyerProductPrice = customtkinter.CTkLabel(master=BuyersItemFrame, height=10, width=150,
                                                                       text=f"Price: ₱ {BuyersProductDetails[4]}",
                                                                       text_color="#001858", font=('Arial', 10, 'bold'))
                            BuyerProductPrice.grid(column=0, row=4, pady=1, padx=2)

                            addCartbtn = customtkinter.CTkButton(master=BuyersItemFrame, height=20, width=150,
                                                                 text="Buy Now", fg_color="#f582ae",
                                                                 text_color="#001858", font=('Arial Black', 12, 'bold'))
                            addCartbtn.grid(column=0, row=5, pady=3, padx=2)

                        except Exception as e:
                            print(f"Error displaying image: {e}")
                    else:
                        print("No image available")

        BuyerFrame = Frame(Recyclemart, 600, 1200, "#fef6e4", None, None, 0, 0, 0)
        AccountInfoFrame = Frame(Recyclemart, 520, 360, "#f3d2c1", "#001858", None, 0, 800, 13)
        ProfileFrame = Frame(AccountInfoFrame, 110, 110, "#f3d2c1", "#001858", 1, 0, 10, 20)
        Avatar = customtkinter.CTkImage(Image.open("avatar.png"), size=(100, 100))
        SFrame = ScrollableFrame(Recyclemart, 455, "#f3d2c1", 700, "vertical", "#fef6e4", 10, "#001858", 3, "#8bd3dd",
                                 "#f3d2c1", 50, 50)
        ProfileLabel = Label(ProfileFrame, 100, 100, "", Avatar, "white", "white", "white", None, 5, 5)

        name = Frame(AccountInfoFrame, 20, 70, "#f3d2c1", "#001858", 1, 0, 125, 20)
        id = Frame(AccountInfoFrame, 20, 70, "#f3d2c1", "#001858", 1, 0, 125, 45)
        num = Frame(AccountInfoFrame, 20, 70, "#f3d2c1", "#001858", 1, 0, 125, 70)
        add = Frame(AccountInfoFrame, 20, 70, "#f3d2c1", "#001858", 1, 0, 125, 95)

        namel = Label(name, 0, 0, "Name:", None, "#f3d2c1", "#FFFFDD", "#001858", ('Arial', 12, 'bold'), 10, 2.5)
        idl = Label(id, 0, 0, "ID:", None, "#f3d2c1", "#FFFFDD", "#001858", ('Arial', 12, 'bold'), 10, 2.5)
        numl = Label(num, 0, 0, "Number:", None, "#f3d2c1", "#FFFFDD", "#001858", ('Arial', 12, 'bold'), 10, 2.5)
        addl = Label(add, 0, 0, "Address", None, "#f3d2c1", "#FFFFDD", "#001858", ('Arial', 12, 'bold'), 10, 2.5)
        Ename = Label(AccountInfoFrame, 0, 0, "Name", None, "#f3d2c1", "#FFFFDD", "#001858", ('Arial', 12, 'bold'), 200, 20)
        EId = Label(AccountInfoFrame, 0, 0, "ID", None, "#f3d2c1", "#FFFFDD", "#001858", ('Arial', 12, 'bold'), 200, 45)
        Enumber = Label(AccountInfoFrame, 0, 0, "Number", None, "#f3d2c1", "#FFFFDD", "#001858", ('Arial', 12, 'bold'), 200,
                        70)
        Eaddress = Label(AccountInfoFrame, 0, 0, "Address", None, "#f3d2c1", "#FFFFDD", "#001858", ('Arial', 12, 'bold'),
                         200, 95)

        fname = Database.fetchname(D_Username)
        fetchid = Database.fetchid(D_Username)
        fetchnum = Database.fetchnumber(D_Username)
        fetchadd = Database.fetchaddress(D_Username)
        fetchprofile = Database.fetchprofile(D_Username)

        id = fetchid[0]
        AddProducts.user_id(id)


        if fname:
            Ename.configure(text=fname[0])

        if fetchid:
            id = fetchid[0]
            EId.configure(text=id)

        if fetchnum:
            Enumber.configure(text=fetchnum[0])

        if fetchadd:
            Eaddress.configure(text=fetchadd[0])

        if fetchprofile:
            imagepath = fetchprofile[0]
            try:
                image = Image.open(imagepath)
                userprofile = customtkinter.CTkImage(image, size=(100, 100))
                ProfileLabel.configure(image=userprofile)
            except Exception as e:
                print(f"Error loading image: {e}")
        else:
            print("not found")

        SearchBar = Entry(Recyclemart, 25, 300, "#8bd3dd", "#001858", "#fef6e4", "#001858", "Search", "#001858", 400, 15)

        search = customtkinter.CTkImage(Image.open("search.png"), size=(30, 30))

        SearchBtn = Button(Recyclemart, 40, 40, search, "", "#fef6e4", search_products, "#f582ae", "#8bd3dd", "#001858", 710, 5)

        Cart = CustomTabView(AccountInfoFrame, 330, 320, "#f3d2c1", "#f3d2c1", "#8bd3dd", "#f582ae", "#f582ae",
                                "#001858", "#001858", 1, 20, 140)
        yourCart = Cart.add("Your Cart")
        Cart.set("Your Cart")


        Sort = Menu(Recyclemart, ["Price Desc", "Price Asc", "Name Desc", "Name Asc"], 2, 140, "#265073", "white",
                    "#FF8F8F", "normal", "#8bd3dd", "#f582ae", 25, "#fef6e4", customtkinter.StringVar(value="Sort"), 80,
                    15)
        Categories = Menu(Recyclemart,
                          ["All","Plastic Bottles", "Glass Bottles", "Newspaper", "Aluminum cans", "Hard Paper", "Metal", "Others"], 2, 140,
                          "#265073", "white", "#FF8F8F", "normal", "#8bd3dd", "#f582ae", 25, "#fef6e4",
                          customtkinter.StringVar(value="Categories"), 230, 15)

        CartFrame = customtkinter.CTkScrollableFrame(master=yourCart, width=280, height=220, fg_color="#f3d2c1",
                                                     bg_color="#f3d2c1", scrollbar_fg_color="#f3d2c1",
                                                     border_width=0, scrollbar_button_hover_color="#f3d2c1",
                                                     scrollbar_button_color="#f3d2c1",
                                                     label_font=('Arial', 15, 'bold'))
        CartFrame.grid(row=0, column=0)
        BuyersProduct = fetchproducts()


        ProductCart = []

        num_of_len = len(ProductCart)
        num_of_row = num_of_len + 1


        if BuyersProduct:
            def BuyersProductDetails():
                for index, BuyersProductDetails in enumerate(BuyersProduct):
                    row = index // 4
                    col = index % 4

                    productName = BuyersProductDetails[2]
                    productQuantity = BuyersProductDetails[3]
                    productID = BuyersProductDetails[0]
                    productPrice = (BuyersProductDetails[5])

                    def select_quantity(productName, productQuantity, productID, productPrice):
                        numQuantity = customtkinter.CTkInputDialog(text="Enter the number of quantity",
                                                                   title="Select Quantity")

                        try:
                            entered_quantity = int(numQuantity.get_input())
                            if entered_quantity > productQuantity:
                                messagebox.showerror(title="Error",
                                                     message=f"This product have only {productQuantity} pieces")
                            else:
                                print(productName, entered_quantity, productID, productPrice)
                                on_add_to_cart(productName, entered_quantity, productID, productPrice)
                                calculate_total(entered_quantity, productPrice, productID)
                        except ValueError:
                            messagebox.showerror(title="Error", message="Input a valid quantity")

                    def on_add_to_cart(product, quantity, productid, adding_price_on_cart):

                        adding_price_on_cart = adding_price_on_cart

                        for item in ProductCart:

                            if item[0] == product and item[2] == productid:
                                messagebox.showerror(title="Error", message=f"{product} is already in the cart.")
                                return
                        your_product_frame = customtkinter.CTkFrame(master=CartFrame, fg_color="#f3d2c1", bg_color="#f3d2c1", border_color="#8bd3dd", border_width=1, width=250)
                        your_product_frame.grid(sticky="w", pady=3)

                        product_label = customtkinter.CTkLabel(master=your_product_frame, text=f"Product: {product}", text_color="#001858", font=('Arial', 10, 'bold'), fg_color="#f3d2c1", height=10, width=20)
                        product_label.grid(row=num_of_row + 1, column=0, pady=3, padx=3)

                        product_quantity_in_cart = customtkinter.CTkLabel(master=your_product_frame, text=f"Quantity: {quantity}", height=10, width=70, font=('Arial', 10, 'bold'), fg_color="#f3d2c1", bg_color="#f3d2c1", text_color="#001858")
                        product_quantity_in_cart.grid(row=num_of_row + 1, column=2, pady=10, padx=5)

                        remove_image = customtkinter.CTkImage(Image.open("delete.png"), size=(15,15))

                        remove = customtkinter.CTkButton(master=your_product_frame, image=remove_image, text="", fg_color="#f3d2c1", bg_color="#f3d2c1", height=15, width=15, command=lambda pID = productid, pNAme = productName: remove_product(pID, productName))
                        remove.grid(row=num_of_row + 1, column=3, pady=3, padx=3, sticky = "e")

                        ProductCart.append((product, quantity, productid, adding_price_on_cart))
                        print(ProductCart)

                    BuyersItemFrame = customtkinter.CTkFrame(master=SFrame, fg_color="#8bd3dd", height=200, width=190)
                    BuyersItemFrame.grid(row=row, column=col, pady=10, padx=10)

                    YourProductImage = BuyersProductDetails[1]

                    if YourProductImage:
                        try:
                            ItemImage = Image.open(YourProductImage)
                            YourDefaultProduct = customtkinter.CTkImage(ItemImage, size=(150, 140))

                            ProductFrame = customtkinter.CTkFrame(master=BuyersItemFrame, fg_color="#8bd3dd")
                            ProductFrame.grid(row=0, column=0, pady=3, padx=3)

                            ProductImageLabel = customtkinter.CTkLabel(master=ProductFrame, height=140, width=150,
                                                                       image=YourDefaultProduct, text="")
                            ProductImageLabel.grid(row=0, column=0)

                        except Exception as e:
                            print(f"Error displaying image: {e}")
                    else:
                        print("No image available")



                    BuyerProductName = customtkinter.CTkLabel(master=BuyersItemFrame, height=10, width=150,
                                                              text=f"Name: {productName}",
                                                              text_color="#001858",
                                                              font=('Arial', 10, 'bold'))
                    BuyerProductName.grid(column=0, row=1, pady=1, padx=2)

                    BuyerProductQuantity = customtkinter.CTkLabel(master=BuyersItemFrame, height=10, width=150,
                                                                  text=f"Quantity: {productQuantity} Pieces",
                                                                  text_color="#001858",
                                                                  font=('Arial', 10, 'bold'))
                    BuyerProductQuantity.grid(column=0, row=2, pady=1, padx=2)

                    BuyerProductCategory = customtkinter.CTkLabel(master=BuyersItemFrame, height=10, width=150,
                                                                  text=f"Category: {BuyersProductDetails[4]}",
                                                                  text_color="#001858",
                                                                  font=('Arial', 10, 'bold'))
                    BuyerProductCategory.grid(column=0, row=3, pady=1, padx=2)

                    BuyerProductPrice = customtkinter.CTkLabel(master=BuyersItemFrame, height=10, width=150,
                                                               text=f"Price: ₱ {productPrice}",
                                                               text_color="#001858", font=('Arial', 10, 'bold'))
                    BuyerProductPrice.grid(column=0, row=4, pady=1, padx=2)

                    addCartbtn = customtkinter.CTkButton(master=BuyersItemFrame, height=20, width=150,
                                                         text="Add to Cart", fg_color="#f582ae",
                                                         text_color="#001858", font=('Arial Black', 12, 'bold'), command=lambda name=productName, quantity=productQuantity, id=productID, price=productPrice: select_quantity(name, quantity, id, price))
                    addCartbtn.grid(column=0, row=5, pady=3, padx=2)

                def calculate_total(calculate_quantity, calculate_price, productID):
                    print()


                    total_expense = sum(item[3] * Decimal(item[1]) for item in ProductCart)
                    Total.configure(text=f"Total: ₱ {total_expense}")




                def remove_product(productid, productName):
                    print(f"Removing product with id {productid} and name {productName}")
                    print(f"Current items in cart: {ProductCart}")

                    cart_items_to_remove = [item for item in ProductCart if
                                            item[2] == productid and item[0] == productName]

                    print(f"Items to remove: {cart_items_to_remove}")

                    for item in cart_items_to_remove:
                        ProductCart.remove(item)

                    for widget in CartFrame.winfo_children():
                        widget.destroy()
                    print(f"Items with id {productid} and name {productName} removed from the cart")
                    print(f"current items from cart {ProductCart}")
            BuyersProductDetails()


        def checkout():
            for item in ProductCart:
                q = item[1]
                i = item[2]
                Checkout(q, i)


        Total = customtkinter.CTkLabel(master=AccountInfoFrame, text=f"Total: ", height=35,
                                       font=('Arial Black', 20, 'bold'), text_color="#001858")
        Total.place(y=470, x=30)

        BuyProduct = customtkinter.CTkButton(master=AccountInfoFrame, width=80, height=30, text="Check Out",
                                             font=('Arial Black', 15, 'bold'), text_color="#001858",
                                             fg_color="#f582ae",
                                             command=checkout)
        BuyProduct.place(y= 480, x = 230)



    def About():
        AboutBG = customtkinter.CTkImage(Image.open("About.png"), size = (1200, 600))
        AboutLabel = Label(AboutTab, 100, 100, "", AboutBG, "white", "white", "white", None, 0, 0)

    def SellerTab():

        def search_result():
            product_name = SearchBar1.get()
            product_category = Categories1.get()
            product_sort = Sort1.get()
            search_results = Database.searchproducts(product_name, product_category, product_sort)
            print(search_results)
            if search_results:
                for widget in DFrame.winfo_children():
                    widget.destroy()

                for index, product in enumerate(search_results):
                    row = index // 4
                    col = index % 4

                    ItemFrame = customtkinter.CTkFrame(master=DFrame, fg_color="#a786df", border_color="#d9d4e7",
                                                       border_width=0.5)
                    ItemFrame.grid(row=row, column=col, padx=40, pady=20)

                    productImage = product[0]

                    if productImage:
                        try:
                            ItemImage = Image.open(productImage)
                            DefaultProduct = customtkinter.CTkImage(ItemImage, size=(150, 140))

                            ProductFrame = customtkinter.CTkFrame(master=ItemFrame, fg_color="#a786df")
                            ProductFrame.grid(row=0, column=0, pady=5, padx=5)

                            ProductImageLabel = customtkinter.CTkLabel(master=ProductFrame, height=140, width=150,
                                                                       image=DefaultProduct, text="")
                            ProductImageLabel.grid(row=0, column=0)

                        except:
                            pass

                    else:
                        print("no image")

                    search = customtkinter.CTkImage(Image.open("search.png"), size=(30, 30))


                    UpdateButton = customtkinter.CTkButton(master=ItemFrame, width=50, height=15, text="Update",
                                                           font=('Arial Black', 15, 'bold'), border_color="",
                                                           command=None)
                    UpdateButton.grid(row=5, column=0, pady=5, sticky="e", padx=3)

                    DeleteButton = customtkinter.CTkButton(master=ItemFrame, width=50, height=15, text="Delete",
                                                           font=('Arial Black', 15, 'bold'), border_color="",
                                                           command=DeleteProduct)
                    DeleteButton.grid(row=5, column=0, rowspan=1, pady=5, sticky="w", padx=3)

        def DeleteProduct(productid):
            try:
                Database.deleteproducts(productid)
                refresh_dframe()
            except Exception as e:
                print(f"{e}")

        pending_updates = {}

        def new_name(product_id):
            enter_new_name = customtkinter.CTkInputDialog(text="Enter New Product Name", title="Update Name")
            new_name_value = enter_new_name.get_input()

            if new_name_value:
                pending_updates[product_id] = {'name': new_name_value}
                print(pending_updates)
            else:
                print("No new name entered")

        def new_quantity(product_id):
            enter_new_quantity = customtkinter.CTkInputDialog(text="Enter New Product Quantity",
                                                              title="Update Quantity")
            new_quantity_value = int(enter_new_quantity.get_input())

            if new_quantity_value:
                pending_updates[product_id] = {'quantity': new_quantity_value}
                print(pending_updates)
            else:
                print("No new quantity entered")

        def new_price(product_id):
            enter_new_price = customtkinter.CTkInputDialog(text="Enter New Product Price", title="Update Price")
            new_price_value = float(enter_new_price.get_input())

            if new_price_value:
                pending_updates[product_id] = {'price': new_price_value}
                print(pending_updates)
            else:
                print("No new price entered")

        def new_category(product_id):
            enter_new_category = customtkinter.CTkInputDialog(text="Enter New Product Category",
                                                              title="Update Category")
            new_category_value = enter_new_category.get_input()

            if new_category_value:
                pending_updates[product_id] = {'category': new_category_value}
                print(pending_updates)
            else:
                print("No new category entered")

        def commit_updates():
            try:
                for product_id, updates in pending_updates.items():
                    if 'name' in updates:
                        update_name(updates['name'], product_id)
                    if 'quantity' in updates:
                        update_quantity(updates['quantity'], product_id)
                    if 'price' in updates:
                        update_price(updates['price'], product_id)
                    if 'category' in updates:
                        update_category(updates['category'], product_id)

                pending_updates.clear()

            except Exception as e:
                print(f"Error committing updates: {e}")

        def AddP():
            AddProducts.AddProducts()

        InventoryFrame = Frame(SellandRecycle, 600, 1200, "#f9f8fc", None, None, 0, 0, 0)
        InventoryFrame1 = customtkinter.CTkFrame(master=SellandRecycle, height=50, width=693, fg_color="#fec7d7",bg_color="#f9f8fc", border_color="#0e172c", border_width=3, corner_radius=10)
        InventoryFrame1.place(x=170, y=30)

        DFrame = ScrollableFrame(InventoryFrame, 400, "#fec7d7", 1000, "vertical", "#f9f8fc", 10, "#0e172c", 3, "#a786df",
                                 "#fec7d7", 75, 100)

        add = customtkinter.CTkImage(Image.open("addProduct.png"), size=(50, 50))

        search = customtkinter.CTkImage(Image.open("search.png"), size=(30, 30))

        Addbtn = Button(InventoryFrame, 50, 50, add, "", "#f9f8fc", AddP, "#f9f8fc", "white", "#f9f8fc", 880, 25)
        SearchBar1 = Entry(InventoryFrame1, 30, 300, "#a786df", "#0e172c", "#fec7d7", "#0e172c", "Search", "black", 330,
                           10)

        SearchBtn1 = Button(InventoryFrame1, 30, 30, search, "", "#fec7d7",
                            search_result, "#fec7d7", "gray", "#fec7d7", 640, 5)

        Sort1 = Menu(InventoryFrame1, ["Price Desc", "Price Asc", "Name Desc", "Name Asc"], 2, 150, "#265073",
                     "white", "#FF8F8F", "normal", "#a786df", "#fffffe", 30, "#fec7d7",
                     customtkinter.StringVar(value="Sort"), 10, 10)
        Categories1 = Menu(InventoryFrame1,
                           ["Plastic Bottles", "Glass Bottles", "Newspaper", "Aluminum cans", "Hard Paper", "Metal",
                            "Others"], 2,
                           150, "#265073", "white", "#FF8F8F", "normal", "#a786df", "#fffffe", 30, "#fec7d7",
                           customtkinter.StringVar(value="Categories"), 170, 10)

        fetchid = Database.fetchid(D_Username)
        user_id = fetchid[0]

        user_products = Database.users_fetchproducts(user_id)

        for index, product in enumerate(user_products):
            row = index // 4
            col = index % 4

            ItemFrame = customtkinter.CTkFrame(master=DFrame, fg_color="#a786df", border_color="#d9d4e7", border_width=0.5)
            ItemFrame.grid(row=row, column=col, padx=40, pady=20)

            productImage = product[1]

            if productImage:
                try:
                    ItemImage = Image.open(productImage)
                    DefaultProduct = customtkinter.CTkImage(ItemImage, size=(150, 140))

                    ProductFrame = customtkinter.CTkFrame(master=ItemFrame, fg_color="#a786df")
                    ProductFrame.grid(row=0, column=0, pady=5, padx=5)

                    ProductImageLabel = customtkinter.CTkLabel(master=ProductFrame, height=140, width=150,
                                                               image=DefaultProduct, text="")
                    ProductImageLabel.grid(row=0, column=0)

                except:
                    pass

            else:
                print("no image")



            LabelProductName = customtkinter.CTkLabel(master=ItemFrame, text="Product: ", width=60, height=15, font=('Arial', 10, 'bold'),text_color="#fffffe")
            LabelProductName.grid(row=1, column=0, padx=3, pady=1, sticky="w")

            ProductName = customtkinter.CTkButton(master=ItemFrame, text=product[2], width=80, height=15, font=('Arial', 10), fg_color="#0e172c", border_color="#fec7d7", text_color="#fffffe", border_width=0.5, command=lambda product_id = product[0]: new_name(product_id))
            ProductName.grid(row=1, column=0, rowspan=1,  padx=3, pady=1, sticky="e")

            LabelProductQuantity = customtkinter.CTkLabel(master=ItemFrame, text="Quantity: ", width=60, height=15, font=('Arial', 10, 'bold'), text_color="#fffffe")
            LabelProductQuantity.grid(row=2, column=0,  pady=1,  padx=3, sticky="w")

            ProductQuantity = customtkinter.CTkButton(master=ItemFrame, text=product[3], width=80, height=15, font=('Arial', 10), fg_color="#0e172c", border_color="#fec7d7", text_color="#fffffe", border_width=0.5, command=lambda product_id = product[0]: new_quantity(product_id))
            ProductQuantity.grid(row=2, column=0, rowspan=1, pady=1,  padx=3, sticky="e")

            LabelProductPrice = customtkinter.CTkLabel(master=ItemFrame, text="Price: ", width=60, height=15, font=('Arial', 10, 'bold'), text_color="#fffffe")
            LabelProductPrice.grid(row=3, column=0, pady=1, sticky="w",  padx=3)

            ProductPrice = customtkinter.CTkButton(master=ItemFrame, text=f"₱ {product[5]}", width=80, height=15, font=('Arial', 10), fg_color="#0e172c", border_color="#fec7d7", text_color="#fffffe", border_width=0.5,command=lambda product_id = product[0]: new_price(product_id))
            ProductPrice.grid(row=3, column=0, rowspan=1, pady=1, sticky="e",  padx=3)

            LabelProductCategory = customtkinter.CTkLabel(master=ItemFrame, text="Category: ", width=60, height=15, text_color="#fffffe",
                                                       font=('Arial', 10, 'bold'))
            LabelProductCategory.grid(row=4, column=0, pady=1, sticky="w", padx=3)

            ProductCategory = customtkinter.CTkButton(master=ItemFrame, text=product[4], width=80, height=15, font=('Arial', 10), fg_color="#0e172c", border_color="#fec7d7", text_color="#fffffe", border_width=0.5, command=lambda product_id = product[0]: new_category(product_id))
            ProductCategory.grid(row=4, column=0, rowspan=1, pady=1, sticky="e", padx=3)

            UpdateButton = customtkinter.CTkButton(master=ItemFrame, width=50, height=15, text="Update", font=('Arial Black', 15, 'bold'), border_color="", command = commit_updates)

            UpdateButton.grid(row=5, column=0, pady=5,sticky="e",  padx=3)


            DeleteButton = customtkinter.CTkButton(master=ItemFrame, width=50, height=15, text="Delete", font=('Arial Black', 15, 'bold'), border_color="", command=lambda productid=product[0]: DeleteProduct(productid))
            DeleteButton.grid(row=5, column=0, rowspan=1, pady=5, sticky = "w",  padx=3)




    BuyMaterials()
    SellerTab()
    About()
    SellerBuyerWindow.mainloop()
