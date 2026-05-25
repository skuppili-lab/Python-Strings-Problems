def view_expense():
    try:
        with open("expense.txt","r") as file:
            for line in file:
                amount,description,item=line.strip().split(",")
                print(f"Amount: {amount}, Description: {description}, Item: {item}")
    except FileNotFoundError:
        print("file is not there")
    finally:
        print("thank you!!")


def Add_expense():
    amount=int(input("Enter the amount spent:"))
    description=input("Enter the description:")
    item=input("Enter the item name:")
    try:
        with open("expense.txt","a") as file:
            print("\n")
            file.write(f"{amount},{description},{item}")
    except FileNotFoundError as e:
        print(f"{e}: File is not there")
    except TypeError as e:
        print(f"{e}:Invalid")
    finally:
        print("thank you!!")

def calculate_total():
    total=0
    try:
        with open("expense.txt","r") as file:
            for line in file:
                amount,description,item=line.strip().split(",")
                total+=int(amount)
        print(f"Total Expense:{total}")
    except FileNotFoundError:
        print("file is not there")
    finally:
        print("thank you!!")      


print("EXPENSE TRACKER")
print("1. View Expense")
print("2. Add  Expense")
print("3. Calculate Total expense")
    
choice=int(input("Enter your choice:"))
if choice == 1:
    view_expense()
elif choice ==2:
    Add_expense()
elif choice ==3:
    calculate_total()
else:
    print("Invalid choice")




