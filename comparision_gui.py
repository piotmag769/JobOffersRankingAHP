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

        self.points = tk.Label(frame1, text='points:', font=("Arial", 15))
        self.points.pack()

        self.job1 = tk.Label(frame2, text='job1 name', font=("Arial", 15))
        self.job1.pack()

        self.job2 = tk.Label(frame3, text='job2 name', font=("Arial", 15))
        self.job2.pack()

        self.job1_points= tk.Text(frame2, height=3, width=5,font=("Arial", 12))
        self.job1_points.pack()

        self.job2_points = tk.Text(frame3, height=3, width=5, font=("Arial", 12))
        self.job2_points.pack()

        self.next_button = tk.Button(frame4, text="Next", command=self._next_comparision,bg="#ccffff")
        self.next_button.pack(ipadx=30,ipady=15,side =tk.BOTTOM)

        self.done_button = tk.Button(frame5, text="Done", command=self._open_results_gui, bg="#ccffff")
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

