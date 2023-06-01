import sqlite3
from tkinter import *
from tkinter import messagebox
import random

import reservasi

room_number_taken = []

room_prices = {
    "Deluxe Room": 500000,
    "Family Room": 1200000,
    "Suite Room": 3000000
}



class CheckIN:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("CHECK IN")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.config(background="#A0C1B8")

        self.top = LabelFrame(self.root)
        self.top.pack(side="top")

        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")

        self.checkbox = Frame(self.root)
        self.checkbox.pack(side="top")

        # display message
        self.label = Label(self.top, font=('arial', 50, 'bold'), text="CHECK IN", fg="#709FB0", anchor="center")
        self.label.grid(row=0, column=3, padx=10, pady=10)

        # name label
        self.name_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Nama:", fg="#709FB0", anchor="w")
        self.name_label.grid(row=0, column=2, padx=10, pady=10)

        self.name_var = StringVar()

        # text enter field
        self.name_entry = Entry(self.bottom, width=50, textvar=self.name_var)
        self.name_entry.grid(row=0, column=3, padx=10, pady=10)

        # email label
        self.email_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Email:", fg="#709FB0", anchor="w")
        self.email_label.grid(row=1, column=2, padx=10, pady=10)

        # text enter field
        self.email_var = StringVar()
        self.email_entry = Entry(self.bottom, width=50, textvar=self.email_var)
        self.email_entry.grid(row=1, column=3, padx=10, pady=10)

        # room type label
        self.room_type_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Tipe Kamar:", fg="#709FB0", anchor="w")
        self.room_type_label.grid(row=2, column=2, padx=10, pady=10)

        # room type options
        self.room_type_var = StringVar()
        self.room_type_var.set("Choose a room type")
        self.room_type_options = ["Deluxe Room", "Family Room", "Suite Room"]
        self.room_type_menu = OptionMenu(self.bottom, self.room_type_var, *self.room_type_options)
        self.room_type_menu.config(width=45)
        self.room_type_menu.grid(row=2, column=3, padx=10, pady=10)

        # room number label
        self.room_number_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Nomor Kamar:", fg="#709FB0", anchor="w")
        self.room_number_label.grid(row=3, column=2, padx=10, pady=10)

        # text enter field
        self.room_number_var = IntVar()
        self.room_number_entry = Entry(self.bottom, width=50, textvar=self.room_number_var)
        self.room_number_entry.grid(row=3, column=3, padx=10, pady=10)

        # day label
        self.day_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Jumlah Malam:", fg="#709FB0", anchor="w")
        self.day_label.grid(row=4, column=2, padx=10, pady=10)

        # text enter field
        self.day_var = IntVar()
        self.day_entry = Entry(self.bottom, width=50, textvar=self.day_var)

        # price label
        self.price_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Harga:", fg="#709FB0", anchor="w")
        self.price_label.grid(row=5, column=2, padx=10, pady=10)

        # text enter field
        self.price_var = DoubleVar()
        self.price_entry = Entry(self.bottom, width=50, textvar=self.price_var, state="readonly")
        self.price_entry.grid(row=5, column=3, padx=10, pady=10)

        def on_entry_complete(event):
            price = room_prices[self.room_type_var.get()] * self.day_var.get()
            self.price_var.set(price)

        self.day_entry.bind("<FocusOut>", on_entry_complete)
        self.day_entry.grid(row=4, column=3, padx=10, pady=10)

        # payment label
        self.payment_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Pembayaran:", fg="#709FB0", anchor="w")
        self.payment_label.grid(row=6, column=2, padx=10, pady=10)

        # text enter field
        self.payment_var = DoubleVar()
        self.payment_entry = Entry(self.bottom, width=50, textvar=self.payment_var)
        
        def on_kembalian_complete(event):
            kembalian = self.payment_var.get() - self.price_var.get()
            self.kembalian_var.set(kembalian)

        self.payment_entry.bind("<FocusOut>", on_kembalian_complete)
        self.payment_entry.grid(row=6, column=3, padx=10, pady=10)

        # kembalian label
        self.kembalian_label = Label(self.bottom, font=('arial', 20, 'bold'), text="Kembalian:", fg="#709FB0", anchor="w")
        self.kembalian_label.grid(row=7, column=2, padx=10, pady=10)

        # kembalian enter field
        self.kembalian_var = DoubleVar()
        self.kembalian_entry = Entry(self.bottom, width=50, textvar=self.kembalian_var, state="readonly")

        self.kembalian_entry.grid(row=7, column=3, padx=10, pady=10)

        def submit_info():
            name = self.name_entry.get()
            email = self.email_entry.get()
            room_type = self.room_type_var.get()
            room_number = self.room_number_var.get()
            day = self.day_var.get()
            price = self.price_var.get()
            payment = self.payment_var.get()
            kembalian = self.kembalian_var.get()

            if not room_numberf():
                reset()
                return
            
            if kembalian < 0:
                messagebox.showerror("Error", "Masukan jumlah payment dengan benar")
                return

            # Validate the inputs (you can add your own validation logic)

            # Database operations
            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS Hotels (Name TEXT, Email TEXT, RoomType TEXT, RoomNumber Number, Day Number, Price REAL, Payment Real, Kembalian Real)')
                cursor.execute('INSERT INTO Hotels (Name, Email, RoomType, RoomNumber, Day, Price, Payment, Kembalian) VALUES(?,?,?,?,?,?,?,?)',
                            (name, email, room_type, room_number, day, price, payment, kembalian))
                conn.commit()
            messagebox.showinfo("Success", "Berhasil check in!")

        def room_numberf():
            conn = sqlite3.connect('Hotel.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS Hotels (Name TEXT, Email TEXT, RoomType TEXT, RoomNumber Number, Day Number, Price REAL, Payment Real, Kembalian Real)')
                cursor.execute("SELECT RoomNumber FROM Hotels")  # Select all room numbers
                rows = cursor.fetchall()
                room_numbers = [row[0] for row in rows]  # Create a list of room numbers
            if self.room_number_var.get() in room_numbers:
                messagebox.showerror("Error", "Kamar sudah terisi.")
                return False
            return True

        def reset():
            # Reset the form fields
            self.name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.room_type_var.set("Choose Room Type")
            self.room_number_entry.set(0, END)
            self.day_var.delete(0, END)
            self.price_var.set(0, END)
            self.payment_var.delete(0, END)
            self.kembalian_var.delete(0, END)

        # create submit button
        self.submit_button = Button(self.checkbox, text="Submit", font=('', 15), bg="#709FB0", relief=RIDGE, height=2, width=15, fg="black", anchor="center", command=submit_info)
        self.submit_button.grid(row=8, column=1, padx=10, pady=10)

        # back to home page
        def home_and_destroy():
            self.root.destroy()
            reservasi.home_ui()

        self.back_home_button = Button(self.checkbox, text="Home", font=('', 15), bg="#709FB0", relief=RIDGE, height=2, width=15, fg="black", anchor="center", command=home_and_destroy)
        self.back_home_button.grid(row=8, column=2, padx=10, pady=10)


        Button(self.checkbox, text="Reset", font=('', 15), bg="#709FB0", relief=RIDGE, height=2, width=15, fg="black", anchor="center", command=reset).grid(row=8, column=3)



def check_in_ui_fun():
    root = Tk()
    application = CheckIN(root)
    root.mainloop()
