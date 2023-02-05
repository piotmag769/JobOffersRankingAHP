import tkinter as tk
import numpy as np

from consistency_gui import ConsistencyGui
from ranking import RankingCalculator


class ResultsGui:
    def __init__(self, ranking_calculator: RankingCalculator, alternatives_names, features_names):
        self.ranking_calculator = ranking_calculator
        self.alternatives_names = alternatives_names
        self.features_names = features_names

        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Results')

        self.label = tk.Label(self.root, text='Results:', font=("Arial", 25))
        self.label.pack(side=tk.TOP)

        self.listbox = tk.Listbox(height=10,
                                  width=15,
                                  activestyle='dotbox',
                                  font="Helvetica",
                                  fg="blue")
        self.listbox.pack()

        self.next_button = tk.Button(
            text="Show consistency ratios", command=self._show_consistency_ratios, bg="#ccffff")
        self.next_button.pack(ipadx=30, ipady=15, side=tk.BOTTOM)

        self.ranking, self.C_1_2_consistency_ratio, self.C_array_consistency_ratio, self.C_array_consistency_ratios \
            = self.ranking_calculator.compute_ranking_and_consistency_ratios()

        self._make_ranking()

    def _make_ranking(self):
        nr_of_jobs = len(self.ranking)
        for i in range(nr_of_jobs):
            self.ranking[i] = np.append(self.ranking[i], i)
        self.ranking.sort(key=lambda y: y[0])

        for i in range(nr_of_jobs):
            self.listbox.insert("end", str(i+1) + ". " +
                                self.alternatives_names[int(self.ranking[i][1])])

    def _show_consistency_ratios(self):
        self.root.destroy()
        ConsistencyGui(self.C_1_2_consistency_ratio, self.C_array_consistency_ratio,
                       self.C_array_consistency_ratios, self.features_names).run()

    def run(self):
        self.root.mainloop()
