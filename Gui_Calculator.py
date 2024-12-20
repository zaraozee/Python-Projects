import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def button_click(value):
    if value == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, ctk.END)
            entry.insert(ctk.END, str(result))
        except Exception:
            entry.delete(0, ctk.END)
            entry.insert(ctk.END, "Error")
    elif value == "C":
        entry.delete(0, ctk.END)
    else:
        entry.insert(ctk.END, value)

root = ctk.CTk()
root.title("GUI Calculator")
root.geometry("280x370")
root.resizable(False, False)

entry = ctk.CTkEntry(root, font=("Arial", 20), justify="right", width=250)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
]

for i, btn_text in enumerate(buttons):
    row = (i // 4) + 1
    col = i % 4
    button = ctk.CTkButton(root, text=btn_text, width=60, height=70, corner_radius=20,
                           font=("Arial", 18), command=lambda value=btn_text : button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
