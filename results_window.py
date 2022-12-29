import tkinter as tk


class ResultsWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Results')

        self.label = tk.Label(self.root, text='Results:', font=("Arial", 25))
        self.label.pack(side=tk.TOP)


        self.root.mainloop()
