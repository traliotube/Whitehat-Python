import tkinter as tk

root = tk.Tk()
root.configure(bg="#F6091E")

canvas = tk.Canvas(root, width=450, height=250)
canvas.create_image(0, 0, anchor=tk.NW)
canvas.create_rectangle(0, 0, 450, 45, fill="#F6091E")


label_heading = canvas.create_text(225, 20, font=(
    'Corier', '24', 'bold'), text="Driving License", fill="white")
label_id_tag = canvas.create_text(
    25, 60, font=('Times', '14', 'bold'), text="ID :")
label_name_tag = canvas.create_text(
    30, 100, font=('Times', '12', 'bold'), text="Name :")
label_dob_tag = canvas.create_text(52, 120, font=(
    'Times', '12', 'bold'), text="Date of birth :")
label_pin_tag = canvas.create_text(
    32, 140, font=('Times', '12', 'bold'), text="Pin no. :")
label_address_tag = canvas.create_text(
    36, 160, font=('Times', '12', 'bold'), text="Address :")
label_vehicle_type_tag = canvas.create_text(155, 180, font=(
    'Times', '12', 'bold'), text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
label_id = tk.Label()
label_name = tk.Label()
label_dob = tk.Label()
label_pin = tk.Label()
label_address = tk.Label()
label_vehicle_type = tk.Label()


# Define the function
def assignData():
    id = 9547863210
    print(id)
    name = "Batman"
    print(name)
    dob = "17 April 1915"
    print(dob)
    pincode = 321456
    print(type(pincode))
    address = "72 Faxcol Dr Gotham City, NJ 321456"
    print(type(address))
    vehiclesAllowed = ["Four Wheeler", "Two Wheeler"]
    print(type(vehiclesAllowed))

    # Assign the data to the labels
    label_id["text"] = id
    label_name["text"] = name
    label_dob["text"] = dob
    label_pin["text"] = pincode
    label_address["text"] = address
    label_vehicle_type["text"] = vehiclesAllowed


# Create a button
button1 = tk.Button(root, text="Show Data", command=assignData)

button1.configure(width=20, activebackground="#9EC6EE", relief=tk.FLAT)
button1_window = canvas.create_window(
    200, 235, anchor=tk.CENTER, window=button1)
label_id_window = canvas.create_window(
    80, 60, anchor=tk.CENTER, window=label_id)
label_name_window = canvas.create_window(
    100, 100, anchor=tk.CENTER, window=label_name)
label_dob_window = canvas.create_window(
    140, 120, anchor=tk.CENTER, window=label_dob)
label_pin_window = canvas.create_window(
    85, 140, anchor=tk.CENTER, window=label_pin)
label_address_window = canvas.create_window(
    130, 160, anchor=tk.CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(
    335, 180, anchor=tk.CENTER, window=label_vehicle_type)

canvas.pack()
button1.pack()
root.mainloop()
