import json
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

def add_expense():

    try:
        with open("data.json", "r") as file:
            current_data = json.load(file)
    except json.JSONDecodeError:
        print(f"No existing record")
        current_data = {}
    except FileNotFoundError:
        print(f"File not found")
        current_data = {}
    


    expense = category = ""
    # category_list = ["Food", "Logistics", "Operation", "Maintenance"]

    while True:
        expense =input("Name of Expense: ").strip()
        if not expense:
            print("Expense can't be empty")
            continue
        break
    while True:
        category = input("Category: ").strip()
        if not category:
            print("Category can't be empty. Try Again. \n")
            continue
        
        break
        

    while True:
        try:
            amount = float((input("Amount: ")).strip())
            if amount < 0:
                print("Invalid: less than 0. \n")
                continue
            break

        except ValueError:
            print("Input an amount. Ex. 5000, 200, 10.00")
            continue
        

    description = (input("description: ")).strip()

    # Automating addition of Id to the new expense
    # Fetching the highest ID and increment by 1
    new_id = getnew_id(current_data)
    current_data[new_id] = {
        "expense":expense,
        "category":category, 
        "amount":amount, 
        "description":description,
        }

    with open("data.json", "w") as file:
        json.dump(current_data, file, indent=4)

def viewexpenses():
    view =input("select Category:")
    try:
        with open("data.json", "r") as file:
            current_data = json.load(file)
    except json.JSONDecodeError:
        print("File is Empty")
        return
    print("*"*65)
    print(f'{"ID":20}{"EXPENSE":20}{"CATEGORY":20}{"AMOUNT":20}')
    for exp_id, ex in current_data.items():
       print(f"{exp_id:20} {ex['expense']:20}{ex['category']:20}{ex['amount']:20.2f}")
        
def total_expense():
    totaled_expense = 0
    try:
        with open("data.json", "r") as file:
            current_data = json.load(file)
    except FileNotFoundError as fnf:
        print("File Not Found")
        return
    except json.JSONDecodeError as e:
        print("invalid JSON")
        return

    for _, record in current_data.items():
        a =record["amount"]
        totaled_expense += a 

    print(totaled_expense)

def spend_category():
    user_cat = input("Input Category")
    cat_total = 0
    try:
        with open("data.json", "r") as file:
            current_data = json.load(file)
            for _, exp in current_data.items():
                if exp["category"] == user_cat:
                    cat_total += exp["amount"]
    except FileNotFoundError:
        return "File not Found"
    except json.JSONDecodeError:
        return "Invalid"
    return cat_total


def delete_expense():

    try:
            with open("data.json", "r") as file:
                current_data = json.load(file)
    except FileNotFoundError:
            print("File not Found")
            return
    except json.JSONDecodeError:
        print("Invalid/Corrupted Json")
        return
     
    exp_to_del = input("id of expense: ")

   
    if exp_to_del in current_data.keys() :
        del current_data[exp_to_del]
    else:
        print("id not found")
        return

    try:
        with open("data.json", "w") as file:
            json.dump(current_data,file, indent=4)
    except :
        print(f"Error updating file")


def getnew_id(current_data):
    if len(current_data) == 0:
        return 1
    max_id = max(int(x) for x in current_data if str(x).isdigit())
    return max_id + 1
        

if __name__ == "__main__":
    
    entry=input("1. View Expense\n2. Add Expense\n3. Total Expense\n4. Delete Expense\n5. update ID\n ")
    while not entry.isdigit():
        print("Error!, Try Again")
        entry=input("options 1 - 5 \n")
    else:
        while entry != "end":
            status=int(entry)
            match status:
                    case 1:
                        viewexpenses()
                    case 2:
                        add_expense()
                    case 3:
                        total_expense()
                    case 4:
                        delete_expense()
                    # case 5:
                    #     id_checker()
                    case _:
                        print("Invalid option. Please select 1 - 5 ")
            entry=input("1. View Expense\n2. Add Expense\n3. Total Expense\n4. Delete Expense\n5. update ID\n ")
        else:
            print("Retry")










            
