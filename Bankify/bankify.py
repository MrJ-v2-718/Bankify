import os
import tkinter as tk
from tkinter import messagebox
from hashlib import sha256

# Create Root Window
root = tk.Tk()

# Set Window Title
root.title("Bankify")

# Set Background Color
root.config(background="#0a0c18")


# Help Message Box
def help_click():
    messagebox.showinfo(
        "How To Use",
        "Create an account to start managing your money. Once an account is created, "
        "you can login using your account ID and password. Account IDs "
        "are case-sensitive and cannot be changed."
    )


# About Message Box
def about_click():
    messagebox.showinfo(
        "About",
        "Created by MrJ\n2024©"
    )


# Function Called When Create Account Button Is Clicked
def create_account_click():
    # Retreive User Entries
    account_id = temp_account_id.get()
    name = temp_name.get()
    email = temp_email.get()
    password = temp_password.get()
    password = sha256(password.encode("utf-8")).hexdigest()
    accounts_directory = "Accounts"
    all_accounts = os.listdir(accounts_directory)

    # Require User To Enter All Fields
    if account_id == "" or name == "" or email == "" or password == "":
        notification.config(fg="red", text="All Fields Required")
        return

    for account_check in all_accounts:
        if account_id == account_check:
            # Notify User If Account ID Already Exists
            notification.config(fg="red", text="Account Already Exists")
            return
            # Skip Over The README.md File
        elif account_check == "README.md":
            continue

    # Write Data To New Account File
    new_file = open(os.path.join(accounts_directory, account_id), "w")
    new_file.write(account_id + "\n")
    new_file.write(name + "\n")
    new_file.write(email + "\n")
    new_file.write(password + "\n")
    new_file.write("0")
    new_file.close()
    notification.config(fg="green", text="Account Created Successfully")


# Function That Generates A Window For Account Creation
def create_account():
    # Variables
    global temp_account_id
    global temp_name
    global temp_email
    global temp_password
    global notification

    # Temporary Storage For User Inputs
    temp_account_id = tk.StringVar()
    temp_name = tk.StringVar()
    temp_email = tk.StringVar()
    temp_password = tk.StringVar()

    # Create Account Screen
    create_account_screen = tk.Toplevel(root)
    create_account_screen.title("Create Account")

    # Set The Background Color
    create_account_screen.config(background="#0a0c18")

    # Create Account Labels
    tk.Label(
        create_account_screen,
        text="Enter Information Below To Create Your Account",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 18)
    ).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(
        create_account_screen,
        text="Account ID",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=1, sticky="w", pady=5, padx=5)

    tk.Label(
        create_account_screen,
        text="Name",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=2, sticky="w", pady=5, padx=5)

    tk.Label(
        create_account_screen,
        text="Email",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=3, sticky="w", pady=5, padx=5)

    tk.Label(
        create_account_screen,
        text="Password",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=4, sticky="w", pady=5, padx=5)

    notification = tk.Label(
        create_account_screen,
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    )
    notification.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

    # Create Account Entries
    tk.Entry(
        create_account_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=30,
        textvariable=temp_account_id
    ).grid(row=1, column=0, sticky="e", pady=5, padx=5)

    tk.Entry(
        create_account_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=30,
        textvariable=temp_name
    ).grid(row=2, column=0, sticky="e", pady=5, padx=5)

    tk.Entry(
        create_account_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=30,
        textvariable=temp_email
    ).grid(row=3, column=0, sticky="e", pady=5, padx=5)

    tk.Entry(
        create_account_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=30,
        textvariable=temp_password,
        show="$"
    ).grid(row=4, column=0, sticky="e", pady=5, padx=5)

    # Create Account Button
    tk.Button(
        create_account_screen,
        text="Create Account",
        command=create_account_click,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 14)
    ).grid(row=5, column=0, columnspan=2, padx=5, pady=5)


# Function Called When Login Button Is Clicked
def login_click():
    global login_account_id
    accounts_directory = "Accounts"

    # Make A List Of All User Accounts
    all_accounts = os.listdir(accounts_directory)
    login_account_id = temp_login_account_id.get()
    login_password = temp_login_password.get()
    login_password = sha256(login_password.encode("utf-8")).hexdigest()

    for account_id in all_accounts:
        if account_id == login_account_id:
            # Open User Account File If Matching ID Is Found
            file = open(os.path.join(accounts_directory, account_id), "r")
            file_data = file.read()
            file_data = file_data.split("\n")

            # Assign Read Values To Variables
            info_name = file_data[1]
            password = file_data[3]

            # Account Information
            if login_password == password:
                login_screen.destroy()
                personal_info = tk.Toplevel(root)
                personal_info.title("Account Information")

                # Set the background color
                personal_info.config(background="#0a0c18")

                # Labels
                tk.Label(
                    personal_info,
                    text="Account Information",
                    background="#0a0c18",
                    foreground="#50d9da",
                    font=("URW Gothic", 18)
                ).grid(row=0, sticky="n", padx=10, pady=10)

                tk.Label(
                    personal_info,
                    text="Welcome " + info_name,
                    background="#0a0c18",
                    foreground="#50d9da",
                    font=("URW Gothic", 14)
                ).grid(row=1, sticky="n", padx=5, pady=5)

                # Buttons
                tk.Button(
                    personal_info,
                    text="Balance & Account Details",
                    background="#50d9da",
                    foreground="#0a0c18",
                    font=("URW Gothic", 14),
                    width=25,
                    command=balance
                ).grid(row=2, sticky="n", padx=10, pady=10)

                tk.Button(
                    personal_info,
                    text="Deposit",
                    background="#50d9da",
                    foreground="#0a0c18",
                    font=("URW Gothic", 14),
                    width=25,
                    command=deposit
                ).grid(row=3, sticky="n", padx=10, pady=10)

                tk.Button(
                    personal_info,
                    text="Withdrawal",
                    background="#50d9da",
                    foreground="#0a0c18",
                    font=("URW Gothic", 14),
                    width=25,
                    command=withdrawal
                ).grid(row=4, sticky="n", padx=10, pady=10)

                tk.Button(
                    personal_info,
                    text="Edit Account Details",
                    background="#50d9da",
                    foreground="#0a0c18",
                    font=("URW Gothic", 14),
                    width=25,
                    command=edit_account
                ).grid(row=5, sticky="n", padx=10, pady=10)

                return
            else:
                login_notification.config(fg="red", text="Password Incorrect")
                return

    login_notification.config(fg="red", text="No Account Found")


# Function Called When Create Account Button Is Clicked
def edit_account_click():
    # Retreive Entries
    account_id = temp_account_id_edit.get()
    name = temp_name_edit.get()
    email = temp_email_edit.get()
    password = temp_password_edit.get()

    # Hash Password
    password = sha256(password.encode("utf-8")).hexdigest()

    # Set The Directory Name For Account Access
    accounts_directory = "Accounts"
    all_accounts = os.listdir(accounts_directory)

    # Require The User To Provide All Data Fields
    if account_id == "" or name == "" or email == "" or password == "":
        edit_notification.config(fg="red", text="All Fields Required")
        return

    for account_check in all_accounts:
        if account_id == account_check:
            # Open User Account File If Matching Account ID Is Found
            file = open(os.path.join(accounts_directory, account_id), "r+")
            file_data = file.read()
            info = file_data.split("\n")

            # Assign Read Values To Variables
            current_balance = info[4]

            # Delete Old Account Data
            file.seek(0)
            file.truncate(0)

            # Write New Account Data
            file.write(account_id + "\n")
            file.write(name + "\n")
            file.write(email + "\n")
            file.write(password + "\n")
            file.write(current_balance)
            file.close()
            edit_notification.config(fg="green", text="Account Updated Successfully")

            # Clear Entry Boxes
            temp_account_id_edit.set("")
            temp_name_edit.set("")
            temp_email_edit.set("")
            temp_password_edit.set("")

            return
        elif account_check == "README.md":
            continue
    edit_notification.config(fg="red", text="No Account Found")


# Function That Generates A Window For Editing Account Details
def edit_account():
    # Variables
    global temp_account_id_edit
    global temp_name_edit
    global temp_email_edit
    global temp_password_edit
    global edit_notification

    # Temporary Storage For User Inputs
    temp_account_id_edit = tk.StringVar()
    temp_name_edit = tk.StringVar()
    temp_email_edit = tk.StringVar()
    temp_password_edit = tk.StringVar()

    # Edit Account Screen
    create_account_screen = tk.Toplevel(root)
    create_account_screen.title("Edit Account")

    # Set The Background Color
    create_account_screen.config(background="#0a0c18")

    # Create Account Labels
    tk.Label(
        create_account_screen,
        text="Enter Information Below To Edit Your Account",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 18)
    ).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(
        create_account_screen,
        text="Current Account ID",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=1, sticky="w", pady=5, padx=5)

    tk.Label(
        create_account_screen,
        text="New Name",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=2, sticky="w", pady=5, padx=5)

    tk.Label(
        create_account_screen,
        text="New Email",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=3, sticky="w", pady=5, padx=5)

    tk.Label(
        create_account_screen,
        text="New Password",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=4, sticky="w", pady=5, padx=5)

    edit_notification = tk.Label(
        create_account_screen,
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    )
    edit_notification.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

    # Create Account Entries
    tk.Entry(
        create_account_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=30,
        textvariable=temp_account_id_edit
    ).grid(row=1, column=1, sticky="e", pady=5, padx=5)

    tk.Entry(
        create_account_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=30,
        textvariable=temp_name_edit
    ).grid(row=2, column=1, sticky="e", pady=5, padx=5)

    tk.Entry(
        create_account_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=30,
        textvariable=temp_email_edit
    ).grid(row=3, column=1, sticky="e", pady=5, padx=5)

    tk.Entry(
        create_account_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=30,
        textvariable=temp_password_edit,
        show="$"
    ).grid(row=4, column=1, sticky="e", pady=5, padx=5)

    # Create Account Button
    tk.Button(
        create_account_screen,
        text="Submit",
        command=edit_account_click,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 14)
    ).grid(row=5, column=1, columnspan=2, padx=5, pady=5)


# Function That Generates A Window For Account Deposits
def deposit():
    # Variables
    global amount
    global deposit_notification
    global current_balance_label
    amount = tk.StringVar()

    # Open User Account File
    accounts_directory = "Accounts"
    file = open(os.path.join(accounts_directory, login_account_id), "r")
    file_data = file.read()
    user_info = file_data.split("\n")

    # Assign Read Balance To Variable
    info_balance = user_info[4]

    # Deposit Screen
    deposit_screen = tk.Toplevel(root)
    deposit_screen.title("Deposit")

    # Set The Background Color
    deposit_screen.config(background="#0a0c18")

    # Deposit Labels
    tk.Label(
        deposit_screen,
        text="Deposit Information",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 18)
    ).grid(row=0, column=0, columnspan=2, sticky="n", pady=10)

    current_balance_label = tk.Label(
        deposit_screen,
        text="Current Balance : $" + "{:,.2f}".format(float(info_balance)),
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    )
    current_balance_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(
        deposit_screen,
        text="\tAmount : $",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=2, column=0, padx=10, pady=10)

    deposit_notification = tk.Label(
        deposit_screen,
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    )
    deposit_notification.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Deposit Entry
    tk.Entry(
        deposit_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        textvariable=amount
    ).grid(row=2, column=1, padx=10, pady=10)

    # Deposit Button
    tk.Button(
        deposit_screen,
        text="Finish Deposit",
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 14),
        command=deposit_click
    ).grid(row=3, column=0, columnspan=2, padx=10, pady=10)


# The Math For Deposits
def deposit_math(rounded_deposit, current_balance):
    deposit_amount = rounded_deposit
    current_balance = current_balance
    updated_balance = current_balance + deposit_amount
    return updated_balance


# Function Called When Deposit Button Is Clicked
def deposit_click():
    if amount.get() == "":
        # Require User To Enter An Amount
        deposit_notification.config(text="Enter An Amount", fg="red")
        amount.set("")
        return

    # Ensure Amount Is A Positive Value And Numeric
    try:
        if float(amount.get()) <= 0:
            deposit_notification.config(text="Negative Amount Not Allowed", fg="red")
            amount.set("")
            return
    except ValueError:
        deposit_notification.config(text="Enter Numeric Value", fg="red")
        amount.set("")
        return

    # Ensure Amount Is Less Than 10 Digits
    if len(amount.get()) >= 10:
        deposit_notification.config(text="Must Be Less Than 10 Digits", fg="red")
        amount.set("")
        return

    # Set The Directory Name For Account Access
    accounts_directory = "Accounts"

    # Open User Account File
    file = open(os.path.join(accounts_directory, login_account_id), "r+")
    file_data = file.read()
    info = file_data.split("\n")

    # Assign Read Values To Variables
    account_id = info[0]
    name = info[1]
    email = info[2]
    password = info[3]
    current_balance = info[4]

    # Round Deposit Amount To The Nearest Cent
    rounded_deposit = round(float(amount.get()), 2)
    current_balance = float(current_balance)

    # Call To deposit_math() To Calculate New Balance
    updated_balance = deposit_math(rounded_deposit, current_balance)

    # Round Updated Balance To The Nearest Cent Before Writing To Account File
    updated_balance = round(updated_balance, 2)

    # Format Updated Balance To Two Decimal Places
    updated_balance = "{:.2f}".format(updated_balance)

    # Clear Deposit Entry Box
    amount.set("")

    # Delete Old File Data
    file.seek(0)
    file.truncate(0)

    # Replace Old Balance With New Balance In Account File
    file.write(account_id + "\n")
    file.write(name + "\n")
    file.write(email + "\n")
    file.write(password + "\n")
    file.write(str(updated_balance))
    file.close()

    # Show User Updated Balance
    current_balance_label.config(text="Current Balance : $" + "{:,.2f}".format(float(updated_balance)), fg="green")
    deposit_notification.config(text="Balance Updated", fg="green")


# Function That Generates A Window For Account Withdrawals
def withdrawal():
    # Variables
    global withdrawal_amount
    global withdrawal_notification
    global current_balance_label_w
    withdrawal_amount = tk.StringVar()

    # Open User Account File
    accounts_directory = "Accounts"
    file = open(os.path.join(accounts_directory, login_account_id), "r")
    file_data = file.read()
    user_info = file_data.split("\n")

    # Assign Read Balance To Variable
    info_balance = user_info[4]

    # Withdrawal Screen
    withdrawal_screen = tk.Toplevel(root)
    withdrawal_screen.title("Withdrawal")

    # Set The Background Color
    withdrawal_screen.config(background="#0a0c18")

    # Withdrawal Labels
    tk.Label(
        withdrawal_screen,
        text="Withdrawal",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 18)
    ).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    current_balance_label_w = tk.Label(
        withdrawal_screen,
        text="Current Balance : $" + "{:,.2f}".format(float(info_balance)),
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    )
    current_balance_label_w.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(
        withdrawal_screen,
        text="\tAmount : $",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=2, column=0, padx=10, pady=10)

    withdrawal_notification = tk.Label(
        withdrawal_screen,
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    )
    withdrawal_notification.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Withdrawal Entry
    tk.Entry(
        withdrawal_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        textvariable=withdrawal_amount
    ).grid(row=2, column=1, padx=10, pady=10)

    # Withdrawal Button
    tk.Button(
        withdrawal_screen,
        text="Finish Withdrawal",
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 14),
        command=withdrawal_click
    ).grid(row=3, column=0, columnspan=2, padx=10, pady=10)


# Function Called When Withdrawal Button Is Clicked
def withdrawal_math(rounded_withdrawal, current_balance):
    rounded_withdrawal_amount = rounded_withdrawal
    current_balance = current_balance
    updated_balance = current_balance - rounded_withdrawal_amount
    return updated_balance


def withdrawal_click():
    # Require User To Enter An Amount
    if withdrawal_amount.get() == "":
        withdrawal_notification.config(text="Enter An Amount", fg="red")
        withdrawal_amount.set("")
        return

    # Ensure Amount Is A Positive Value And Numeric
    try:
        if float(withdrawal_amount.get()) <= 0:
            withdrawal_notification.config(text="Negative Amount Not Allowed", fg="red")
            withdrawal_amount.set("")
            return
    except ValueError:
        withdrawal_notification.config(text="Enter Numeric Value", fg="red")
        withdrawal_amount.set("")
        return

    # Ensure Amount Is Less Than 10 Digits
    if len(withdrawal_amount.get()) >= 10:
        withdrawal_notification.config(text="Must Be Less Than 10 Digits", fg="red")
        withdrawal_amount.set("")
        return

    # Set The Directory Name For Account Access
    accounts_directory = "Accounts"
    file = open(os.path.join(accounts_directory, login_account_id), "r+")
    file_data = file.read()
    info = file_data.split("\n")

    # Assign Read Values To Variables
    account_id = info[0]
    name = info[1]
    email = info[2]
    password = info[3]
    current_balance = info[4]

    # Round Withdrawal Amount To The Nearest Cent
    rounded_withdrawal = round(float(withdrawal_amount.get()), 2)
    current_balance = float(current_balance)

    # Check If Withdrawal Amount Is Larger Than Balance
    if rounded_withdrawal > current_balance:
        withdrawal_notification.config(text="Insufficient Funds", fg="red")
        withdrawal_amount.set("")
        return

    # Call To withdrawal_math() To Calculate New Balance
    updated_balance = withdrawal_math(rounded_withdrawal, current_balance)

    # Round Updated Balance To The Nearest Cent Before Writing To Account File
    updated_balance = round(updated_balance, 2)

    # Format Updated Balance To Two Decimal Places
    updated_balance = "{:.2f}".format(updated_balance)

    # Clear Withdrawal Entry Box
    withdrawal_amount.set("")

    # Delete Old File Data
    file.seek(0)
    file.truncate(0)

    # Replace Old Balance With New Balance In Account File
    file.write(account_id + "\n")
    file.write(name + "\n")
    file.write(email + "\n")
    file.write(password + "\n")
    file.write(str(updated_balance))
    file.close()

    # Show User Updated Balance
    current_balance_label_w.config(text="Current Balance : $" + "{:,.2f}".format(float(updated_balance)), fg="green")
    withdrawal_notification.config(text="Balance Updated", fg="green")


# Function That Generates A Window For Balance
def balance():
    # Open User Account File
    accounts_directory = "Accounts"
    file = open(os.path.join(accounts_directory, login_account_id), "r")
    file_data = file.read()
    user_info = file_data.split("\n")

    # Read Values From File
    info_account_id = user_info[0]
    info_name = user_info[1]
    info_email = user_info[2]
    info_balance = user_info[4]

    # Balance Screen
    personal_info_screen = tk.Toplevel(root)
    personal_info_screen.title("Balance")

    # Set The Background Color
    personal_info_screen.config(background="#0a0c18")

    # Balance Labels
    tk.Label(
        personal_info_screen,
        text="Balance & Account Details",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 18)
    ).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(
        personal_info_screen,
        text="Account ID : " + info_account_id,
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(
        personal_info_screen,
        text="Name : " + info_name,
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(
        personal_info_screen,
        text="Email : " + info_email,
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(
        personal_info_screen,
        text="Balance : $" + "{:,.2f}".format(float(info_balance)),
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Function That Generates A Window For The Login Screen
def login():
    # Variables
    global temp_login_account_id
    global temp_login_password
    global login_notification
    global login_screen
    temp_login_account_id = tk.StringVar()
    temp_login_password = tk.StringVar()

    # Login Screen
    login_screen = tk.Toplevel(root)
    login_screen.title("Login")

    # Set The Background Color
    login_screen.config(background="#0a0c18")

    # Login Labels
    tk.Label(
        login_screen,
        text="Enter Details To Login",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 18)
    ).grid(row=0, column=0, columnspan=2, sticky="n", padx=10, pady=10)

    tk.Label(
        login_screen,
        text="Account ID",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=1, sticky="w", padx=5, pady=5)

    tk.Label(
        login_screen,
        text="Password",
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    ).grid(row=2, sticky="w", padx=5, pady=5)

    login_notification = tk.Label(
        login_screen,
        background="#0a0c18",
        foreground="#50d9da",
        font=("URW Gothic", 14)
    )
    login_notification.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    # Login Entries
    tk.Entry(
        login_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=25,
        textvariable=temp_login_account_id
    ).grid(row=1, column=1, padx=5, pady=5, sticky="e")

    tk.Entry(
        login_screen,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 12),
        width=25,
        textvariable=temp_login_password,
        show="$"
    ).grid(row=2, column=1, padx=5, pady=5, sticky="e")

    # Login Button
    tk.Button(
        login_screen,
        text="Login",
        command=login_click,
        width=15,
        background="#50d9da",
        foreground="#0a0c18",
        font=("URW Gothic", 14)
    ).grid(row=3, column=0, columnspan=2, pady=5, padx=5)


# Create A Help Bar
menu_bar = tk.Menu(
    root,
    background="#50d9da",
    foreground="#0a0c18",
    font=("URW Gothic", 14)
)

help_menu = tk.Menu(
    menu_bar,
    background="#50d9da",
    foreground="#0a0c18",
    font=("URW Gothic", 14),
    tearoff=0
)

# Create How To Use Tab
help_menu.add_command(
    label='How To Use...',
    background="#50d9da",
    foreground="#0a0c18",
    font=("URW Gothic", 14),
    command=help_click
)

# Create About Tab
help_menu.add_command(
    label='About',
    background="#50d9da",
    foreground="#0a0c18",
    font=("URW Gothic", 14),
    command=about_click
)

# Create Cascading Help Tab
menu_bar.add_cascade(
    label='Help',
    menu=help_menu,
    background="#50d9da",
    foreground="#0a0c18",
    font=("URW Gothic", 14)
)

# Configure Help Menu Bar
root.config(menu=menu_bar)

# Slogan Labels
tk.Label(
    root,
    text="Simplify Your Money",
    background="#0a0c18",
    foreground="#50d9da",
    font=("URW Gothic", 18)
).grid(row=0, sticky="n", pady=10)

tk.Label(
    root,
    text="Simplify Your Life",
    background="#0a0c18",
    foreground="#50d9da",
    font=("URW Gothic", 16)
).grid(row=1, sticky="n")

# Bankify Logo
photo = tk.PhotoImage(file="Bankify.png")
image_label = tk.Label(
    root,
    image=photo,
    background="#0a0c18",
    width=500,
    height=500
)
image_label.grid(row=2, pady=5)

# Create Account Button
tk.Button(
    root,
    text="Create Account",
    background="#50d9da",
    foreground="#0a0c18",
    font=("URW Gothic", 14),
    width=20,
    command=create_account
).grid(row=3, sticky="n", pady=10)

# Login Button
tk.Button(
    root,
    text="Login",
    background="#50d9da",
    foreground="#0a0c18",
    font=("URW Gothic", 14),
    width=20,
    command=login
).grid(row=4, sticky="n", pady=10)

# Call To Main Loop
if __name__ == "__main__":
    root.mainloop()
