import json
records = []

def welcome_screen():
    print("-"*40)
    print("Welcome to Expense Splitter Simulation")
    print("-"*40)

def show_menu():
    print("Main Menu")
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Summary Stats")
    print("7. Save to File")
    print("8. Load from File")
    print("9. Clear All Data")
    print("10. Help")
    print("0. Exit")
    print("-"*40)

def add_record():
    try:
        name = input("Enter name: ")
        amount = float(input("Enter amount spent: "))
        records.append({"Record name": name, "Amount spent": amount})
        print("Record added.")
    except Exception as error:
        print(f"Error while adding a record: {error}")

def view_records():
    if not records:
        print("No records found.")
        return
    print("All Records:")
    for index, record in enumerate(records):
        print(f"{index + 1}. Name: {record['name']}, Amount: {record['amount']}")

def search_record():
    search_name = input("Enter name to search: ")
    found = [x for x in records if x['name'] == search_name]
    if found:
        for x in found:
            print(f"Found: {x['name']}, Amount: {x['amount']}")
    else:
        print("No such record found.")

def update_record():
    view_records()
    try:
        idx = int(input("Enter record number to update: "))
        if 0 <= idx < len(records):
            name = input("Enter new name: ")
            amount = float(input("Enter new amount: "))
            records[idx + 1] = {"name": name, "amount": amount}
            print("Record updated.")
        else:
            print("Invalid record number.")
    except Exception as error:
        print(f"Error while updating record: {error}")

def delete_record():
    view_records()
    try:
        idx = int(input("Enter record number to delete: "))
        if 0 <= idx < len(records):
            del records[idx + 1]
            print("Record deleted.")
        else:
            print("Invalid record number.")
    except Exception as error:
        print(f"Error while deleting record: {error}")

def summary_stats():
    if not records:
        print("No records to summarize.")
        return
    total = sum(r['amount'] for r in records)
    avg = total / len(records)
    print(f"Total: {total}, Average: {avg}")

def save_to_file():
    global records
    if not records:
        print("No records to save.")
        return
    try:
        file = open("records.json", "w")
        json.dump(records, file)
        file.close()
        print("Data saved to records.json")
    except Exception as error:
        print(f"Error while saving file: {error}")

def load_from_file():
    global records
    try:
        file = open("records.json", "r")
        records = json.load(file)
        print("Data loaded.")
    except Exception as error:
        print(f"Error while loading file: {error}")

def clear_data():
    confirm = input("Are you sure you want to clear all data? (yes/no): ")
    if confirm.lower() == "yes":
        records.clear()
        print("All records cleared.")
    else:
        print("Operation cancelled.")

def help_menu():
    print("Instructions: Use numbers to choose actions from the main menu.")

while True:
    welcome_screen()
    show_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_record()
    elif choice == '2':
        view_records()
    elif choice == '3':
        search_record()
    elif choice == '4':
        update_record()
    elif choice == '5':
        delete_record()
    elif choice == '6':
        summary_stats()
    elif choice == '7':
        save_to_file()
    elif choice == '8':
        load_from_file()
    elif choice == '9':
        clear_data()
    elif choice == '10':
        help_menu()
    elif choice == '0':
        print("Exiting program.")
        break
    else:
        print("Invalid option. Try again.")