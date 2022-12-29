import tkinter as tk

from results_window import ResultsWindow


class CompWindow:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Comparision')

        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)
        frame3 = tk.Frame(self.root)
        frame4 = tk.Frame(self.root)
        frame5 = tk.Frame(self.root)

        self.label = tk.Label(self.root, text='Comparing... 1/40',font=("Arial", 25))
        self.label.pack(side = tk.TOP)

        self.category = tk.Label(self.root, text='category name', font=("Arial", 20))
        self.category.pack(side=tk.TOP)


        self.job1 = tk.Label(frame1, text='job1 name / job2 name = ', font=("Arial", 15))
        self.job1.pack()

        self.spin_box = tk.Spinbox(frame2,from_=0,to=50,values=["1/9","1/8","1/7","1/6","1/5","1/4","1/3","1/2","1","2","3","4","5","6","7","8","9"],wrap=True)
        self.spin_box.pack()

        self.next_button = tk.Button(frame3, text="Next", command=self._next_comparision,bg="#ccffff")
        self.next_button.pack(ipadx=30,ipady=15,side =tk.BOTTOM)

        self.done_button = tk.Button(frame4, text="Done", command=self._open_results_gui, bg="#ccffff")
        self.done_button.pack(ipadx=30, ipady=15, side=tk.BOTTOM)

        frame1.pack(side =tk.LEFT)
        frame2.pack(side=tk.LEFT)
        frame3.pack(side=tk.LEFT)
        frame4.pack(side=tk.LEFT)
        frame5.pack(side=tk.LEFT)
        self.root.mainloop()


    def _next_comparision(self):
        pass

    def _open_results_gui(self):
        self.root.destroy()
        gui = ResultsWindow()

