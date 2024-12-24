import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample data structure to store blood bank data
blood_data = {
    'A+': 10,
    'A-': 5,
    'B+': 8,
    'B-': 3,
    'O+': 15,
    'O-': 2,
    'AB+': 6,
    'AB-': 1
}

donors = []

# Add donor information
def add_donor():
    name = name_entry.get()
    blood_group = blood_group_combobox.get()
    age = age_entry.get()
    contact = contact_entry.get()

    if not (name and blood_group and age and contact):
        messagebox.showerror("Input Error", "Please fill all fields!")
        return

    donors.append({
        'Name': name,
        'Blood Group': blood_group,
        'Age': age,
        'Contact': contact
    })

    blood_data[blood_group] += 1
    update_chart()
    messagebox.showinfo("Success", "Donor added successfully!")
    clear_fields()

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    blood_group_combobox.set('')

# Display donors
def view_donors():
    donor_window = tk.Toplevel(root)
    donor_window.title("Donor Details")

    tree = ttk.Treeview(donor_window, columns=("Name", "Blood Group", "Age", "Contact"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Blood Group", text="Blood Group")
    tree.heading("Age", text="Age")
    tree.heading("Contact", text="Contact")
    tree.pack(fill=tk.BOTH, expand=True)

    for donor in donors:
        tree.insert("", tk.END, values=(donor['Name'], donor['Blood Group'], donor['Age'], donor['Contact']))

# Update chart
def update_chart():
    blood_groups = list(blood_data.keys())
    quantities = list(blood_data.values())

    ax.clear()
    bars = ax.bar(blood_groups, quantities, color=['#FF9999', '#FFCC99', '#99CCFF', '#CCFF99', '#FF6666', '#6666FF', '#66FF66', '#FFFF66'])
    ax.set_title("Blood Group Availability", fontsize=14, fontweight='bold')
    ax.set_xlabel("Blood Groups", fontsize=12, fontweight='bold')
    ax.set_ylabel("Units Available", fontsize=12, fontweight='bold')
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)

    for bar, qty in zip(bars, quantities):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 1, str(qty), 
                ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

    canvas.draw()

# Main application window
root = tk.Tk()
root.title("Blood Bank Management System")
root.geometry("900x650")
root.configure(bg='#F0F0F0')

# Input fields
frame = tk.Frame(root, bg='#F0F0F0')
frame.pack(pady=20)

tk.Label(frame, text="Name:", font=("Arial", 12, "bold"), bg='#F0F0F0').grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Blood Group:", font=("Arial", 12, "bold"), bg='#F0F0F0').grid(row=1, column=0, padx=10, pady=10)
blood_group_combobox = ttk.Combobox(frame, values=list(blood_data.keys()), font=("Arial", 12))
blood_group_combobox.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame, text="Age:", font=("Arial", 12, "bold"), bg='#F0F0F0').grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(frame, font=("Arial", 12))
age_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(frame, text="Contact:", font=("Arial", 12, "bold"), bg='#F0F0F0').grid(row=3, column=0, padx=10, pady=10)
contact_entry = tk.Entry(frame, font=("Arial", 12))
contact_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
tk.Button(frame, text="Add Donor", command=add_donor, font=("Arial", 12, "bold"), bg='#66CC66', fg='white').grid(row=4, column=0, padx=10, pady=20)
tk.Button(frame, text="View Donors", command=view_donors, font=("Arial", 12, "bold"), bg='#6699CC', fg='white').grid(row=4, column=1, padx=10, pady=20)

# Matplotlib chart
fig, ax = plt.subplots(figsize=(6, 5))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(pady=20)

update_chart()

root.mainloop()