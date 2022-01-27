from operator import itemgetter
from textwrap import fill
from tkinter import *
from tkinter import ttk


class Todo:
    def __init__(self, root):
        #========== Create and cofigurate the file of the To Do List ==========#
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App',
            font='arial, 25 bold', width=10, bd=5, bg='green', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
            font='arial, 18 bold', width=10, bd=5, bg='green', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
            font='arial, 18 bold', width=10, bd=5, bg='green', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=33, font="arial, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='arial, 10 bold')
        self.text.place(x=20, y=120)

    #========== Add task ==========#

    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
            file.seek(0)
        self.text.delete(1.0, END)
        
    #========== Delete task ==========#  

    def delete(self):
        delete_ = self.main_text.curselection()
        look = self.main_text.get(delete_)
        with open('data.txt', 'r+') as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                item = str(look)
                if item not in line:
                    f.write(line)
            f.truncate()
        self.main_text.delete(delete_)

    #========== Run the required operations ==========#         
    
    def run_operation(self):
        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        #========== Configure the add and delete buttons ==========# 
        
        button = Button(self.root, text= "Add", font='sarif, 20 bold italic',
            width=10, bd=5, bg='green', fg='black', command=self.add)
        button.place(x=3, y=180)

        button2 = Button(self.root, text= "Delete", font='sarif, 20 bold italic',
            width=10, bd=5, bg='green', fg='black', command=self.delete)
        button2.place(x=3, y=280)


if __name__ == "__main__":
    root = Tk()
    ui = Todo(root)
    ui.run_operation()
    root.mainloop()
