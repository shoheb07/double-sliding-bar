import tkinter as tk

def update_min(val):
    min_val = min_scale.get()
    max_val = max_scale.get()
    if min_val > max_val:
        min_scale.set(max_val)
    min_label.config(text=f"Min: {min_scale.get()}")

def update_max(val):
    min_val = min_scale.get()
    max_val = max_scale.get()
    if max_val < min_val:
        max_scale.set(min_val)
    max_label.config(text=f"Max: {max_scale.get()}")

root = tk.Tk()
root.title("Double Range Slider")

tk.Label(root, text="Select Range", font=("Arial", 14)).pack(pady=10)

min_scale = tk.Scale(
    root, from_=0, to=100, orient="horizontal",
    command=update_min, length=300
)
min_scale.pack()

max_scale = tk.Scale(
    root, from_=0, to=100, orient="horizontal",
    command=update_max, length=300
)
max_scale.set(100)
max_scale.pack()

min_label = tk.Label(root, text="Min: 0")
min_label.pack()

max_label = tk.Label(root, text="Max: 100")
max_label.pack()

root.mainloop()
