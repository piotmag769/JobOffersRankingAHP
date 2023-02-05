import tkinter as tk

from alternatives_comparision_gui import AlternativesComparisionGui
from ranking import RankingCalculator


class CategoriesComparisionGui:
    def __init__(self, ranking_calculator: RankingCalculator, alternatives_names, features_names, experts_names):
        self.ranking_calculator = ranking_calculator
        self.alternatives_names = alternatives_names
        self.features_names = features_names
        self.expert_names = experts_names
        self.comparision_in_total_str = str(sum(i for i in range(len(self.features_names))))

        self.first_index = 0
        self.second_index = 1
        self.comparision_counter = 1

        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Comparision for categories')

        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)
        frame3 = tk.Frame(self.root)

        self.label = tk.Label(
            self.root, text="Comparing... 1/" + self.comparision_in_total_str, font=("Arial", 25))
        self.label.pack(side=tk.TOP)

        self.features_label = tk.Label(
            frame1, text=self._generate_label(), font=("Arial", 15))
        self.features_label.pack()

        self.spin_box = tk.Spinbox(frame2, from_=0, to=50, values=[
                                   "1/9", "1/8", "1/7", "1/6", "1/5", "1/4", "1/3", "1/2", "1", "2", "3", "4", "5", "6", "7", "8", "9"], wrap=True)
        self.spin_box.pack()

        self.next_button = tk.Button(
            frame3, text="Next", command=self._next_comparision, bg="#ccffff")
        self.next_button.pack(ipadx=30, ipady=15, side=tk.BOTTOM)

        frame1.pack(side=tk.LEFT)
        frame2.pack(side=tk.LEFT)
        frame3.pack(side=tk.LEFT)

    def _generate_label(self):
        return self.features_names[self.first_index] + " / " + self.features_names[self.second_index] + " = "

    def _read_from_spin_box(self):
        text = self.spin_box.get()
        if '/' in text:
            numerator, denominator = text.split('/')
            return int(numerator) / int(denominator)

        return int(text)

    def _next_comparision(self):
        ratio = self._read_from_spin_box()

        self.ranking_calculator.C_1_2[self.first_index][self.second_index] = ratio
        self.ranking_calculator.C_1_2[self.second_index][self.first_index] = 1 / ratio

        self.second_index += 1
        if self.second_index == len(self.features_names):
            self.first_index += 1
            self.second_index = self.first_index + 1

        if self.first_index >= len(self.features_names) - 1:
            self._open_results_gui()
            return

        self.comparision_counter += 1

        self.features_label.config(text=self._generate_label())
        self.label.config(text="Comparing..." +
                          str(self.comparision_counter) + "/" + self.comparision_in_total_str)

    def _open_results_gui(self):
        self.root.destroy()
        AlternativesComparisionGui(self.ranking_calculator,
                                   self.alternatives_names, self.features_names, self.expert_names).run()

    def run(self):
        self.root.mainloop()
