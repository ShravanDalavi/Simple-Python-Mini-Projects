import tkinter as tk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES

# Create a mapping from language names to language codes
language_dict = {v: k for k, v in LANGUAGES.items()}

# Function to handle translation
def translate_text():
    translator = Translator()
    try:
        src_text = entry_text.get("1.0", tk.END).strip()
        src_lang = language_dict[src_lang_var.get()]
        dest_lang = language_dict[dest_lang_var.get()]

        if not src_text:
            messagebox.showerror("Error", "Please enter text to translate")
            return

        translation = translator.translate(src_text, src=src_lang, dest=dest_lang)
        entry_translation.delete("1.0", tk.END)
        entry_translation.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Creating main window
root = tk.Tk()
root.title("Translator")

# Source Text
label_text = tk.Label(root, text="Text to Translate")
label_text.pack(pady=5)
entry_text = tk.Text(root, height=10, width=50)
entry_text.pack(pady=5)

# Source Language
label_src_lang = tk.Label(root, text="Source Language")
label_src_lang.pack(pady=5)
src_lang_var = tk.StringVar(root)
src_lang_var.set("english")  # default value
src_lang_menu = tk.OptionMenu(root, src_lang_var, *language_dict.keys())
src_lang_menu.pack(pady=5)

# Destination Language
label_dest_lang = tk.Label(root, text="Destination Language")
label_dest_lang.pack(pady=5)
dest_lang_var = tk.StringVar(root)
dest_lang_var.set("marathi")  # default value for Marathi
dest_lang_menu = tk.OptionMenu(root, dest_lang_var, *language_dict.keys())
dest_lang_menu.pack(pady=5)

# Translation result
label_translation = tk.Label(root, text="Translated Text")
label_translation.pack(pady=5)
entry_translation = tk.Text(root, height=10, width=50)
entry_translation.pack(pady=5)

# Translate button
button_translate = tk.Button(root, text="Translate", command=translate_text)
button_translate.pack(pady=5)

root.mainloop()
