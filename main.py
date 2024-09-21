from tkinter import *

def draw_window():
    root = Tk()
    label  = Label(root, text='Hello world')
    label.pack()

    listbox = Listbox(root)
    listbox.pack()

    for i in ['one', 'two', 'three', 'four']:
        listbox.insert(END, i)

    root.mainloop()

if __name__ == '__main__':
    draw_window()