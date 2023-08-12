# import tkinter as tk
# import random

# def generate_password():
#     capchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     spchar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', ',', '.']
#     smallchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
#     passlen = int(length_entry.get())
#     capans = cap_var.get()
#     smallans = small_var.get()
#     digans = dig_var.get()
#     spans = sp_var.get()
    
#     comblis = []
    
#     if capans:
#         comblis += capchar
#     if smallans:
#         comblis += smallchar
#     if digans:
#         comblis += dig
#     if spans:
#         comblis += spchar
    
#     if not comblis:
#         result_label.config(text="Error: No characters selected")
#         return
    
#     password = ""
#     random.shuffle(comblis)
    
#     for _ in range(passlen):
#         password += random.choice(comblis)
    
#     result_label.config(text="Generated Password: " + password)

# # Create GUI window
# window = tk.Tk()
# window.title("Password Generator")

# # Length entry
# length_label = tk.Label(window, text="Password Length:")
# length_label.pack()
# length_entry = tk.Entry(window)
# length_entry.pack()

# # Checkboxes for character types
# cap_var = tk.BooleanVar()
# cap_check = tk.Checkbutton(window, text="Capital Letters", variable=cap_var)
# cap_check.pack()

# small_var = tk.BooleanVar()
# small_check = tk.Checkbutton(window, text="Lowercase Letters", variable=small_var)
# small_check.pack()

# dig_var = tk.BooleanVar()
# dig_check = tk.Checkbutton(window, text="Digits", variable=dig_var)
# dig_check.pack()

# sp_var = tk.BooleanVar()
# sp_check = tk.Checkbutton(window, text="Special Characters", variable=sp_var)
# sp_check.pack()

# # Generate button
# generate_button = tk.Button(window, text="Generate Password", command=generate_password)
# generate_button.pack()

# # Result label
# result_label = tk.Label(window, text="")
# result_label.pack()

# # Start GUI event loop
# window.mainloop()
# import tkinter as tk
# import random
# def generate_password():
#     capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#     small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#     digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#     special = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']

   
# print('💫✨Welcome To New Innovation✨💫')
# Name=input('Enter The Name: ')
# Email=input('Enter The Mail ID: ')
# password_length = int(input('Enter the* length of Password: '))
# capital_letter = str(input('You Want Capital Letters Allowed? (Y/N): '))
# small_letter = str(input('You Want to Allow Small letters? (Y/N): '))
# digits = str(input('You Want to Allow digits? (Y/N): '))
# specials = str(input('You Want to Allow Special characters? (Y/N): '))

# #combination = []

# if capital_letter == 'Y':
#     if small_letter == 'Y':
#         if digits == 'Y':
#             if specials == 'Y':
#                 combination = capital + digit + special + small
#             else:
#                 combination = capital + digit + small
#         else:
#             if specials == 'Y':
#                 combination = capital + special + small
#             else:
#                 combination = capital + small
#     else:
#         if digits == 'Y':
#             if specials == 'Y':
#                 combination = capital + digit + special
#             else:
#                 combination = capital + digit
#         else:
#             if specials == 'Y':
#                 combination = capital + special
#             else:
#                 print("Error, Invalid Choice")
#                 exit()
# else:
#     if small_letter == 'Y':
#         if digits == 'Y':
#             if specials == 'Y':
#                 combination = digit + special + small
#             else:
#                 combination = digit + small
#         else:
#             if specials == 'Y':
#                 combination = special + small
#             else:
#                 combination = small
#     else:
#         if digits == 'Y':
#             if specials == 'Y':
#                 combination = digit + special
#             else:
#                 combination = digit
#         else:
#             if specials == 'Y':
#                 combination = special
#             else:
#                 print("Error, Invalid Choice")
#                 exit()

# password = ''
# for i in range(password_length):
#     password = combination[random.randint(0, len(combination)-1)]
    

# random.shuffle(combination)
# for i in range(password_length):
#     q = random.choice(combination)
#     random.shuffle(combination)
#     password += q

# print("\nGenerated Password is:",password)

# import random
# import tkinter as tk

# capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# special = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']


# password = tk.Tk()
# password.configure(bg='sky blue')  

# def generate_password():
#     print('Welcome To New Innovation')
#     Name = input_name.get()
#     Email = input_email.get()
#     password_length = int(input_length.get())
#     capital_letter = input_capital.get()
#     small_letter = input_small.get()
#     digits = input_digits.get()
#     specials = input_specials.get()

#     combination = []
    
#     if capital_letter == 'Y':
#         if small_letter == 'Y':
#             if digits == 'Y':
#                 if specials == 'Y':
#                     combination = capital + digit + special + small
#                 else:
#                     combination = capital + digit + small
#             else:
#                 if specials == 'Y':
#                     combination = capital + special + small
#                 else:
#                     combination = capital + small
#         else:
#             if digits == 'Y':
#                 if specials == 'Y':
#                     combination = capital + digit + special
#                 else:
#                     combination = capital + digit
#             else:
#                 if specials == 'Y':
#                     combination = capital + special
#                 else:
#                     print("Error, Invalid Choice")
#                     return
#     else:
#         if small_letter == 'Y':
#             if digits == 'Y':
#                 if specials == 'Y':
#                     combination = digit + special + small
#                 else:
#                     combination = digit + small
#             else:
#                 if specials == 'Y':
#                     combination = special + small
#                 else:
#                     combination = small
#         else:
#             if digits == 'Y':
#                 if specials == 'Y':
#                     combination = digit + special
#                 else:
#                     combination = digit
#             else:
#                 if specials == 'Y':
#                     combination = special
#                 else:
#                     print("Error, Invalid Choice")
#                     return

#     password = ''
#     for i in range(password_length):
#         password += random.choice(combination)

#     password_label.config(text="Generated Password is: " + password)

# # Create input fields and labels
# welcome_label = tk.Label(password, text='Welcome To New Innovation',fg='black')
# welcome_label.pack()

# input_name_label = tk.Label(password, text="Enter The Name:",fg='black')
# input_name_label.pack()
# input_name = tk.Entry(password)
# input_name.pack()

# input_email_label = tk.Label(password, text="Enter The Mail ID:",fg='black')
# input_email_label.pack()
# input_email = tk.Entry(password)
# input_email.pack()

# input_length_label = tk.Label(password, text="Enter the length of Password:", fg='black')
# input_length_label.pack()
# input_length = tk.Entry(password)
# input_length.pack()

# input_capital_label = tk.Label(password, text="You Want Capital Letters Allowed? (Y/N):",fg='black')
# input_capital_label.pack()
# input_capital = tk.Entry(password)
# input_capital.pack()

# input_small_label = tk.Label(password, text="You Want to Allow Small letters? (Y/N):",fg='black')
# input_small_label.pack()
# input_small = tk.Entry(password)
# input_small.pack()

# input_digits_label = tk.Label(password, text="You Want to Allow digits? (Y/N):",fg='black')
# input_digits_label.pack()
# input_digits = tk.Entry(password)
# input_digits.pack()

# input_specials_label = tk.Label(password, text="You Want to Allow Special characters? (Y/N):",fg='black')
# input_specials_label.pack()
# input_specials = tk.Entry(password)
# input_specials.pack()

# generate_button = tk.Button(password, text="Generate Password", command=generate_password,fg='black')
# generate_button.pack()

# password_label = tk.Label(password, text="",fg='black')
# password_label.pack()

import random
import tkinter as tk

capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']

password = tk.Tk()
password.configure(bg='sky blue')

def generate_password():
    print('Welcome To New Innovation')
    Name = input_name.get()
    Email = input_email.get()
    password_length = int(input_length.get())
    capital_letter = input_capital.get()
    small_letter = input_small.get()
    digits = input_digits.get()
    specials = input_specials.get()

    combination = []

    if capital_letter == 'Y':
        if small_letter == 'Y':
            if digits == 'Y':
                if specials == 'Y':
                    combination = capital + digit + special + small
                else:
                    combination = capital + digit + small
            else:
                if specials == 'Y':
                    combination = capital + special + small
                else:
                    combination = capital + small
        else:
            if digits == 'Y':
                if specials == 'Y':
                    combination = capital + digit + special
                else:
                    combination = capital + digit
            else:
                if specials == 'Y':
                    combination = capital + special
                else:
                    print("Error, Invalid Choice")
                    return
    else:
        if small_letter == 'Y':
            if digits == 'Y':
                if specials == 'Y':
                    combination = digit + special + small
                else:
                    combination = digit + small
            else:
                if specials == 'Y':
                    combination = special + small
                else:
                    combination = small
        else:
            if digits == 'Y':
                if specials == 'Y':
                    combination = digit + special
                else:
                    combination = digit
            else:
                if specials == 'Y':
                    combination = special
                else:
                    print("Error, Invalid Choice")
                    return

    password = ''
    for i in range(password_length):
        password += random.choice(combination)

    password_label.config(text="Generated Password is: " + password)

# Create input fields and labels
welcome_label = tk.Label(password, text='Welcome To New Innovation', fg='black')
welcome_label.grid(row=0, column=0, columnspan=2)

input_name_label = tk.Label(password, text="Enter The Name:", fg='black')
input_name_label.grid(row=1, column=0)
input_name = tk.Entry(password)
input_name.grid(row=1, column=1)

input_email_label = tk.Label(password, text="Enter The Mail ID:", fg='black')
input_email_label.grid(row=2, column=0)
input_email = tk.Entry(password)
input_email.grid(row=2, column=1)

input_length_label = tk.Label(password, text="Enter the length of Password:", fg='black')
input_length_label.grid(row=3, column=0)
input_length = tk.Entry(password)
input_length.grid(row=3, column=1)

input_capital_label = tk.Label(password, text="You Want Capital Letters Allowed? (Y/N):", fg='black')
input_capital_label.grid(row=4, column=0)
input_capital = tk.Entry(password)
input_capital.grid(row=4, column=1)

input_small_label = tk.Label(password, text="You Want to Allow Small letters? (Y/N):", fg='black')
input_small_label.grid(row=5, column=0)
input_small = tk.Entry(password)
input_small.grid(row=5, column=1)

input_digits_label = tk.Label(password, text="You Want to Allow digits? (Y/N):", fg='black')
input_digits_label.grid(row=6, column=0)
input_digits = tk.Entry(password)
input_digits.grid(row=6, column=1)

input_specials_label = tk.Label(password, text="You Want to Allow Special characters? (Y/N):", fg='black')
input_specials_label.grid(row=7, column=0)
input_specials = tk.Entry(password)
input_specials.grid(row=7, column=1)

generate_button = tk.Button(password, text="Generate Password", command=generate_password, fg='black')
generate_button.grid(row=8, column=0, columnspan=2)

password_label = tk.Label(password, text="", fg='black')
password_label.grid(row=9, column=0, columnspan=2)

password.mainloop()

       
                  
