import tkinter as tk

class employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

root = tk.Tk()
obj = employee(root)
root.mainloop()
     