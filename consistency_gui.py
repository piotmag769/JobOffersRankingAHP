import tkinter as tk


class ConsistencyGui:
    def __init__(self, C_1_2_consistency_ratio, C_array_consistency_ratios, C_arrays_per_expert_consistency_ratios, features_names, root):
        self.root = root
        for ele in root.winfo_children():
            ele.destroy()
        self.root.title('Consistency ratio')

        self.C_1_2_consistency_ratio = C_1_2_consistency_ratio
        self.C_array_consistency_ratios = C_array_consistency_ratios
        self.C_arrays_per_expert_consistency_ratios = C_arrays_per_expert_consistency_ratios
        self.features_names = features_names

        self.title_label = tk.Label(text='Consistency ratios',
                                    font=("Arial", 25))
        self.title_label.pack()

        self.C_1_2_consistency_label = tk.Label(
            text='for categories comparision matrix: ' + str(self.C_1_2_consistency_ratio), font=("Arial", 12))
        self.C_1_2_consistency_label.pack()

        self.title_label_jobs = tk.Label(text='for jobs comparision matrices: ',
                                         font=("Arial", 12))
        self.title_label_jobs.pack()

        self.listbox = tk.Listbox(height=20,
                                  width=60,
                                  activestyle='dotbox',
                                  font=("Arial", 12))
        self.listbox.pack()
        self._fill_listbox()

    def _fill_listbox(self):
        nr_of_experts = len(self.C_arrays_per_expert_consistency_ratios)
        nr_of_features = len(self.C_array_consistency_ratios)

        for i in range(nr_of_experts):
            for j in range(nr_of_features):
                self.listbox.insert("end", "expert " + str(i) + " in terms of " + self.features_names[j] + ": " +
                                    str(self.C_arrays_per_expert_consistency_ratios[i][j]))

        for i in range(nr_of_features):
            self.listbox.insert("end", "aggregated rating in terms of " + self.features_names[i] + ": " +
                                str(self.C_array_consistency_ratios[i]))

    def run(self):
        self.root.mainloop()
