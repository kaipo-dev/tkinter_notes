import tkinter as tk
import json
import os
from datetime import datetime

class Note():
    def __init__(self, ID, title = '', contents = '', date_created = '', date_modified = ''):
        timedate = Note.get_current_datetime()
        self.ID = ID
        self.title = title
        self.contents = contents
        self.date_created = timedate if date_created == '' else date_created
        self.date_modified = timedate if date_modified == '' else date_modified

        self.show_note()
    
    def retrieve_title(self):
        return self.title
    
    def retrieve_contents(self):
        return self.contents
    
    def change_title(self, title):
        self.title = title

    def save_note(self, title, contents, current_datetime):
        self.title = title
        self.contents = contents
        self.date_modified = current_datetime

        self.save_json(str(self.ID) + " - " + self.title)

    def load_note(self, filename):
        note_dict = Note.load_json(filename)
        self.ID = note_dict['id']
        self.title = note_dict['title']
        self.contents = note_dict['contents']
        self.date_created = note_dict['date_created']
        self.date_modified = note_dict['date_modified']

        self.show_note()

    # Serialising and saving the note object to a json file
    def note_to_dict(self):
        return {
            'id' : self.ID,
            'title' : self.title,
            'contents' : self.contents,
            'date_created' : self.date_created,
            'date_modified' : self.date_modified
        }
    
    def save_json(self, filename):
        path = f"notes\\{filename}.json"
        path = os.path.join(os.path.dirname(__file__), path)
        note_dict = self.note_to_dict() # Needs () after the method call to call it, if without returns as an object and cant be serialised
        with open(path, 'w') as file:
            json.dump(note_dict, file)

    # Deserialising and loading the json file to a note object
    @classmethod
    def dict_to_note(cls, data):
        return cls(
            data['id'],
            data['title'],
            data['contents'],
            data['date_created'],
            data['date_modified']
        )
    
    @classmethod
    def load_json(cls, filename):
        path = f"notes\\{filename}" # filename contains .jason at end
        path = os.path.join(os.path.dirname(__file__), path)
        with open(path) as file:
            data = json.load(file)
        return cls.dict_to_note(data)

    # Need to figure out how to use the methods above to then reopen the notes as a window again #

    def show_note(self):
        self.window = tk.Tk()

        self.fr_buttons = tk.Frame(self.window)
        self.fr_editor = tk.Frame(self.window)

        self.btn_saveNote = tk.Button(self.fr_buttons, text="Save Note", command=lambda : self.save_note(self.noteTitle.get("1.0",'end-1c'), self.noteContents.get("1.0",'end-1c'), Note.get_current_datetime())) #Args: title, contents, current_datetime
        self.btn_saveNote.pack()

        self.noteTitle = tk.Text(self.fr_editor, height=1, wrap=tk.WORD)
        self.noteTitle.pack(side=tk.TOP, fill=tk.X)
        self.noteContents = tk.Text(self.fr_editor, wrap=tk.WORD)
        self.noteContents.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.noteTitle.insert(tk.END, self.title)
        self.noteContents.insert(tk.END, self.contents)

        self.fr_buttons.pack(side=tk.TOP, fill = tk.X)
        self.fr_editor.pack(side=tk.TOP, fill = tk.BOTH, expand=True)

        self.window.title(f'Note - ID: {self.ID}')
        self.window.geometry("540x660")
        self.window.mainloop()

    def get_current_datetime():
        now = datetime.now()
        current_dt = now.strftime("%d/%m/%Y %H:%M:%S")
        return current_dt