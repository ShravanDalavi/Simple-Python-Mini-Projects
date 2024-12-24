# Blood Bank Management System
This is a Python-based graphical application for managing blood bank data, designed using `tkinter` for the GUI and `matplotlib` for visualizing blood group availability. It allows users to add donor details, view donor lists, and monitor blood group inventory.

## Features
- Add Donors: Input donor details like name, blood group, age, and contact information.
- View Donor List: Display all donor details in a tabular format.
- Blood Group Availability Chart: Visualize the current inventory of blood groups with an interactive bar chart.
- Real-time Updates: Automatically update the inventory chart after adding donor information.

## Required Modules

- `tkinter`: For creating the graphical user interface.
- `matplotlib`: For plotting and displaying the inventory chart.
- `ttk` (part of `tkinter`): For enhanced GUI components.


## How to Install Required Modules
Ensure you have Python installed (version 3.6 or above). Install the required modules using the following commands:
```bash
pip install matplotlib
```

## How to Run the Script
1. Save the script as `BloodBank.py` or any other preferred name.
2. Open a terminal/command prompt and navigate to the folder where the script is saved.
3. Run the script using:
```bash
python BloodBank.py
```

## Example Usage
1. Add Donor:
Enter donor details (Name, Blood Group, Age, Contact) in the provided input fields.
Click the "Add Donor" button to save the information and update the inventory chart.
2. View Donors:
Click the "View Donors" button to open a new window displaying all registered donors in a tabular format.
3. Monitor Inventory:
Observe the bar chart displaying the availability of each blood group.

## Acknowledgments

- **Tkinter Documentation**: For GUI framework references.
- **Matplotlib Documentation**: For chart plotting and integration guidance.
- Special thanks to the Python community for continuous support and open-source resources.