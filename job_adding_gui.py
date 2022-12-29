import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from comparision_gui import ComparisionWindow
from ranking import RankingCalculator


class JobAddingWindow:
    def __init__(self, ranking_calculator: RankingCalculator):
        self.ranking_calculator = ranking_calculator
        self.jobs_names = []

        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Job offers')

        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)

        self.label = tk.Label(frame2, text='Jobs list:', font=("Arial", 25))
        self.label.pack()

        self.jobs_list = ScrolledText(frame2, width=30, height=18)
        self.jobs_list.pack()

        self.job_name = tk.Text(frame1, height=3, width=30, font=("Arial", 12))
        self.job_name.pack()
        self.add_job_button = tk.Button(
            frame1, text="Add job", command=self._add_job, bg="#ccffff")
        self.add_job_button.pack(ipadx=100, ipady=15)

        self.done_button = tk.Button(
            frame2, text="Done", command=self._open_comparision_gui, bg="#ccffff")
        self.done_button.pack(ipadx=100, ipady=15)

        frame1.pack(side=tk.LEFT)
        frame2.pack(side=tk.RIGHT)

    def _open_comparision_gui(self):
        self.ranking_calculator.C_1_2 = [[] for _ in range(5)]
        self.ranking_calculator.C_array = [
            []for _ in range(len(self.jobs_names))]
        self.root.destroy()
        ComparisionWindow(self.ranking_calculator).mainloop()

    def _add_job(self):
        new_job_name = self.job_name.get(1.0, "end-1c")
        self.jobs_list.insert(tk.INSERT, new_job_name + "\n")
        self.jobs_names.append(new_job_name)

    def mainloop(self):
        self.root.mainloop()
