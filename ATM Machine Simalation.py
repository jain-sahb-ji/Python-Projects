import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog

# Function to get and validate PIN
def get_pin(master):
    """Gets and validates user's PIN using a dialog."""
    while True:
        pin = simpledialog.askstring("PIN", "Enter your PIN:", show='*')
        if pin and pin.isdigit() and len(pin) == 4:
            return pin
        messagebox.showerror("Error", "Invalid PIN. Please enter a 4-digit numeric PIN.")

# Function to check balance
def check_balance(master):
    """Displays the current account balance in a message box."""
    messagebox.showinfo("Balance", f"Your account balance: ${balance:.2f}")

# Function to withdraw money
def withdraw(master):
    """Allows the user to withdraw money, updating the balance."""
    global balance
    while True:
            amount = simpledialog.askfloat("Withdrawal", "Enter withdrawal amount:")
            if amount > 0 and amount <= balance:
                balance -= amount
                transactions.append(f"Withdrawal: -${amount:.2f}")  # Add to transaction history
                messagebox.showinfo("Success", f"Withdrawal successful. New balance: ${balance:.2f}")
                return 
            messagebox.showerror("Error", "Invalid amount or insufficient funds.")

# Function to deposit money
def deposit(master):
    """Allows the user to deposit money, updating the balance."""
    global balance
    while True:
            amount = simpledialog.askfloat("Deposit", "Enter deposit amount:")
            if amount > 0:
                balance += amount
                transactions.append(f"Deposit: +${amount:.2f}")  # Add to transaction history
                messagebox.showinfo("Success", f"Deposit successful. New balance: ${balance:.2f}")
                return 
            messagebox.showerror("Error", "Invalid amount.")

# Function to change PIN
def change_pin(master):
    """Allows the user to change their PIN."""
    global pin
    new_pin = get_pin(master)
    if new_pin:
        pin = new_pin
        messagebox.showinfo("Success", "PIN changed successfully.")
        verify_pin(master)

# Function to display transaction history
def show_transaction_history(master):
    """Displays a list of past transactions."""
    if not transactions:
            messagebox.showinfo("Transaction History", "No transactions yet.")
    else:
        transaction_text = "\n".join(transactions)
        messagebox.showinfo("Transaction History", transaction_text)

# Function to verify PIN before performing tasks
def verify_pin(master):
    user_pin = get_pin(master)
    if user_pin == pin:
        return True
    else:
        messagebox.showerror("Error", "Incorrect PIN. Try again.")
        verify_pin(master)
        

# Main function
def main():
    global balance, pin, transactions
    balance = 1000.0
    pin = "1234"
    transactions = []

    window = tk.Tk()
    window.title("ATM Simulator")

    style = ttk.Style()
    style.theme_use('clam')

    def login():
        if verify_pin(window): 
            login_frame.pack_forget()
            menu_frame.pack()

    # Login frame
    login_frame = ttk.Frame(window, padding="20")
    login_frame.pack()
    ttk.Label(login_frame, text="Welcome to the ATM!").pack(pady=10)
    ttk.Button(login_frame, text="Enter PIN", command=login).pack()

    # Menu frame (initially hidden)
    menu_frame = ttk.Frame(window, padding="20")
    for i, option in enumerate(["Check Balance", "Withdraw", "Deposit", "Change PIN", "Transaction History", "Exit"]):
        ttk.Button(menu_frame, text=option, command=lambda choice=i+1: handle_choice(choice)).pack(pady=5)

    def handle_choice(choice):
        if choice == 1:
            check_balance(window)
        elif choice == 2:
            withdraw(window)
        elif choice == 3:
            deposit(window)
        elif choice == 4:
            change_pin(window)
        elif choice == 5:
            show_transaction_history(window)
        elif choice == 6:
            print("Thank you for using the ATM. Goodbye!")
            window.destroy()

    window.mainloop()

if __name__ == "__main__":
    main()
