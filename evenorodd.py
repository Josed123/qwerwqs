import json
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# File paths for storing data
CART_FILE = "cart.json"
LIBRARY_FILE = "library.json"
EXPENSES_FILE = "expenses.json"
TASKS_FILE = "tasks.json"

# Function to load data from JSON files
def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save data to JSON files
def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Shopping Cart Program
cart = load_data(CART_FILE)

def shopping_cart():
    def display_menu():
        print(Back.GREEN + Fore.BLACK + "\nShopping Cart Menu:")
        print(Fore.GREEN + "1. Add Item to Cart")
        print(Fore.GREEN + "2. View Cart")
        print(Fore.GREEN + "3. Edit Item Quantity")
        print(Fore.GREEN + "4. Remove Item from Cart")
        print(Fore.GREEN + "5. View Total Price")
        print(Fore.GREEN + "6. Back to Main Menu")

    def add_item():
        name = input(Fore.CYAN + "Enter item name: ")
        price = float(input(Fore.CYAN + "Enter item price: "))
        quantity = int(input(Fore.CYAN + "Enter quantity: "))
        cart.append({"name": name, "price": price, "quantity": quantity})
        save_data(CART_FILE, cart)

    def view_cart():
        if cart:
            print(Back.CYAN + Fore.BLACK + "\nItems in Cart:")
            for index, item in enumerate(cart, 1):
                print(Fore.WHITE + f"{index}. {item['name']} - ${item['price']} x {item['quantity']}")
        else:
            print(Fore.RED + "Your cart is empty.")

    def edit_item_quantity():
        if cart:
            view_cart()
            try:
                item_num = int(input(Fore.CYAN + "Enter item number to edit: "))
                if 1 <= item_num <= len(cart):
                    new_quantity = int(input(Fore.CYAN + "Enter new quantity: "))
                    cart[item_num - 1]["quantity"] = new_quantity
                    save_data(CART_FILE, cart)
                else:
                    print(Fore.RED + "Invalid item number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "Your cart is empty.")

    def remove_item():
        if cart:
            view_cart()
            try:
                item_num = int(input(Fore.CYAN + "Enter item number to remove: "))
                if 1 <= item_num <= len(cart):
                    removed_item = cart.pop(item_num - 1)
                    save_data(CART_FILE, cart)
                    print(Fore.GREEN + f"Item '{removed_item['name']}' removed.")
                else:
                    print(Fore.RED + "Invalid item number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "Your cart is empty.")

    def view_total():
        total = sum(item['price'] * item['quantity'] for item in cart)
        print(Fore.MAGENTA + f"Total price: ${total:.2f}")

    while True:
        display_menu()
        try:
            choice = int(input(Fore.BLUE + "\nEnter your choice: "))
            if choice == 1:
                add_item()
            elif choice == 2:
                view_cart()
            elif choice == 3:
                edit_item_quantity()
            elif choice == 4:
                remove_item()
            elif choice == 5:
                view_total()
            elif choice == 6:
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")


# Library System Program
library = load_data(LIBRARY_FILE)

def library_system():
    def display_menu():
        print(Back.BLUE + Fore.WHITE + "\nLibrary Menu:")
        print(Fore.GREEN + "1. Add Book")
        print(Fore.GREEN + "2. View Books")
        print(Fore.GREEN + "3. Edit Book")
        print(Fore.GREEN + "4. Remove Book")
        print(Fore.GREEN + "5. Search Book")
        print(Fore.GREEN + "6. Back to Main Menu")

    def add_book():
        title = input(Fore.CYAN + "Enter book title: ")
        author = input(Fore.CYAN + "Enter book author: ")
        year = int(input(Fore.CYAN + "Enter publication year: "))
        library.append({"title": title, "author": author, "year": year})
        save_data(LIBRARY_FILE, library)

    def view_books():
        if library:
            print(Back.CYAN + Fore.BLACK + "\nBooks in Library:")
            for index, book in enumerate(library, 1):
                print(Fore.WHITE + f"{index}. {book['title']} by {book['author']} ({book['year']})")
        else:
            print(Fore.RED + "No books to display.")

    def edit_book():
        if library:
            view_books()
            try:
                book_num = int(input(Fore.CYAN + "Enter book number to edit: "))
                if 1 <= book_num <= len(library):
                    new_title = input(Fore.CYAN + "Enter new title: ")
                    new_author = input(Fore.CYAN + "Enter new author: ")
                    new_year = int(input(Fore.CYAN + "Enter new publication year: "))
                    library[book_num - 1] = {"title": new_title, "author": new_author, "year": new_year}
                    save_data(LIBRARY_FILE, library)
                else:
                    print(Fore.RED + "Invalid book number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "No books to edit.")

    def remove_book():
        if library:
            view_books()
            try:
                book_num = int(input(Fore.CYAN + "Enter book number to remove: "))
                if 1 <= book_num <= len(library):
                    removed_book = library.pop(book_num - 1)
                    save_data(LIBRARY_FILE, library)
                    print(Fore.GREEN + f"Book '{removed_book['title']}' removed.")
                else:
                    print(Fore.RED + "Invalid book number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "No books to remove.")

    def search_book():
        search_term = input(Fore.CYAN + "Enter title or author to search: ").lower()
        found_books = [book for book in library if search_term in book['title'].lower() or search_term in book['author'].lower()]
        if found_books:
            print(Back.CYAN + Fore.BLACK + "\nSearch Results:")
            for book in found_books:
                print(Fore.WHITE + f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
        else:
            print(Fore.RED + "No books found.")

    while True:
        display_menu()
        try:
            choice = int(input(Fore.BLUE + "\nEnter your choice: "))
            if choice == 1:
                add_book()
            elif choice == 2:
                view_books()
            elif choice == 3:
                edit_book()
            elif choice == 4:
                remove_book()
            elif choice == 5:
                search_book()
            elif choice == 6:
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")


# Expense Tracker Program
expenses = load_data(EXPENSES_FILE)

def expense_tracker():
    def display_menu():
        print(Back.GREEN + Fore.BLACK + "\nExpense Tracker Menu:")
        print(Fore.GREEN + "1. Add Expense")
        print(Fore.GREEN + "2. View Expenses")
        print(Fore.GREEN + "3. Edit Expense")
        print(Fore.GREEN + "4. Remove Expense")
        print(Fore.GREEN + "5. View Total Expenses")
        print(Fore.GREEN + "6. Back to Main Menu")

    def add_expense():
        category = input(Fore.CYAN + "Enter expense category: ")
        amount = float(input(Fore.CYAN + "Enter expense amount: "))
        expenses.append({"category": category, "amount": amount})
        save_data(EXPENSES_FILE, expenses)

    def view_expenses():
        if expenses:
            print(Back.CYAN + Fore.BLACK + "\nExpenses:")
            for index, expense in enumerate(expenses, 1):
                print(Fore.WHITE + f"{index}. {expense['category']} - ${expense['amount']}")
        else:
            print(Fore.RED + "No expenses to display.")

    def edit_expense():
        if expenses:
            view_expenses()
            try:
                expense_num = int(input(Fore.CYAN + "Enter expense number to edit: "))
                if 1 <= expense_num <= len(expenses):
                    new_category = input(Fore.CYAN + "Enter new category: ")
                    new_amount = float(input(Fore.CYAN + "Enter new amount: "))
                    expenses[expense_num - 1] = {"category": new_category, "amount": new_amount}
                    save_data(EXPENSES_FILE, expenses)
                else:
                    print(Fore.RED + "Invalid expense number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "No expenses to edit.")

    def remove_expense():
        if expenses:
            view_expenses()
            try:
                expense_num = int(input(Fore.CYAN + "Enter expense number to remove: "))
                if 1 <= expense_num <= len(expenses):
                    removed_expense = expenses.pop(expense_num - 1)
                    save_data(EXPENSES_FILE, expenses)
                    print(Fore.GREEN + f"Expense '{removed_expense['category']}' removed.")
                else:
                    print(Fore.RED + "Invalid expense number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "No expenses to remove.")

    def view_total():
        total = sum(expense['amount'] for expense in expenses)
        print(Fore.MAGENTA + f"Total expenses: ${total:.2f}")

    while True:
        display_menu()
        try:
            choice = int(input(Fore.BLUE + "\nEnter your choice: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                edit_expense()
            elif choice == 4:
                remove_expense()
            elif choice == 5:
                view_total()
            elif choice == 6:
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")


# To-Do List Program
tasks = load_data(TASKS_FILE)

def todo_list():
    def display_menu():
        print(Back.RED + Fore.WHITE + "\nTo-Do List Menu:")
        print(Fore.GREEN + "1. Add Task")
        print(Fore.GREEN + "2. View Tasks")
        print(Fore.GREEN + "3. Edit Task")
        print(Fore.GREEN + "4. Remove Task")
        print(Fore.GREEN + "5. Mark Task as Completed")
        print(Fore.GREEN + "6. Back to Main Menu")

    def add_task():
        name = input(Fore.CYAN + "Enter task name: ")
        tasks.append({"name": name, "completed": False})
        save_data(TASKS_FILE, tasks)

    def view_tasks():
        if tasks:
            print(Back.CYAN + Fore.BLACK + "\nTasks:")
            for index, task in enumerate(tasks, 1):
                status = "Completed" if task["completed"] else "Pending"
                print(Fore.WHITE + f"{index}. {task['name']} - {status}")
        else:
            print(Fore.RED + "No tasks to display.")

    def edit_task():
        if tasks:
            view_tasks()
            try:
                task_num = int(input(Fore.CYAN + "Enter task number to edit: "))
                if 1 <= task_num <= len(tasks):
                    new_name = input(Fore.CYAN + "Enter new task name: ")
                    tasks[task_num - 1]["name"] = new_name
                    save_data(TASKS_FILE, tasks)
                else:
                    print(Fore.RED + "Invalid task number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "No tasks to edit.")

    def remove_task():
        if tasks:
            view_tasks()
            try:
                task_num = int(input(Fore.CYAN + "Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    save_data(TASKS_FILE, tasks)
                    print(Fore.GREEN + f"Task '{removed_task['name']}' removed.")
                else:
                    print(Fore.RED + "Invalid task number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "No tasks to remove.")

    def mark_completed():
        if tasks:
            view_tasks()
            try:
                task_num = int(input(Fore.CYAN + "Enter task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    save_data(TASKS_FILE, tasks)
                    print(Fore.GREEN + f"Task '{tasks[task_num - 1]['name']}' marked as completed.")
                else:
                    print(Fore.RED + "Invalid task number.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
        else:
            print(Fore.RED + "No tasks to mark as completed.")

    while True:
        display_menu()
        try:
            choice = int(input(Fore.BLUE + "\nEnter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                edit_task()
            elif choice == 4:
                remove_task()
            elif choice == 5:
                mark_completed()
            elif choice == 6:
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

# Main menu
def main_menu():
    while True:
        print(Back.BLACK + Fore.WHITE + "\nMain Menu:")
        print(Fore.GREEN + "1. Shopping Cart")
        print(Fore.GREEN + "2. Library System")
        print(Fore.GREEN + "3. Expense Tracker")
        print(Fore.GREEN + "4. To-Do List")
        print(Fore.GREEN + "5. Exit")

        try:
            choice = int(input(Fore.BLUE + "\nEnter your choice: "))
            if choice == 1:
                shopping_cart()
            elif choice == 2:
                library_system()
            elif choice == 3:
                expense_tracker()
            elif choice == 4:
                todo_list()
            elif choice == 5:
                print(Fore.GREEN + "Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

if __name__ == "__main__":
    main_menu()
