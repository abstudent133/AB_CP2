root.count = 0
def add():
    root.count += 1
    tk.Label(root, text=root.count).pack()

btn = tk.Button(root, text="ADD",command=add)
btn.pack()