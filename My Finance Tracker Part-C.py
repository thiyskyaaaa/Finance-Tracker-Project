import tkinter as tk
from tkinter import ttk
import json

# Global list to store transactions
#open a gloabale dictionary name transactions
transactions = {}


# File handling functions
def load_transactions():
    global transactions
    #load  informations to the file using json
    try:#using try  block to not to crash the program
        with open('file.json', 'r') as file:
            #using 'r for only reading not to write or append
            #read the file
            transactions = json.load(file)
            return transactions
    except Exception as E:
        print(E)
        with open('file.json', 'x') as file:
            print("file.json file created.")
            #using except for not to crash the program
            #if the file is not executed
            save_transactions()
        #if the file exicuted then save it

def save_transactions():
    #to save the file
    with open('file.json', 'w') as file:#'w' >>> if the file not exist, it will created.
        #if the file is exist it'll overwritten.
        json.dump(transactions, file)

def read_bulk_transactions_from_file(filename):
    try: #not to crash the program
        with open(filename, 'r') as file:
        # read the file and using 'with' statement ensure that file
        # is closed properly
            for line in file:
            #iterates the each and evry line
                transaction_data = line.strip().split(',')
                #split in to a list
                if len(transaction_data) == 3: #transaction_data elements 
                    amount = float(transaction_data[0])
                    category = transaction_data[1]
                    date = transaction_data[2]
    except FileNotFoundError:
    #if the specific file is not exicuted, handle the error
        print(f"File '{filename}' not found.")
    except Exception as e:
    #handle the error i.e.catches the other errors
        print(f"Error reading transactions from file: {e}")



# Feature implementations
def add_transaction():
    global transactions
    # user inputs for transactions
    
    choice = input("Enter NO 1 to add a transaction or NO 2 to add from a file: ")
    #choice 1 for a new transaction and choice 2 for add from a old file

    if choice == '1': #add new transactions
        while True:
            try:
                amount = float(input("Enter Amount: "))
                if amount <= 0:
                    print("Invalid Input. Please enter a valid amount!")
                else:
                    print("Valid Amount.")
                    break #break the loop if a valid amount entered
            except ValueError:
                print("Invalid Input. Enter a valid input")
                
        category = input("Enter the category: ") #input a category eg: Groceries,salary,food,etc  
      
        while True:
            try:#place the code that can throw error
                year = int(input("Enter a year (YYYY): "))#enter the year
                if len(str(year)) == 4: #the input year has to be 4 digit
                    break
                else:
                    print("Invalid Input. Please enter a valid Input.")
            except ValueError: #place the code to handle the error >>> error message
                print("Invalid Input. Please Try Again.")
                continue

     
        try:
            month = int(input("Enter a month (MM) : ")) #enter the month
            if 0 < month <= 12:
                pass
        except Exception as E:
            print(E)

        try: #place the code that can throw error
            date = int(input("Enter a date (DD): "))
            if 0 < date <= 31: #dates should have 1 to 31 including day 1 and day 31
                pass
            if month in [4, 6, 9, 11]:
                if date <= 30: #30 days months
                    pass
                else:
                    print("Invalid Input")
            elif month == 2:
                if (year % 4 == 0):#check the year is a leap or not
                    if date <= 29: #if the month is a leap year
                        pass
                    else:
                        if date <= 28: #28 days month
                            pass
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                if date <= 31: #31 days month
                    pass
            else:
                print("Invalid Date. Please Re-Enter!") #Inputs are incorrect
                pass
        except ValueError:
            print("Invalid Input")

        ymd = (f"{str(year)} - {str(month)} - {str(date)}") #call a variable name ymd and assign the date like YYYY-MM-DD 
        print(ymd) #print it #print ymd

        transaction_dict = {"amount": amount,
                "date": ymd} #create a dictionary called transaction_dict including amount and date using this format 

        if category not in transactions:
            transactions[category] = [] #create a category list

        print(category) #print the category >>> the list
        transactions[category].append(transaction_dict) #append the dictionary called transaction_dict to the category list
        save_transactions()  #save the ad transaction
        print("Transactions added successfully!") #print a message to the user

    elif choice == '2': #add from a old file
        filename =  input("Enter the filename :")
        read_bulk_transactions_from_file(filename)#call the read_bulk_transactions_from_file function
    else:
        print("Invalid Input") #print a message
     

def view_transactions(): #display all transactions
    if not transactions:
        print("No transactions Found")
    else:
        #if the transactions found >> print it
        for transaction in transactions: #loop variable
            print("******Transaction Found******")
            print(transactions)#print the dictionary as a list with variables
            break


def update_transaction():
    # Placeholder for update transaction logic
    # Remember to use save_transactions() after updating 
    #Display transactions.
    global transactions
    #using global for changing informations
    view_transactions()
    
    #user can update the choices they want
    #get the inputs that user needs to update in this case
    
    #get the category to update
    catogery = input("Enter the category you want to update: ")

    try: #place the code that can throw error
        # check if the category exist
        if catogery in transactions:
            #get the index to update
            ntransactions = int(input(f"What index you want to update? Enter the transaction to update (0-{len(transactions[catogery]) - 1}): "))

            #check if the index is valid
            if 0 <= ntransactions < len(transactions[catogery]):
                transaction = transactions[catogery][ntransactions] #define the key

                while True: 
                    print("\nChoose the option: \n 1. Amount \n 2. Date") #give the options that user can update
                    choice = input("Enter the choice you want to update: ")

                    try:
                        choice = int(choice) #check the choice is valid
                        if 1 <= choice <= 2:
                            break
                        else:
                            print("Invalid option. Please try again!")
                    except ValueError:
                        print("Invalid input. Please enter a number...")

                if choice == 1: #update the amount
                    amount = float(input("Enter the new amount: "))
                    transactions[catogery][ntransactions]["amount"] = amount #define the key
                elif choice == 2: #update the date
                    while True:
                        try:
                            date = input("Enter the new date to update (YYYY-MM-DD): ")
                            year, month, day = map(int, date.split("-"))
                            transactions[catogery][ntransactions]["date"] = date
                            break
                        except ValueError:
                            print("Invalid date format. Please follow YYYY-MM-DD.")

                #save the update transaction
                save_transactions()
                print("Transaction updated successfully!") #prnt a message
            else:
                raise ValueError("Invalid Transaction Choice. Please Re-Enter.")#prnt a message
        else:
            print(f"The category '{catogery}' does not exist.") # if the category does not exist print a message
    except ValueError as e: #handle the error
        print(e) 


def delete_transaction():
    # Placeholder for delete transaction logic
    # Remember to use save_transactions() after deleting
    global transactions
    # Using global for changing information
    view_transactions()
    try:
        category_to_delete = input("Enter the category you want to delete from: ")
        #get the category user want to delete
        if category_to_delete in transactions:
            #get the list of transactions corresponding to the category
            tran_list = transactions[category_to_delete]
            index_to_delete = int(input(f"Enter the index of the transaction you want to delete from '{category_to_delete}' (1-n): ")) - 1
            #enter the index user want to delete in the specific category user prompt
            if 0 <= index_to_delete < len(tran_list):
                #delete the index of the category
                deleted_transaction = tran_list.pop(index_to_delete)
                print("Transaction deleted successfully:")
                print(deleted_transaction)
                save_transactions() #save it to the file
            else:
                print("Invalid index. Please enter a number between 1 and", len(transactions))
        else:
            print("Category does not exist. Please enter a valid category.")
    except ValueError: #handle the error
        print("Invalid input! Please enter a valid number.")



def display_summary():
    # Placeholder for summary display logic
    print("Transaction Summary:")
    for category, tran_list in transactions.items():
        total_amount = sum(transaction["amount"] for transaction in tran_list) #get the total of each category
        print(f"Category: {category}, Total Amount: {total_amount}") #print it

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")
        self.display_transactions(self.transactions)


    def create_widgets(self):

        width, height = 500, 500
        display_width = self.root.winfo_screenwidth()
        display_height = self.root.winfo_screenheight()
        left = int(display_width/2 - width/2)
        top = int(display_height/2 - height/2)
        self.root.geometry(f'{width}x{height}+{left}+{top}')
        self.root.title("Personal Finance Tracker")
        self.root.resizable(False, False)
        self.root.iconbitmap('icon.ico')
        self.root.config(bg='purple')
        self.logo_image = tk.PhotoImage(file="logo.png")
        # Create a label for the logo
        self.logo_label = tk.Label(self.root, image=self.logo_image)
        self.logo_label.pack(side="top", anchor="nw")
    

        #self.heading = ttk.Label(self.root, text= "Personal Finance Tracker")
        self.heading = ttk.Label(self.root,text='Personal Finance Tracker', font='Georgia 18 italic ', background='violet',)
        self.heading.pack(side='top',pady=5)


        frame1 = ttk.Frame(self.root, width=300, height=100, relief=tk.GROOVE)
        frame1.pack_propagate(False)
        frame1.pack(side='top')

    
        # Search bar and button
        self.search_entry = ttk.Entry(frame1)
        self.search_entry.pack(pady=10)
        search_button = ttk.Button(frame1, text='Search', command=self.search_transactions)
        search_button.pack()

       
        # Treeview for displaying transactions
        treeview_frame = ttk.Frame(self.root)
        treeview_frame.pack(fill=tk.BOTH, expand=True)

        # Create a Canvas to hold the Treeview
        canvas = tk.Canvas(treeview_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Scrollbar for the Canvas #Scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(treeview_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add the Treeview to the Canvas
        self.table = ttk.Treeview(canvas, columns=('category', 'amount', 'date'), show='headings', yscrollcommand=scrollbar.set)
        self.table.heading('category', text='CATEGORY',command=lambda: self.sort_by_column('category', False))
        self.table.heading('amount', text='AMOUNT',command=lambda: self.sort_by_column('amount', False))
        self.table.heading('date', text='DATE',command=lambda: self.sort_by_column('date', False))
        self.table.column('category', width=200)
        self.table.column('amount', width=150)

        # Add the Treeview to the Canvas
        canvas.create_window((0, 0), window=self.table, anchor=tk.NW)

        # Configure the Canvas to scroll the Treeview
        canvas.configure(yscrollcommand=scrollbar.set)

        # Configure the Treeview to resize with the Frame
        self.table.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    def load_transactions(self, filename): #loard informations  using json
        try:
            with open('file.json', 'r') as file:
                return json.load(file)
        except Exception as E:
            print(E)
            with open('file.json', 'x') as file:
                print("file.json file created.")
        except FileNotFoundError:
            return {}

    def display_transactions(self, transactions):
        for row in self.table.get_children():
            self.table.delete(row)

        for category, tran_list in transactions.items():
            for transaction in tran_list:
                amount = transaction["amount"]
                date = transaction["date"]
                self.table.insert('', 'end', values=(category, amount, date))

    def search_transactions(self): 
        search_term = self.search_entry.get().lower()
        search_results = {}

        for category, tran_list in self.transactions.items():
            list2 = [transaction for transaction in tran_list
                             if search_term in str(transaction["amount"]).lower() or
                             search_term in transaction["date"].lower() or
                             search_term in category.lower()]
            if list2:
                search_results[category] = list2

        self.display_transactions(search_results)

    def sort_by_column(self, col, reverse):
        sorted_transactions = {}
        for category, tran_list in self.transactions.items():
            if col == 'amount':
                sorted_list = sorted(tran_list, key=lambda x: x[col], reverse=reverse)
            else:
                sorted_list = sorted(tran_list, key=lambda x: x.get(col, '').lower(), reverse=reverse)
            sorted_transactions[category] = sorted_list

        self.display_transactions(sorted_transactions)
          

def main_menu():
    load_transactions() # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Read Bulk Transaction From a File")
        print("7. Finance Tracker GUI")
        print("8. Exit")
        choice = input("Enter your choice: ")
        

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            filename =  input("Enter the filename :")
            read_bulk_transactions_from_file(filename)
        elif choice == '7':
            def main():
                root = tk.Tk()
                app = FinanceTrackerGUI(root)
                root.mainloop()
            if __name__ == "__main__":
                    main()
        elif choice == '8':
            save_transactions() #save before exit
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
    
# if you are paid to do this assignment please delete this line of comment
