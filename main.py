import tkinter as tk

class employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1300x650+0+0")
        self.mainLabel = tk.Label(self.root,bd=5,relief="groove", text="Employee Management System", font=("Arial", 40, "bold"), bg="black", fg="gold")
        self.mainLabel.pack(side=tk.TOP, fill=tk.X) 


        #......Fram1......
        self.Fram1 = tk.Frame(self.root, bd=5, relief="groove", width=350, height=550)
        self.Fram1.place(x=10, y=80)


        #......Fram2......
        self.Fram2 = tk.Frame(self.root, bd=5, relief="groove", width=900, height=550)
        self.Fram2.place(x=380, y=80)



root = tk.Tk()
obj = employee(root)
root.mainloop()
     