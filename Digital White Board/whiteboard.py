import tkinter as tk

# Default brush settings
brush_color = 'black'
brush_size = 2

# Function to handle drawing on the canvas
def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

# Function to clear the canvas
def clear_canvas():
    canvas.delete('all')

# Function to set the brush color
def set_brush_color(new_color):
    global brush_color
    brush_color = new_color

# Function to set the brush size
def set_brush_size(new_size):
    global brush_size
    brush_size = new_size

# Creating main window
root = tk.Tk()
root.title("Digital Whiteboard")

# Creating the canvas
canvas = tk.Canvas(root, bg='white', width=800, height=600)
canvas.pack()

# Bind the paint function to mouse events
canvas.bind("<B1-Motion>", paint)

# Frame for the color buttons
color_frame = tk.Frame(root)
color_frame.pack(pady=5)

# Color buttons
colors = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'brown', 'orange']
for color in colors:
    button = tk.Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: set_brush_color(c))
    button.pack(side='left', padx=2)

# Brush size buttons
size_frame = tk.Frame(root)
size_frame.pack(pady=5)

sizes = [2, 5, 8, 11]
for size in sizes:
    button = tk.Button(size_frame, text=str(size), command=lambda s=size: set_brush_size(s))
    button.pack(side='left', padx=2)

# Clear button
button_clear = tk.Button(root, text="Clear", command=clear_canvas)
button_clear.pack(pady=5)

root.mainloop()
