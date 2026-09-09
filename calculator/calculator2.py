import tkinter as tk
import math

# ---------- Core Logic ----------
expression = ""

def update_display(value):
    display_var.set(value)

def on_click(value):
    global expression

    if value == "C":
        expression = ""
        update_display("")

    elif value == "=":
        try:
            expr = expression.replace("π", str(math.pi)).replace("e", str(math.e))
            result = str(eval(expr))
            expression = result
            update_display(result)
        except:
            expression = ""
            update_display("Error")

    elif value == "⌫":
        expression = expression[:-1]
        update_display(expression)

    elif value == "√":
        try:
            expression = str(math.sqrt(float(expression)))
            update_display(expression)
        except:
            update_display("Error")
            expression = ""

    elif value in ["sin", "cos", "tan"]:
        try:
            num = float(expression)
            if value == "sin":
                expression = str(math.sin(math.radians(num)))
            elif value == "cos":
                expression = str(math.cos(math.radians(num)))
            else:
                expression = str(math.tan(math.radians(num)))
            update_display(expression)
        except:
            update_display("Error")
            expression = ""

    elif value == "log":
        try:
            expression = str(math.log10(float(expression)))
            update_display(expression)
        except:
            update_display("Error")
            expression = ""

    else:
        expression += value
        update_display(expression)


# ---------- UI Setup ----------
root = tk.Tk()
root.title("Modern Scientific Calculator")
root.geometry("420x520")
root.configure(bg="#1e1e2f")

display_var = tk.StringVar()

# ---------- Display ----------
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Consolas", 20),
    bg="#2d2d44",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
display.pack(fill="both", padx=10, pady=10, ipady=15)


# ---------- Layout Frames ----------
main_frame = tk.Frame(root, bg="#1e1e2f")
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame, bg="#1e1e2f")
left_frame.pack(side="left", expand=True, fill="both")

right_frame = tk.Frame(main_frame, bg="#25253a", width=100)
right_frame.pack(side="right", fill="y")


# ---------- Button Style ----------
def create_button(parent, text, bg="#3a3a5a"):
    btn = tk.Button(
        parent,
        text=text,
        font=("Arial", 12, "bold"),
        bg=bg,
        fg="white",
        bd=0,
        activebackground="#50507a",
        activeforeground="white",
        relief="flat",
        command=lambda: on_click(text)
    )
    return btn


# ---------- Number Pad ----------
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for row in buttons:
    row_frame = tk.Frame(left_frame, bg="#1e1e2f")
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        b = create_button(row_frame, btn)
        b.pack(side="left", expand=True, fill="both", padx=4, pady=4)


# ---------- Side Scientific Panel ----------
scientific_buttons = ["sin", "cos", "tan", "log", "√", "π", "e", "C", "⌫"]

for btn in scientific_buttons:
    b = create_button(right_frame, btn, bg="#44446a")
    b.pack(fill="x", padx=5, pady=5, ipady=8)


# ---------- Keyboard Support ----------
def key_input(event):
    key = event.char

    if key in "0123456789+-*/.":
        on_click(key)
    elif event.keysym == "Return":
        on_click("=")
    elif event.keysym == "BackSpace":
        on_click("⌫")

root.bind("<Key>", key_input)

# ---------- Run ----------
root.mainloop()