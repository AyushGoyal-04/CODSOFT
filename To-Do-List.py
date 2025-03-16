import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.title}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def view_tasks(self):
        return [str(task) for task in self.tasks]

    def update_task(self, index, new_title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title
        else:
            raise IndexError("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise IndexError("Invalid task number.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            raise IndexError("Invalid task number.")

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.view_tasks():
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            self.todo_list.add_task(title)
            self.refresh_task_list()

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_title = simpledialog.askstring("Update Task", "Enter new task title:")
            if new_title:
                self.todo_list.update_task(selected_index, new_title)
                self.refresh_task_list()
        except IndexError:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.todo_list.delete_task(selected_index)
            self.refresh_task_list()
        except IndexError:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def mark_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.todo_list.mark_task_completed(selected_index)
            self.refresh_task_list()
        except IndexError:
            messagebox.showwarning("Mark as Completed", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()