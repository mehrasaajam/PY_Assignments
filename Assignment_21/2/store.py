
import sqlite3
import qrcode


def show_menu():
    print("1: Add")
    print("2: Edit")
    print("3: Remove")
    print("4: Search")
    print("5: Show list")
    print("6: Buy")
    print("7: qr code")
    print("8: Exit")


def add():
    code_a = input("Enter product code: ")
    name_a = input("Enter product name: ")
    price_a = input("Enter product price: ")
    count_a = input("Enter product count: ")

    my_cursor.execute(f"INSERT INTO products(code,name,price,count) VALUES({code_a},'{name_a}',{price_a},{count_a})")
    connection.commit()


def edit():
    edited_code = input("Enter code: ")
    print("1: Name")
    print("2: Price")
    print("3: Count")
    a = int(input("Enter the number of item that you want change: "))
    b = input("Enter your edited: ")

    if a == 1:
        my_cursor.execute(f"UPDATE products SET name='{b}' WHERE code={edited_code}")
        print("Information updated successfully")
    elif a == 2:
        my_cursor.execute(f"UPDATE products SET price={b} WHERE code={edited_code}")
        print("Information updated successfully")
    elif a == 3:
        my_cursor.execute(f"UPDATE products SET count={b} WHERE code={edited_code}")
        print("Information updated successfully")
    else:
        print("There is no product with this code!")

    connection.commit()


def remove():
    removed_code = input("Enter code: ")
    my_cursor.execute(f"DELETE FROM products WHERE code={removed_code}")
    connection.commit()


def search():
    searched_code = input("Enter code: ")
    for data in my_cursor.execute(f"SELECT * FROM products WHERE code={searched_code}"):
        print(data)


def show_list():
    for data in my_cursor.execute("SELECT * FROM products"):
        print(data)


def buy():
    receipt = []
    sum = 0
    while True:

        a = input("Want you continue? ('yes' or 'no') ")

        if a == "yes":
            code_a = int(input("Enter product code: "))
            number = int(input("Enter the number of product: "))
            c = my_cursor.execute(f"SELECT count FROM products WHERE code={code_a}")
            count_a = int(c.fetchone()[0])
                    
            if number > count_a:
                print("Insufficient inventory!")
            else:
                residual = count_a - number
                p = my_cursor.execute(f"SELECT price FROM products WHERE code={code_a}")
                price_a = int(p.fetchone()[0])
                bill = number * price_a
                sum = sum + bill
                n = my_cursor.execute(f"SELECT name FROM products WHERE code={code_a}")
                name_a = str(n.fetchone()[0])
                receipt.append({"code": code_a, "name": name_a, "price": price_a, "count": number})
                my_cursor.execute(f"UPDATE products SET count={residual} WHERE code={code_a}")
                connection.commit()

        elif a == "no":
            print(receipt)
            print("sum receipt = ", sum)
            break


def qr_code():
    code_a = input("Enter product code: ")
    for data in my_cursor.execute(f"SELECT * FROM products WHERE code={code_a}"):
        img = qrcode.make(data)
        img.save("qrcode.png")



print("welcome to store")

connection = sqlite3.connect("store.db")
my_cursor = connection.cursor()

while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        qr_code()
    elif choice == 8:
        exit(0)
    else:
        print("your choice should be between 1 to 8")
