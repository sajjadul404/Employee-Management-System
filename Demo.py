import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

FILE_NAME = "employees.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Salary", "Contact"])


def add_employee():
    eid = entry_id.get()
    name = entry_name.get()
    dept = entry_dept.get()
    salary = entry_salary.get()
    contact = entry_contact.get()

    if eid == "" or name == "" or dept == "" or salary == "" or contact == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([eid, name, dept, salary, contact])

    messagebox.showinfo("Success", "Employee Added Successfully")
    clear_fields()
    view_employees()


def view_employees():
    for row in table.get_children():
        table.delete(row)

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            table.insert("", tk.END, values=row)


def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dept.delete(0, tk.END)
    entry_salary.delete(0, tk.END)
    entry_contact.delete(0, tk.END)


def delete_employee():
    selected = table.selection()
    if not selected:
        messagebox.showerror("Error", "Select a record to delete")
        return

    values = table.item(selected)["values"]
    eid = values[0]

    rows = []
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row and row[0] != eid:
                writer.writerow(row)

    messagebox.showinfo("Success", "Employee Deleted")
    view_employees()


def search_employee():
    keyword = entry_search.get().lower()

    for row in table.get_children():
        table.delete(row)

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if keyword in row[0].lower() or keyword in row[1].lower():
                table.insert("", tk.END, values=row)


def update_employee():
    selected = table.selection()
    if not selected:
        messagebox.showerror("Error", "Select a record to update")
        return

    eid = entry_id.get()
    name = entry_name.get()
    dept = entry_dept.get()
    salary = entry_salary.get()
    contact = entry_contact.get()

    rows = []
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row and row[0] == eid:
                writer.writerow([eid, name, dept, salary, contact])
            else:
                writer.writerow(row)

    messagebox.showinfo("Success", "Employee Updated")
    view_employees()


def select_item(event):
    selected = table.selection()
    if not selected:
        return

    values = table.item(selected)["values"]
    clear_fields()
    entry_id.insert(0, values[0])
    entry_name.insert(0, values[1])
    entry_dept.insert(0, values[2])
    entry_salary.insert(0, values[3])
    entry_contact.insert(0, values[4])


# GUI
root = tk.Tk()
root.title("Employee Management System")
root.geometry("800x500")

# Labels & Entries
tk.Label(root, text="Employee ID").place(x=20, y=20)
entry_id = tk.Entry(root)
entry_id.place(x=150, y=20)

tk.Label(root, text="Name").place(x=20, y=60)
entry_name = tk.Entry(root)
entry_name.place(x=150, y=60)

tk.Label(root, text="Department").place(x=20, y=100)
entry_dept = tk.Entry(root)
entry_dept.place(x=150, y=100)

tk.Label(root, text="Salary").place(x=20, y=140)
entry_salary = tk.Entry(root)
entry_salary.place(x=150, y=140)

tk.Label(root, text="Contact").place(x=20, y=180)
entry_contact = tk.Entry(root)
entry_contact.place(x=150, y=180)

# Buttons
tk.Button(root, text="Add", width=12, command=add_employee).place(x=20, y=230)
tk.Button(root, text="Update", width=12, command=update_employee).place(x=120, y=230)
tk.Button(root, text="Delete", width=12, command=delete_employee).place(x=220, y=230)
tk.Button(root, text="Clear", width=12, command=clear_fields).place(x=320, y=230)

# Search
tk.Label(root, text="Search (ID/Name)").place(x=450, y=20)
entry_search = tk.Entry(root)
entry_search.place(x=600, y=20)
tk.Button(root, text="Search", command=search_employee).place(x=600, y=50)
tk.Button(root, text="Show All", command=view_employees).place(x=680, y=50)

# Table
columns = ("ID", "Name", "Department", "Salary", "Contact")
table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)

table.place(x=400, y=100, width=380, height=350)
table.bind("<ButtonRelease-1>", select_item)

view_employees()
root.mainloop()
