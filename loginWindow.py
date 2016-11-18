from tkinter import *

# Finale Project
# CIS 4930 Advanced Python Fall 2016
# Team: Vladislav Ignatov, Leonard Holloman
# Date: 11/3/2016

class Login_Window:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        # Title for the Login Window 
        master.wm_title("Login Window")

        # Size of window
        master.minsize(width=300, height=100)

		# Lable for Username and Password
        self.username_lable = Label(frame, text="Username: ")
        self.username_lable.grid(row=0, sticky=E)
        self.password_lable = Label(frame, text="Password: ")
        self.password_lable.grid(row=1, sticky=E)

        # Entry for Username and Password
        self.username_entry = Entry(frame)
        self.username_entry.grid(row=0, column=1)
        self.password_entry = Entry(frame)
        self.password_entry.grid(row=1, column=1)

        # Login button
        self.Login_Button = Button(frame, text="Login", width=10, command=self.Login)
        self.Login_Button.grid(columnspan=2)

        # Exit button to get out of application
        self.Exit_button = Button(frame, text="Exit", width=10, command=frame.quit)
        self.Exit_button.grid(columnspan=2)

    # Login function
    def Login(self):
    	# TODO input validation if username is blank or ...
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Login Test: (Username: " + str(username) + " Password: " + str(password) + ")")
        # TODO implement Login DB verification

if __name__ == "__main__":
	root = Tk()
	app = Login_Window(root)
	root.mainloop()
	root.destroy()