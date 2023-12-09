import mysql.connector
from tkinter import messagebox
from tkinter.messagebox import askyesno

def get_database_connection():
    return mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='project'
    )
def close_database_connection(connection):
    if connection.is_connected():
        connection.close()
def insert_user_data(connection, data):
    cursor = connection.cursor()

    insert_data = (
        "INSERT INTO `users` (first_name, last_name, middle_name, sex, age, email, mobile_number, current_address, username, password, profile_image) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    cursor.execute(insert_data, data)
    connection.commit()
    cursor.close()
def insert_product(connection, data):
    cursor = connection.cursor()

    check_product_query = "SELECT * FROM `products` WHERE id = %s AND name = %s"
    cursor.execute(check_product_query, (data[0], data[2]))
    existing_product = cursor.fetchone()

    if existing_product:
        messagebox.showerror(title="Error", message="You are already selling this product")

    else:
        insert_data = "INSERT INTO `products` (id, product_image, name, quantity, category, price) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_data, data)
        connection.commit()
        cursor.close()
def loginvalidator(connection, data):
    cursor = connection.cursor()

    validate_user_pass = ("SELECT * FROM users WHERE username = %s AND password = %s")
    cursor.execute(validate_user_pass, data)
    data = cursor.fetchone()
    connection.commit()
    cursor.close()
    return data
def fetchname(D_Username):
    connection = get_database_connection()
    cursor = connection.cursor()
    fetch_query = "SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE username = %s"
    cursor.execute(fetch_query, (D_Username,))
    fname = cursor.fetchone()
    cursor.close()
    close_database_connection(connection)
    return fname
def fetchid(D_Username):
    connection = get_database_connection()
    cursor = connection.cursor()
    fetch_query = "SELECT id FROM users WHERE username = %s"
    cursor.execute(fetch_query, (D_Username,))
    fetchid = cursor.fetchone()
    cursor.close()
    close_database_connection(connection)
    return fetchid
def fetchnumber(D_Username):
    connection = get_database_connection()
    cursor = connection.cursor()
    fetch_query = "SELECT mobile_number FROM users WHERE username = %s"
    cursor.execute(fetch_query, (D_Username,))
    fetchnumber = cursor.fetchone()
    cursor.close()
    close_database_connection(connection)
    return fetchnumber
def fetchaddress(D_Username):
    connection = get_database_connection()
    cursor = connection.cursor()
    fetch_query = "SELECT current_address FROM users WHERE username = %s"
    cursor.execute(fetch_query, (D_Username,))
    fetchaddress = cursor.fetchone()
    cursor.close()
    close_database_connection(connection)
    return fetchaddress
def fetchprofile(D_Username):
    connection = get_database_connection()
    cursor = connection.cursor()
    fetch_query = "SELECT profile_image FROM users WHERE username = %s"
    cursor.execute(fetch_query, (D_Username,))
    fetchprofile = cursor.fetchone()
    cursor.close()
    close_database_connection(connection)
    return fetchprofile
def users_fetchproducts(user_id):
    connection = get_database_connection()
    cursor = connection.cursor()
    fetch_query = "SELECT product_id, product_image, name, quantity, category, price FROM products WHERE id = %s"
    cursor.execute(fetch_query, (user_id,))
    users_products = cursor.fetchall()
    cursor.close()
    close_database_connection(connection)
    return users_products
def fetchproducts():
    connection = get_database_connection()
    cursor = connection.cursor()
    fetch_query = "SELECT product_id, product_image, name, quantity, category, price FROM products"
    cursor.execute(fetch_query)
    products = cursor.fetchall()
    cursor.close()
    close_database_connection(connection)
    return products
def deleteproducts(productid):
    confirm_deletion = askyesno(title="Delete", message="Are you sure you want to delete this product?")
    if confirm_deletion:
        connection = get_database_connection()
        cursor = connection.cursor()
        delete = "DELETE FROM products WHERE product_id = %s"
        cursor.execute(delete, (productid,))
        connection.commit()
        cursor.close()
        close_database_connection(connection)
def searchproducts(product_name=None, product_category=None, product_sort=None):
    connection = get_database_connection()
    cursor = connection.cursor()

    search_query = "SELECT product_image, name, quantity, category, price FROM products WHERE 1=1"

    params = []

    if product_name:
        search_query += " AND name = %s"
        params.append(product_name)
    else:
        product_name = 'All'

    if product_category and product_category == 'Categories':
        product_category = 'All'

    if product_category and product_category != 'All':
        search_query += " AND category = %s"
        params.append(product_category)
    else:
        product_category = 'All'
    if product_sort:
        if product_sort == "Name Asc":
            search_query += " ORDER BY name ASC"
        elif product_sort == "Name Desc":
            search_query += " ORDER BY name DESC"
        elif product_sort == "Price Asc":
            search_query += " ORDER BY price ASC"
        elif product_sort == "Price Desc":
            search_query += " ORDER BY price DESC"

    cursor.execute(search_query, tuple(params))
    search_results = cursor.fetchall()
    cursor.close()
    close_database_connection(connection)
    return search_results
def update_name(new_name, product_id):
    try:
        confirmation = askyesno(title="Update Quantity", message="Update Name?")
        if confirmation:
            connection = get_database_connection()
            cursor = connection.cursor()

            update_name_query = "UPDATE products SET name = %s WHERE product_id = %s"
            cursor.execute(update_name_query, (new_name, product_id))

            connection.commit()
            cursor.close()
            close_database_connection(connection)

        print(f"Name updated successfully with an id of {product_id}")
    except Exception as e:
        print(f"Error updating name: {e}")
def update_quantity(new_quantity, product_id):
    try:
        confirmation = askyesno(title="Update Quantity", message="Update Quantity?")
        if confirmation:
            connection = get_database_connection()
            cursor = connection.cursor()

            update_name_query = "UPDATE products SET quantity = %s WHERE product_id = %s"
            cursor.execute(update_name_query, (new_quantity, product_id))
            connection.commit()
            cursor.close()
            close_database_connection(connection)
            print(f"Quantity updated successfully with an id of {product_id}")


    except Exception as e:
        print(f"Error updating name: {e}")
def update_price(new_price, product_id):
    try:
        confirmation = askyesno(title="Update Quantity", message="Update Price?")
        if confirmation:
            connection = get_database_connection()
            cursor = connection.cursor()

            update_name_query = "UPDATE products SET price = %s WHERE product_id = %s"
            cursor.execute(update_name_query, (new_price, product_id))

            connection.commit()
            cursor.close()
            close_database_connection(connection)
            print(f"Price updated successfully with an id of {product_id}")

    except Exception as e:
        print(f"Error updating name: {e}")
def update_category(new_category, product_id):
    try:
        confirmation = askyesno(title="Update Quantity", message="Update Category?")
        if confirmation:
            connection = get_database_connection()
            cursor = connection.cursor()

            update_name_query = "UPDATE products SET category = %s WHERE product_id = %s"
            cursor.execute(update_name_query, (new_category, product_id))

            connection.commit()
            cursor.close()
            close_database_connection(connection)
            print(f"Category updated successfully with an id of {product_id}")

    except Exception as e:
        print(f"Error updating name: {e}")

def Checkout(quantity, product_id):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        subtraction_query = "UPDATE products SET quantity = quantity - %s WHERE product_id = %s"
        cursor.execute(subtraction_query, (quantity, product_id))

        if cursor.rowcount == 0:
            print(f"No rows updated - product ID {product_id} not found.")
        else:
            messagebox.showinfo(title="Status", message="Transaction Complete")

        cursor.execute("SELECT quantity FROM products WHERE product_id = %s", (product_id,))
        updated_quantity = cursor.fetchone()[0]

        if updated_quantity <= 0:
            cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            print(f"Product ID {product_id} removed as quantity reached zero.")

        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"Error subtracting quantity: {e}")





