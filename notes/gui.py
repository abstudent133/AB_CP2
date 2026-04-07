#GUI with Tkinter Notes
import tkinter as tk


root = tk.Tk()

root.title("Testing")
root.configure(background="pink")
root.minsize(250, 250)
root.maxsize(1000, 1000)
root.geometry("300x300+100+100")
label = tk.Label(root, text="This is currently working.", font=("Times New Roman",14,"bold"))
label.config(fg="magenta", background="pink")
#stuff about button
root.count = 0
def add():
    root.count += 1
    tk.Label(root, text=root.count)
    num["text"]=root.count

btn = tk.Button(root, text="ADD",command=add)
btn.pack()
num = tk.Label(root,text="0")
num.pack()
label.pack()
#image = tk.PhotoImage(file="img\\letter.png")
#tk.Label(root, image=image).pack()

root.mainloop()