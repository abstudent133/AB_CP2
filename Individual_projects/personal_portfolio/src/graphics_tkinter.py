
import tkinter


class Menu:
    def __init__(self, options):
        self.options = options

    def use(self):
        root = tkinter.Tk()
        root.title('Personal Portfolio')
        root.configure(bg='pink')
        root.geometry('500x500')

        self.out = tkinter.StringVar()

        def push(name):
            self.out.set(name)
            root.destroy()

        # Title label
        title = tkinter.Label(
            root,
            text="Choose an Option",
            bg='pink',
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)

        # Button frame (keeps things centered)
        frame = tkinter.Frame(root, bg='pink')
        frame.pack(expand=True)

        for option in self.options:
            btn = tkinter.Button(
                frame,
                text=option,
                command=lambda v=option: push(v),
                width=20,
                height=2,
                font=("Arial", 12)
            )
            btn.pack(pady=10)

        root.mainloop()

        return self.out.get()
        

def inputs(question, wrong=False):
    while True:
        root = tkinter.Tk()
        root.title('Personal Portfolio')
        root.configure(bg='pink')
        root.geometry('500x400')

        out = tkinter.StringVar()

        # Main frame (centers everything)
        frame = tkinter.Frame(root, bg='pink')
        frame.pack(expand=True)

        # Question label
        q = tkinter.Label(
            frame,
            text=question,
            bg='pink',
            font=("Arial", 14)
        )
        q.pack(pady=10)

        # Error message
        if wrong:
            error = tkinter.Label(
                frame,
                text='Invalid input. Try again.',
                fg='red',
                bg='pink',
                font=("Arial", 10, "bold")
            )
            error.pack(pady=5)

        # Entry box
        enter = tkinter.Entry(
            frame,
            width=30,
            textvariable=out,
            font=("Arial", 12)
        )
        enter.pack(pady=10)

        # Button
        def end():
            root.destroy()

        button = tkinter.Button(
            frame,
            text='Enter',
            command=end,
            width=15,
            height=2,
            font=("Arial", 11)
        )
        button.pack(pady=15)

        root.mainloop()

        if out.get() != "":
            return out.get()

def show(stuff):
    root = tkinter.Tk()
    root.title('Personal Portfolio')
    root.configure(bg='pink')
    root.geometry('500x400')

    # Main frame to center content
    frame = tkinter.Frame(root, bg='pink')
    frame.pack(expand=True)

    # Message display
    message = tkinter.Message(
        frame,
        text=stuff,
        width=400,
        bg='pink',
        font=("Arial", 12)
    )
    message.pack(pady=20)

    # Button to close
    def end():
        root.destroy()

    button = tkinter.Button(
        frame,
        text='Continue',
        command=end,
        width=15,
        height=2,
        font=("Arial", 11)
    )
    button.pack(pady=20)

    root.mainloop()