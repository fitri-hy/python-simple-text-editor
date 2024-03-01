import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Example Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Example Text Editor - {filepath}")

def search_text():
    txt_edit.tag_remove("found", 1.0, tk.END)

    search_term = txt_search_entry.get()
    start_index = "1.0"
    while True:
        index = txt_edit.search(search_term, start_index, stopindex=tk.END)
        if not index:
            break
        txt_edit.tag_add("found", index, f"{index}+{len(search_term)}c")
        txt_edit.tag_config("found", background="yellow")
        start_index = f"{index}+{len(search_term)}c"

window = tk.Tk()
window.title("Example Text Editor")

frame_text_editor = tk.Frame(window, padx=10)
frame_text_editor.pack(fill=tk.BOTH, expand=True)

txt_edit = tk.Text(frame_text_editor, padx=5, pady=5)
txt_edit.pack(fill=tk.BOTH, expand=True)

frame_search = tk.Frame(window, padx=15, pady=5)
frame_search.pack(fill=tk.X)

txt_search_entry = tk.Entry(frame_search)
txt_search_entry.pack(fill=tk.X, expand=True, side=tk.LEFT)

btn_search = tk.Button(frame_search, text="Search", command=search_text)
btn_search.pack(fill=tk.X, side=tk.LEFT)

frame_buttons = tk.Frame(window)
frame_buttons.pack()

btn_open = tk.Button(frame_buttons, text="Open", command=open_file)
btn_open.pack(side=tk.LEFT, padx=5, pady=5)

btn_save = tk.Button(frame_buttons, text="Save", command=save_file)
btn_save.pack(side=tk.LEFT, padx=5, pady=5)

window.mainloop()
