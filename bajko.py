import tkinter as tk
from tkinter import messagebox
import random

wallet = 50  # Globális változóként definiált pénztárca
wallet_label = None  # Globális változóként definiált címke

def purchase(item, price):
    global wallet
    if wallet >= price:
        wallet -= price
        update_wallet_label()
        messagebox.showinfo("Purchase", f"Thank you for purchasing {item}!")
    else:
        messagebox.showerror("Error", "Not enough funds in your wallet!")

def update_wallet_label():
    wallet_label.config(text=f"Wallet: ${wallet}")

def login():
    username = "aliz2023!"
    password = "2012"
    if username_entry.get() == username and password_entry.get() == password:
        open_shop_window()
    else:
        show_error()

def open_shop_window():
    global wallet_label  # Hozzáadva a globális változókhoz
    # Fő ablak
    root = tk.Tk()
    root.title("Shop")

    # Terméklista
    products = {"Apple 🍎": 10, "Pasta 🍜": 20, "Soup 🚡": 15, "Milk 🥛": 25}

    # Fő ablak konfigurációja
    root.geometry('400x400')
    root.configure(bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)))  # Véletlenszerű háttérszín

    # Cím
    title_label = tk.Label(root, text="Welcome to the Shop", bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg="#FF3399", font=("Arial", 20))
    title_label.pack(pady=20)

    # Terméklista megjelenítése
    for product, price in products.items():
        product_button = tk.Button(root, text=f"{product} - ${price}", bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), font=("Arial", 14),
                                   command=lambda p=product, pr=price: purchase(p, pr))
        product_button.pack(pady=10)

    # Pénztárca címke
    wallet_label = tk.Label(root, text=f"Wallet: ${wallet}", bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), font=("Arial", 14))
    wallet_label.pack(pady=20)

    # Fő ablak megjelenítése
    root.mainloop()

def show_error():
    # Hibaablak
    error_root = tk.Tk()
    error_root.title("Error")
    error_root.config(bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)))  # Véletlenszerű háttérszín

    error_label = tk.Label(error_root, text="ERROR", fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)))  # Szöveg és háttérszín véletlenszerű
    error_label.pack()

frame = tk.Frame(bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)))  # Véletlenszerű háttérszín

# Creating widgets
login_label = tk.Label(
    frame, text="Login", bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), font=("Arial", 30))
username_label = tk.Label(
    frame, text="Username", bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16), bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)))  # Véletlenszerű háttérszín
password_entry = tk.Entry(frame, show="*", font=("Arial", 16), bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)))  # Véletlenszerű háttérszín
password_label = tk.Label(
    frame, text="Password", bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), font=("Arial", 16))
login_button = tk.Button(
    frame, text="Login", bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), fg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)), font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window = tk.Tk()
window.title("Login admin")
window.geometry('340x440')
window.configure(bg='#' + ''.join(random.choice('0123456789ABCDEF') for i in range(6)))  # Véletlenszerű háttérszín
window.mainloop()
