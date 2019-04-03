import subprocess
from tkinter import *
from functools import partial


class SearchGUI:

    def __init__(self, improved_file_search):

        # Root definition
        self.root = Tk()
        self.root.title("File Search")
        self.root.geometry("500x500")

        self.file_search_ob = improved_file_search

        # Search bar definition
        self.entry = Entry(self.root, font="Helvetica 14", width=30)
        self.entry.pack()
        self.entry.bind("<Return>", self.on_keyrelease)

        self.button_list = []

        self.root.mainloop()

    def on_keyrelease(self, event):
        search_term = event.widget.get().lower()
        self.file_search_ob.search(search_term)
        self.update_buttons()

    def update_buttons(self):
        for button in self.button_list:
            button.destroy()
        self.button_list.clear()

        if len(self.file_search_ob.files_matching_search) == 0:
            no_results = Button(self.root, text="No results found", state=DISABLED, width=35, font="Helvetica 14")
            self.button_list.append(no_results)

        for name, path in self.file_search_ob.files_matching_search.items():
            button = Button(self.root, text=name, font="Helvetica 14", width=35, command=partial(open_file, name, path))
            self.button_list.append(button)
        for button in self.button_list:
            button.pack(side=TOP)


def open_file(name, path):
    subprocess.call(path + "\\" + name, shell=True)
