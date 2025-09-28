import tkinter as tk


root = tk.Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")


desc_label = tk.Label(root, text="This app multiplies two numbers.")
desc_label.pack()


num1_label = tk.Label(root, text="Enter first number:")
num1_label.pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

num2_label = tk.Label(root, text="Enter second number:")
num2_label.pack()
num2_entry = tk.Entry(root)
num2_entry.pack()


result_label = tk.Label(root, text="")
result_label.pack()


def multiply_numbers():
    num1 = num1_entry.get()
    num2 = num2_entry.get()
    try:
        product = float(num1) * float(num2)
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


calc_button = tk.Button(root, text="Calculate", command=multiply_numbers)
calc_button.pack()


root.mainloop()










#Taken help from chatGPT