
import qrcode

products = []

def read_from_database():
    f = open("database.txt", "r")
    line = f.read().split("\n")

    for i in range (len(line)-1):

        result = line[i].split(",")
        my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        products.append(my_dict)

    f.close()

def write_to_database():
    f = open("database.txt", "w")

    for row in products:
        a = row["code"] + ", " + row["name"] + ", " + row["price"] + ", " + row["count"] + "\n"
        f.write(a)
    
    f.close()

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
    code = input("Enter product code: ")
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    count = input("Enter product count: ")
    products.append({"code": code, "name": name, "price": price, "count": count})

def edit():
    edited_code = input("Enter code: ")
    for row in products:

        if edited_code == row["code"]:
            print("1: Name")
            print("2: Price")
            print("3: Count")
            a = int(input("Enter the number of item that you want change: "))
            b = input("Enter your edited: ")

            if a == 1:
                row["name"] = b
            elif a == 2:
                row["price"] = b
            elif a == 3:
                row["count"] = b
            
            print("Information updated successfully")
            break

    else:
        print("There is no product with this code!")

def remove():
    removed_code = input("Enter code: ")
    for row in products:

        if removed_code == row["code"]:
            del row["code"]
            del row["name"]
            del row["price"]
            del row["count"]
            print("The product has been successfully removed")
            break

    else:
        print("There is no product with this code!")

def search():
    searched_code = input("Enter code: ")
    for row in products:

        if searched_code == row["code"]:
            print(row["code"], row["name"], row["price"], row["count"])
            break
    else:
        print("There is no product with this code!")

def show_list():
    print("Code\t\tName\t\tPrice")
    for row in products:
        print(row["code"], "\t\t", row["name"], "\t\t", row["price"])

def buy():

    receipt = []
    sum = 0
    while True:

        a = input("Want you continue? ('yes' or 'no') ")

        if a == "yes":
            code = input("Enter product code: ")

            for row in products:

                if code == row["code"]:
                    number = int(input("Enter the number of product: "))
                    
                    if number > int(row["count"]):
                        print("Insufficient inventory!")
                    else:
                        residual = int(row["count"]) - number
                        row["count"] = str(residual)
                        p = int(row["price"])
                        bill = number * p
                        sum = sum + bill
                        receipt.append({"code": row["code"], "name": row["name"], "price": row["price"], "count": number})
                        break
                    
            else:
                print("There is no product with this code!")
        
        elif a == "no":
            print(receipt)
            print("sum receipt = ", sum)
            break

def qr_code():
    code = input("Enter product code: ")
    for row in products:

        if code == row["code"]:
            a = row["name"]
            b = row["price"]
            c = row["count"]
    x = a + b + c
    img = qrcode.make(x)
    img.save("qrcode.png")

print("welcome to store")

while True:
    read_from_database()
    show_menu()
    choice = int(input("enter your choice: "))

    print(products)

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
        write_to_database()
        exit(0)
    else:
        print("your choice should be between 1 to 8")
