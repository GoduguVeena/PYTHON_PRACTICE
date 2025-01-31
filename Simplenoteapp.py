import tkinter as tk
from tkinter import messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Note App")
        
        self.notes = []
        
        self.note_text = tk.Text(root, width=40, height=10)
        self.note_text.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Note", command=self.add_note)
        self.add_button.pack(pady=5)
        
        self.show_button = tk.Button(root, text="Show Notes", command=self.show_notes)
        self.show_button.pack(pady=5)
        
    def add_note(self):
        note = self.note_text.get("1.0", tk.END).strip()
        if note:
            self.notes.append(note)
            self.note_text.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Note added!")
        else:
            messagebox.showwarning("Warning", "Note cannot be empty.")
        
    def show_notes(self):
        if self.notes:
            notes_str = "\n\n".join(self.notes)
            messagebox.showinfo("Your Notes", notes_str)
        else:
            messagebox.showwarning("Warning", "No notes available.")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
