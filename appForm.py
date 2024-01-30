# from tkinter import *
# from tkinter import ttk  # Import ttk module
# from tkinter import messagebox

# class Login:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Login Form")
#         self.root.geometry("1199x600+200+250")
        
        
#         # Login frame
#         frame_login = Frame(self.root, bg="#66c2ff")  # Background color
#         frame_login.place(x=150, y=150, height=540, width=500)

#         title = ttk.Label(frame_login, text="Login In", font=("monospace", 35, "bold"), foreground="#ffffff", background="#66c2ff")
#         title.place(x=90, y=30)
        
#         desc = ttk.Label(frame_login, text="Welcome back", font=("monospace", 15, "bold"), 
#                          foreground="#ffffff", background="#66c2ff")
#         desc.place(x=90, y=100)

#         lbl_user = ttk.Label(frame_login, text="Name", font=("monospace", 15, "bold"), foreground="Grey", background="#66c2ff")
#         lbl_user.place(x=90, y=140)

#         self.txt_user = Entry(frame_login, font=("monospace", 15))
#         self.txt_user.place(x=90, y=170, width=350, height=35)

#         lbl_pass = ttk.Label(frame_login, text="Password", font=("monospace", 15, "bold"), foreground="Grey", background="#66c2ff")
#         lbl_pass.place(x=90, y=210)

#         self.txt_pass = Entry(frame_login, font=("monospace", 15))
#         self.txt_pass.place(x=90, y=240, width=350, height=35)
        
#         forget_btn = Button(frame_login, text="Forget your password?", bg="white",  bd=0, font=("monospace", 12))
#         forget_btn.place(x=90, y=280)

#         login_btn = Button(self.root, text="Login", fg="white", bg="#d77337", bd=0, font=("monospace", 20), 
#                            command=self.login)
#         login_btn.place(x=300, y=470, width=180, height=40)

#         # Start the Tkinter event loop
#         self.root.mainloop()

#     def login(self):
#         if self.txt_pass.get() == "" or self.txt_user.get() == "":
#             messagebox.showerror("Error", "All fields are required", parent=self.root)

# if __name__ == "__main__":
#     root = Tk()
#     obj = Login(root)

#====================================

from tkinter import *
from tkinter import ttk  # Import ttk module
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("1199x600+200+250")

        def validateLogin(username, password):
            # Add your validation logic here
            entered_username = username.get()
            entered_password = password.get()

            # Example validation logic (replace this with your actual logic)
            if entered_username == "red-dog" and entered_password == "password":
                print("Login successful")
            else:
                messagebox.showerror("Something is wrong !", "Why Am I Getting Invalid Password?" "Username is 'red-dog' Password is 'password ' ", parent=self.root)

        # Login frame
        frame_login = Frame(self.root, bg="#66c2ff")  # Background color
        frame_login.place(x=150, y=150, height=540, width=500)

        title = ttk.Label(frame_login, text="Login In", font=("monospace", 35, "bold"), foreground="#ffffff", background="#66c2ff")
        title.place(x=90, y=30)
        
        desc = ttk.Label(frame_login, text="Welcome back", font=("monospace", 15, "bold"), 
                         foreground="#ffffff", background="#66c2ff")
        desc.place(x=90, y=100)

        lbl_user = ttk.Label(frame_login, text="Name", font=("monospace", 15, "bold"), foreground="Grey", background="#66c2ff")
        lbl_user.place(x=90, y=140)

        self.txt_user = Entry(frame_login, font=("monospace", 15))
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = ttk.Label(frame_login, text="Password", font=("monospace", 15, "bold"), foreground="Grey", background="#66c2ff")
        lbl_pass.place(x=90, y=210)

        self.txt_pass = Entry(frame_login, font=("monospace", 15), show='*')
        self.txt_pass.place(x=90, y=240, width=350, height=35)
        
        forget_btn = Button(frame_login, text="Forget your password?", bg="white", bd=0, font=("monospace", 12))
        forget_btn.place(x=90, y=280)

        # Call validateLogin function when login button is clicked
        login_btn = Button(self.root, text="Login", fg="white", bg="#d77337", bd=0, font=("monospace", 20), 
                           command=lambda: validateLogin(self.txt_user, self.txt_pass))
        login_btn.place(x=300, y=470, width=180, height=40)

        # Start the Tkinter event loop
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
