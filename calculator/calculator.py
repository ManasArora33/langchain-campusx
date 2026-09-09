import tkinter as tk
import math

# ---------- Core Logic ----------
def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            expr = expression.replace("π", str(math.pi)).replace("e", str(math.e))
            result = str(eval(expr))
            display_var.set(result)
            expression = result
        except:
            display_var.set("Error")
            expression = ""

    elif text == "C":
        expression = ""
        display_var.set("")

    elif text == "√":
        try:
            result = str(math.sqrt(float(expression)))
            display_var.set(result)
            expression = result
        except:
            display_var.set("Error")
            expression = ""

    elif text in ["sin", "cos", "tan"]:
        try:
            value = float(expression)
            if text == "sin":
                result = str(math.sin(math.radians(value)))
            elif text == "cos":
                result = str(math.cos(math.radians(value)))
            else:
                result = str(math.tan(math.radians(value)))

            display_var.set(result)
            expression = result
        except:
            display_var.set("Error")
            expression = ""

    elif text == "log":
        try:
            # result = str(math.log(float(expression)))
            result = str(math.log10(float(expression)))
            display_var.set(result)
            expression = result
        except:
            display_var.set("Error")
            expression = ""

    else:
        expression += text
        display_var.set(expression)


# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x500")

expression = ""
display_var = tk.StringVar()

# Display
display = tk.Entry(root, textvar=display_var, font="Arial 18", bd=10, relief=tk.RIDGE, justify="right")
display.pack(fill="both", ipadx=8, pady=10, padx=10)

# Buttons Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["sin", "cos", "tan", "√"],
    ["log", "π", "e", "C"]
]

# Create Buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 14", height=2)
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

# Run App
root.mainloop()