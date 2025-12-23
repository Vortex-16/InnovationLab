import customtkinter as ctk

# Appearance settings
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Button click function
def button_click(value):
    display.configure(state="normal")
    current = display.get()

    # Prevent multiple decimals in a single number
    if value == ".":
        last_number = current.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]
        if "." in last_number:
            display.configure(state="disabled")
            return

    display.insert("end", value)
    display.configure(state="disabled")


# Clear display
def clear_display():
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="disabled")

# Calculate result
def calculate():
    expression = display.get()
    try:
        result = eval(expression)

        # Fix floating-point precision
        if isinstance(result, float):
            result = round(result, 10)
            result = int(result) if result.is_integer() else result

        display.configure(state="normal")
        display.delete(0, "end")
        display.insert(0, str(result))
        display.configure(state="disabled")

    except:
        display.configure(state="normal")
        display.delete(0, "end")
        display.insert(0, "Error")
        display.configure(state="disabled")


# Window
app = ctk.CTk()
app.title("Clean Calculator")
app.geometry("380x520")
app.resizable(False, False)

# Display
display = ctk.CTkEntry(app, font=("Arial", 30), width=330, height=70,
                       corner_radius=15, justify="right", state="disabled")
display.pack(pady=20)

# Button frame
frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack()

# Buttons layout
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = ctk.CTkButton(frame, text=text, width=70, height=70,
                            corner_radius=20, font=("Arial", 25),
                            fg_color="#22c55e",  # Green color
                            hover_color="#16a34a",
                            command=calculate)
    else:
        btn = ctk.CTkButton(frame, text=text, width=70, height=70,
                            corner_radius=20, font=("Arial", 25),
                            command=lambda t=text: button_click(t))

    btn.grid(row=row, column=col, padx=8, pady=8)

# Clear button
clear_btn = ctk.CTkButton(app, text="CLEAR", width=320, height=70,
                          corner_radius=20, font=("Arial", 25),
                          fg_color="#ef4444",  # Red
                          hover_color="#dc2626",
                          command=clear_display)
clear_btn.pack(pady=10)

# Start app
app.mainloop()
