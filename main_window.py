import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from comparision_gui import CompWindow


class MainWindow:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Job offers')

        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)

        self.label = tk.Label(frame2, text='Jobs list:',font=("Arial", 25))
        self.label.pack()

        self.jobs_list = ScrolledText(frame2, width=30, height=18)
        self.jobs_list.pack()

        self.job_name= tk.Text(frame1, height=3, width=30,font=("Arial", 12))
        self.job_name.pack()
        self.add_job_button = tk.Button(frame1, text="Add job", command=self._add_job, bg="#ccffff")
        self.add_job_button.pack(ipadx=100, ipady=15)

        self.done_button = tk.Button(frame2, text="Done", command=self._open_comparision_gui,bg="#ccffff")
        self.done_button.pack(ipadx=100,ipady=15)

        frame1.pack(side = tk.LEFT)
        frame2.pack(side=tk.RIGHT)
        self.root.mainloop()

    def _open_comparision_gui(self):
        self.root.destroy()
        gui = CompWindow()

    def _add_job(self):
        self.jobs_list.insert(tk.INSERT,self.job_name.get(1.0, "end-1c") + "\n")





gui = MainWindow()