from tkinter import *
import check_in_ui
import os


class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL PESONA ALAM")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.config(background="#F4E8C1")

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # display message
        self.label = Label(top, font=('arial', 50, 'bold'), text="WELCOME TO PESONA ALAM HOTEL", fg="#709FB0", anchor="center")
        self.label.grid(row=0, column=3)

        def chekin_destroy():
            self.root.destroy()
            check_in_ui.check_in_ui_fun()

        # create check in button
        self.check_in_button = Button(bottom, text="CHECK IN", font=('', 20), bg="#A0C1B8", relief=RIDGE, height=2,
                                      width=50,
                                      fg="black", anchor="center",
                                      command=chekin_destroy)  # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

       

        # create button to exit the program
        self.exit_button = Button(bottom, text="EXIT", font=('', 20), bg="#A0C1B8", relief=RIDGE, height=2, width=50,
                                  fg="black",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=1, column=2, padx=10, pady=10)



def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()

if __name__ == '__main__':
    home_ui()

