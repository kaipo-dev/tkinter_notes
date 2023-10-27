import tkinter as tk
from datetime import datetime
import glob
from note import Note

class Note_Manager():
    note_index = 0

    def __init__(self, acc_id):
        self.acc_id = acc_id
        self.current_note = None

        self.window = tk.Tk()
        self.fr_managerpage = tk.Frame(self.window)

        #widgets go below here
        self.btn_newNote = tk.Button(self.fr_managerpage, text="New Note", command=self.create_note)
        self.btn_newNote.pack(side=tk.TOP, fill=tk.X)

        # Lists all the files in the ./note directory, holding all the notes for now
        self.note_list = tk.Listbox(self.fr_managerpage, selectmode=tk.SINGLE, width=0, height=0)
        self.refresh_list()
        self.note_list.pack(side=tk.LEFT, anchor=tk.NW)

        self.btn_openNote = tk.Button(self.fr_managerpage, text="Open Note", command=lambda : self.open_note(self.note_list.get(self.note_list.curselection())))
        self.btn_openNote.pack(side=tk.BOTTOM)
        self.btn_refresh_list = tk.Button(self.fr_managerpage, text="Refresh", command=lambda : self.refresh_list())
        self.btn_refresh_list.pack(side=tk.BOTTOM)

        self.fr_managerpage.pack(fill=tk.BOTH, expand=True)
 
        self.window.title(f'Note Manager - ID: {self.acc_id}')
        self.window.geometry("540x660")
        self.window.mainloop()
        
    def create_note(self):
        self.current_note = Note(Note_Manager.note_index)
        Note_Manager.incriment_note()


    # './notes\\0 - T.json'
    def open_note(self, selected_file_path):
        self.current_note = Note.load_json(selected_file_path[8:])

    def refresh_list(self):
        note_pathnames = glob.glob("./notes/*.json")
        self.note_list.delete(0,tk.END)
        for i in range(0, len(note_pathnames)):
            self.note_list.insert(i+1, note_pathnames[i])

    @classmethod
    def incriment_note(cls):
        Note_Manager.note_index += 1

if __name__ == '__main__':
    nt_man = Note_Manager(0)