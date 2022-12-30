import numpy as np
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from categories_comparision_gui import CategoriesComparisionGui
from ranking import RankingCalculator


class AddingAlternativesGui:
    def __init__(self, features_names):
        self.features_names = features_names

        self.alternatives_names = []

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
            frame2, text="Done", command=self._open_categories_comparision_window, bg="#ccffff")
        self.done_button.pack(ipadx=100, ipady=15)

        frame1.pack(side=tk.LEFT)
        frame2.pack(side=tk.RIGHT)

    def _open_categories_comparision_window(self):
        alternatives_count = len(self.alternatives_names)
        features_count = len(self.features_names)

        ranking_calculator = RankingCalculator(
            alternatives_count, features_count)

        self.root.destroy()

        CategoriesComparisionGui(ranking_calculator, self.alternatives_names,
                         self.features_names).run()

    def _add_job(self):
        new_job_name = self.job_name.get(1.0, "end-1c")
        self.jobs_list.insert(tk.INSERT, new_job_name + "\n")
        self.alternatives_names.append(new_job_name)

    def run(self):
        self.root.mainloop()
