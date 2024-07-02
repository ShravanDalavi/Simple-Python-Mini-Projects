import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(0, 0)

        self.equation = ""
        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="ridge", justify='right')
        self.display.pack(expand=True, fill="both", padx=10, pady=10)

        # Frame for buttons
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True, fill="both")

        # Button text layout
        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Create and place buttons
        buttons = []
        for text in button_texts:
            button = tk.Button(button_frame, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            buttons.append(button)

        clear_button = tk.Button(button_frame, text="C", font=("Arial", 18), command=self.clear_display, bg="red", fg="white")
        buttons.append(clear_button)

        # Layout buttons in a grid
        row = 0
        col = 0
        for button in buttons:
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Configure grid
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
            button_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.equation))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.equation = result
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.equation = ""
        else:
            self.equation += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.equation)

    def clear_display(self):
        self.equation = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
