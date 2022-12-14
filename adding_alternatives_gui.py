import tkinter as tk
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText


from categories_comparision_gui import CategoriesComparisionGui
from ranking import RankingCalculator


class AddingAlternativesGui:
    def __init__(self):
        self.features_names = []

        self.alternatives_names = []

        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Job offers')

        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)
        frame3 = tk.Frame(self.root)

        self.label = tk.Label(frame2, text='Jobs list:', font=("Arial", 25))
        self.label.pack()

        self.jobs_list = ScrolledText(frame2, width=30, height=18)
        self.jobs_list.pack()

        self.label2 = tk.Label(frame3, text='Categories list:', font=("Arial", 25))
        self.label2.pack()

        self.features_list = ScrolledText(frame3, width=30, height=18)
        self.features_list.pack()

        self.job_name = tk.Text(frame1, height=3, width=15, font=("Arial", 12))
        self.job_name.pack()
        self.add_job_button = tk.Button(
            frame1, text="Add job", command=self._add_job, bg="#ccffff")
        self.add_job_button.pack(ipadx=15, ipady=15)

        self.category_name = tk.Text(frame1, height=3, width=15, font=("Arial", 12))
        self.category_name.pack()
        self.add_category_button = tk.Button(
            frame1, text="Add category", command=self._add_category, bg="#ccffff")
        self.add_category_button.pack(ipadx=15, ipady=15)

        self.done_button = tk.Button(
            frame1, text="Done", command=self._open_categories_comparision_window, bg="#ccffff")
        self.done_button.pack(ipadx=15, ipady=15)

        frame1.pack(side=tk.LEFT)
        frame2.pack(side=tk.LEFT)
        frame3.pack(side=tk.LEFT)

    def _open_categories_comparision_window(self):
        alternatives_count = len(self.alternatives_names)
        features_count = len(self.features_names)

        if alternatives_count < 3:
            tk.messagebox.showinfo("Stop - wait a minute", "Hi :)) You need at least 3 job offers")
            return

        ranking_calculator = RankingCalculator(
            alternatives_count, features_count)

        self.root.destroy()

        CategoriesComparisionGui(ranking_calculator, self.alternatives_names,
                         self.features_names).run()

    def _add_job(self):
        new_job_name = self.job_name.get(1.0, "end-1c")
        self.jobs_list.insert(tk.INSERT, new_job_name + "\n")
        self.alternatives_names.append(new_job_name)

    def _add_category(self):
        new_category_name = self.category_name.get(1.0, "end-1c")
        self.features_list.insert(tk.INSERT, new_category_name + "\n")
        self.features_names.append(new_category_name)

    def run(self):
        self.root.mainloop()
