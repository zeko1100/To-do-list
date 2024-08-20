import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, window):
        self.window = window
        self.window.title("Task Manager")

        # Task storage
        self.task_list = []

        # Input field for new tasks
        self.input_field = tk.Entry(window, width=40)
        self.input_field.grid(row=0, column=0, padx=10, pady=10)

        # Button to add a task
        self.add_button = tk.Button(window, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_display = tk.Listbox(window, width=50, height=15, selectmode=tk.SINGLE)
        self.task_display.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for updating, deleting, and marking tasks
        self.update_button = tk.Button(window, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.remove_button = tk.Button(window, text="Delete Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        self.complete_button = tk.Button(window, text="Mark as Done", command=self.mark_done)
        self.complete_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_task(self):
        task_content = self.input_field.get()
        if task_content != "":
            self.task_list.append({'content': task_content, 'done': False})
            self.refresh_task_display()
            self.input_field.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def refresh_task_display(self):
        self.task_display.delete(0, tk.END)
        for idx, task in enumerate(self.task_list):
            status = "--> Done" if task['done'] else "--> X"
            self.task_display.insert(tk.END, f"{idx + 1}. {task['content']} [{status}]")

    def update_task(self):
        selected_idx = self.task_display.curselection()
        if selected_idx:
            updated_task = self.input_field.get()
            if updated_task != "":
                self.task_list[selected_idx[0]]['content'] = updated_task
                self.refresh_task_display()
                self.input_field.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a task description.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def remove_task(self):
        selected_idx = self.task_display.curselection()
        if selected_idx:
            del self.task_list[selected_idx[0]]
            self.refresh_task_display()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        selected_idx = self.task_display.curselection()
        if selected_idx:
            self.task_list[selected_idx[0]]['done'] = True
            self.refresh_task_display()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

