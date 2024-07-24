import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech():
    try:
        text = entry_translation.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter text first")
            return
        
        language = language_dict[dest_lang_var.get()]
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("translated_text.mp3")
        os.system("start translated_text.mp3")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create a mapping from language names to language codes
language_dict = {
    'english': 'en', 
    'french': 'fr', 
    'spanish': 'es', 
    'german': 'de', 
    'chinese': 'zh', 
    'hindi': 'hi', 
    'japanese': 'ja', 
    'korean': 'ko', 
    'italian': 'it', 
    'portuguese': 'pt', 
    'russian': 'ru'
}

# Creating main window
root = tk.Tk()
root.title("Text-to-Speech")

# Text input
label_text = tk.Label(root, text="Text to Convert to Speech")
label_text.pack(pady=5)
entry_translation = tk.Text(root, height=10, width=50)
entry_translation.pack(pady=5)

# Destination Language
label_dest_lang = tk.Label(root, text="Language")
label_dest_lang.pack(pady=5)
dest_lang_var = tk.StringVar(root)
dest_lang_var.set("english")  # default value
dest_lang_menu = tk.OptionMenu(root, dest_lang_var, *language_dict.keys())
dest_lang_menu.pack(pady=5)

# Text-to-Speech button
button_tts = tk.Button(root, text="Text-to-Speech", command=text_to_speech)
button_tts.pack(pady=5)

root.mainloop()
