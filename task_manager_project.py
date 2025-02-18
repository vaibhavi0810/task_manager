import tkinter as tk
from tkinter import ttk, messagebox

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    messagebox.showinfo("Success", f'Added task: {task}')

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        messagebox.showinfo("Success", f'Deleted task: {removed_task["task"]}')
    except IndexError:
        messagebox.showwarning("Error", "Invalid task number")

def view_tasks():
    task_list.delete(0, tk.END)
    if not tasks:
        task_list.insert(tk.END, "No tasks available")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            task_list.insert(tk.END, f'{i + 1}. {task["task"]} [{status}]')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        messagebox.showinfo("Success", f'Marked task as completed: {tasks[task_index]["task"]}')
    except IndexError:
        messagebox.showwarning("Error", "Invalid task number")

def add_task_ui():
    task = task_entry.get()
    if task:
        add_task(task)
        task_entry.delete(0, tk.END)
        view_tasks()
    else:
        messagebox.showwarning("Error", "Task cannot be empty")

def delete_task_ui():
    try:
        task_index = int(task_index_entry.get()) - 1
        delete_task(task_index)
        task_index_entry.delete(0, tk.END)
        view_tasks()
    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid task number")

def mark_task_completed_ui():
    try:
        task_index = int(task_index_entry.get()) - 1
        mark_task_completed(task_index)
        task_index_entry.delete(0, tk.END)
        view_tasks()
    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid task number")

root = tk.Tk()
root.title("Task Manager")
root.geometry("500x500")
root.configure(bg='#e6f7ff')

# Set the color scheme and font styles
style = ttk.Style()
style.configure('TLabel', background='#e6f7ff', foreground='#003366', font=('Arial', 12, 'bold'))
style.configure('TEntry', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12, 'bold'), background='#ff6600', foreground='#ffffff')

frame = ttk.Frame(root, padding="10")
frame.pack(pady=10)

task_label = ttk.Label(frame, text="Enter Task:")
task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
task_entry = ttk.Entry(frame, width=30)
task_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

add_button = ttk.Button(frame, text="Add Task", command=add_task_ui)
add_button.grid(row=0, column=2, padx=5, pady=5)

task_list = tk.Listbox(root, width=50, height=10, font=('Arial', 12))
task_list.pack(pady=10)

task_index_label = ttk.Label(frame, text="Task Number:")
task_index_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
task_index_entry = ttk.Entry(frame, width=10)
task_index_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

complete_button = ttk.Button(frame, text="Mark Completed", command=mark_task_completed_ui)
complete_button.grid(row=1, column=2, padx=5, pady=5)

delete_button = ttk.Button(frame, text="Delete Task", command=delete_task_ui)
delete_button.grid(row=2, columnspan=3, padx=5, pady=10)

view_tasks()

root.mainloop()