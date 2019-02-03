import sqlite3
import tkinter as tk
import threading


def loadset(ordbog):
    db = sqlite3.connect(ordbog)
    qwery = db.execute('select word_ from lookup1')
    memoydict = [word[0] for word in qwery.fetchall()]
    return memoydict


def lookup():
    text = entry.get()
    global memorydict
    if len(text) > 2:
        maches = [word for word in memorydict if word.startswith(text)]
        maches = enumerate(maches)
        listbox.delete(0, 'end')
        for index, match in maches:
            listbox.insert(index, match)
    else:
        pass


def deleteall(e):
    entry.delete(0, 'end')


def startthread(e):
    t = threading.Thread(target=lookup)
    t.start()


memorydict = loadset('ordbog')
if __name__ == '__main__':
    mainwindow = tk.Tk()
    mainwindow.title('Autocomplete')
    mainwindow.geometry('212x230')
    entry = tk.Entry(mainwindow)
    entry.place(x=10, y=10)
    listbox = tk.Listbox(mainwindow, width=21, height=10)
    listbox.place(x=11, y=50)
    listbox.insert(0, 'Her kommer resultaterne')

    entry.bind("<KeyRelease>", startthread)
    entry.bind('<Mod1-BackSpace>', deleteall)
    mainwindow.minsize(212, 230)
    mainwindow.maxsize(212, 230)
    menubar = tk.Menu(mainwindow)
    pageMenu = tk.Menu(menubar)
    pageMenu.add_command(label="hej")
    menubar.add_cascade(label="hej", menu=pageMenu)
    mainwindow.config(menu=menubar)
    mainwindow.mainloop()
