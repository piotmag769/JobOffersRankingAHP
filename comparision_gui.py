import tkinter as tk

from results_gui import ResultsWindow


class ComparisionWindow:
    def __init__(self, ranking_calculator: RankingCalculator, jobs_names):
        self.ranking_calculator = ranking_calculator
        self.jobs_names = jobs_names

        self.first_job_index = 0
        self.second_job_index = 1

        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Comparision')

        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)
        frame3 = tk.Frame(self.root)
        frame4 = tk.Frame(self.root)
        frame5 = tk.Frame(self.root)

        self.label = tk.Label(
            self.root, text='Comparing...', font=("Arial", 25))
        self.label.pack(side=tk.TOP)

        self.category = tk.Label(
            self.root, text='category name', font=("Arial", 20))
        self.category.pack(side=tk.TOP)

        self.job1 = tk.Label(
            frame1, text=self.jobs_names[self.first_job_index] +
            ' / ' + self.jobs_names[self.second_job_index] + ' = ', font=("Arial", 15))
        self.job1.pack()

        self.spin_box = tk.Spinbox(frame2, from_=0, to=50, values=[
                                   "1/9", "1/8", "1/7", "1/6", "1/5", "1/4", "1/3", "1/2", "1", "2", "3", "4", "5", "6", "7", "8", "9"], wrap=True)
        self.spin_box.pack()

        self.next_button = tk.Button(
            frame3, text="Next", command=self._next_comparision, bg="#ccffff")
        self.next_button.pack(ipadx=30, ipady=15, side=tk.BOTTOM)

        self.done_button = tk.Button(
            frame4, text="Done", command=self._open_results_gui, bg="#ccffff")
        self.done_button.pack(ipadx=30, ipady=15, side=tk.BOTTOM)

        frame1.pack(side=tk.LEFT)
        frame2.pack(side=tk.LEFT)
        frame3.pack(side=tk.LEFT)
        frame4.pack(side=tk.LEFT)
        frame5.pack(side=tk.LEFT)
        self.root.mainloop()


    def _next_comparision(self):

        self.second_job_index += 1
        if self.second_job_index == len(self.jobs_names):
            self.first_job_index += 1
            self.second_job_index = self.first_job_index + 1

        if self.first_job_index == len(self.jobs_names) - 1:
            self._open_results_gui()
            return

        self.job1.config(text=self.jobs_names[self.first_job_index] +
                         ' / ' + self.jobs_names[self.second_job_index] + ' = ')

    def _open_results_gui(self):
        self.root.destroy()
        ResultsWindow(self.ranking_calculator)

    def mainloop(self):
        self.root.mainloop()
