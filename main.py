from tkinter import *
from random import randint
from tkinter import messagebox

class App:
    keyset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'
    def __init__(self):
        self.root = Tk()
        self.root.title('Random Password Generator')
        self.root.geometry('600x400')
        self.root.maxsize(600, 400)

    def run(self):
        self.create_labels()
        self.create_input_box()
        self.root.mainloop()

    def create_labels(self):
        self.label_frame = Frame(self.root, height=50)
        self.label_frame.pack()
        self.control_frame = Frame(self.root, pady=20)
        self.control_frame.pack()
        self.app_label = Label(self.label_frame, text= "Generate random password of any length", font=('Times', 15))
        self.app_label.pack()

    def create_input_box(self):
        self.input_label = Label(self.control_frame, text= "Enter Password Length", font=('Times', 15))
        self.input_box = Entry(self.control_frame, width=20, font=('Times', 15))
        self.action_button = Button(self.control_frame, text='Generate Password', width=20, command=self.generate_password, font=('Times', 15), bg = "green")
        self.save_button = Button(self.control_frame, text='Save Password', width=20, command=self.save_password, font=('Times', 15), bg = "Yellow")
        self.output_label = Label(self.control_frame, text= "Random Password", font=('Times', 15))
        self.close_button = Button(self.control_frame, text='Close App', width=20, command=self.root.destroy, font=('Times', 15), bg='red')
        self.random_password = Label(self.control_frame, text= "", font=('Times', 15))
        self.input_label.grid(row=0, column=0, pady=20)
        self.input_box.grid(row=0, column=1)
        self.output_label.grid(row=1, column=0)
        self.random_password.grid(row=1, column=1)
        self.action_button.grid(row=2, column=1,pady = 20)
        self.save_button.grid(row=3, column=1,pady = 20)
        self.close_button.grid(row=4, column=1,pady = 20)

    def generate_password(self):
        try:
            key_length = int(self.input_box.get())
            if key_length <= 5:
                raise ValueError
            self.enc_key = ""
            for i in range(key_length):
                self.enc_key += self.keyset[randint(0,70)]
            self.random_password.config(text=self.enc_key)
            messagebox.showinfo(title='Success', message=f'Password Generated Successfully: {self.enc_key}')
        except Exception as e:
            messagebox.showerror(title='Error in operation', message='Password must be of 6 characters')
            self.input_box.focus()

    def save_password(self):
        try:
            if len(self.enc_key) == 0:
                raise ValueError
            from datetime import datetime
            with open("credential.txt","a+") as file: 
                file.write(f"Generated Password at time[{datetime.now()}]: {self.enc_key}\n")
            messagebox.showinfo(title='Success', message=f'Password Saved Successfully {self.enc_key}')
        except Exception as e:
            messagebox.showerror(title='Error in operation', message='Unable to open the file,\n Kindly try after some time!')

apk = App()
apk.run()