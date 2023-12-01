from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do-list")
        self.root.geometry("650x510+300+150")

        self.label = Label(self.root, text="To-Do-List",
                           font="ariel, 25 bold", width=10, bd=5, bg="pink", fg="red")
        self.label.pack(side="top", fill=BOTH)

        self.label2 = Label(self.root, text="Add Task",
                            font="ariel, 18 bold", width=10, bd=5, bg="pink", fg="black")
        self.label2.place(x=40, y=58)

        self.label3 = Label(self.root, text="Tasks",
                            font="ariel, 18 bold", width=10, bd=5, bg="pink", fg="black")
        self.label3.place(x=370, y=58)

        self.main_text = Listbox(self.root, height=11, bd=5, width=25, font="ariel, 20 italic bold")
        self.main_text.place(x=260, y=120)

        self.text = Text(self.root, bd=5, height=2, width=30, font="ariel, 10 bold")
        self.text.place(x=20, y=120)

        # ========== Add Task ==========
        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open("data.txt", "a") as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        # ========== Delete Task ==========
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open("data.txt", "r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        def complete():
            selected_index = self.main_text.curselection()
            if selected_index:
                item = self.main_text.get(selected_index)
                self.main_text.delete(selected_index)
                self.main_text.insert(END, f'{item.strip()} (Completed)')

        def incomplete():
            selected_index = self.main_text.curselection()
            if selected_index:
                item = self.main_text.get(selected_index)
                self.main_text.delete(selected_index)
                self.main_text.insert(END, f'{item.strip()} (Incomplete)')


        with open("data.txt", "r") as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        # ========== Buttons ==========
        self.add_button = Button(self.root, text="Add", font="sarif, 20 bold italic",
                                 width=10, bd=5, bg="pink", fg="black", command=add)
        self.add_button.place(x=30, y=200)

        self.delete_button = Button(self.root, text="Delete", font="sarif, 20 bold italic",
                                    width=10, bd=5, bg="pink", fg="black", command=delete)
        self.delete_button.place(x=30, y=280)

        self.complete_button = Button(self.root, text="Complete", font="sarif, 20 bold italic",
                                      width=10, bd=5, bg="pink", fg="black", command=complete)
        self.complete_button.place(x=30, y=360)

        self.complete_button = Button(self.root, text="Incomplete", font="sarif, 20 bold italic",
                                      width=10, bd=5, bg="pink", fg="black", command=incomplete)
        self.complete_button.place(x=30, y=440)

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
