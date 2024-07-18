import tkinter as tk

window = tk.Tk()
window.title("works To-Do")

tasks = []

task_entry = tk.Entry(window, width=50)
task_entry.pack()  

def add_task():
    task = task_entry.get()  
    if task: 
        listbox.insert(tk.END, task) 
        task_entry.delete(0, tk.END) 

add_button = tk.Button(window, text="Add a Task", command=add_task)
add_button.pack() 

listbox = tk.Listbox(window, width=50)
listbox.pack() 

def mark_complete():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        listbox.itemconfig(index, fg="gray")
mark_button = tk.Button(window, text="Mark Completed", command=mark_complete)
mark_button.pack()

def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        if tasks:
            del tasks[index]
            listbox.delete(index)
        else:
            print("Nothing to delete!!")

mark_button = tk.Button(window,text="delete", command=delete_task)
mark_button.pack()

window.mainloop()
