import tkinter as tk

from ranking import RankingCalculator


class ResultsWindow:
    def __init__(self, ranking_calculator: RankingCalculator):
        self.ranking_calculator = ranking_calculator

        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Results')

        self.label = tk.Label(self.root, text='Results:', font=("Arial", 25))
        self.label.pack(side=tk.TOP)

        print(self.ranking_calculator.C_1_2.__repr__())
        print(self.ranking_calculator.C_array.__repr__())
        
        print(self.ranking_calculator.compute_ranking_and_consistency_ratios())

    def run(self):
        self.root.mainloop()
