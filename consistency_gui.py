import tkinter as tk

class ConsistencyGui:
    def __init__(self, C_1_2_consistency_ratio, C_array_consistency_ratios):
        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Consistency ratio')

        self.C_1_2_consistency_ratio = C_1_2_consistency_ratio
        self.C_array_consistency_ratios = C_array_consistency_ratios

        self.C_1_2_consistency_label = tk.Label(text='C12_consistency_ratio = ' + str(self.C_1_2_consistency_ratio), font=("Arial", 25))
        self.C_1_2_consistency_label.pack()

        self.C_consistency_label = tk.Message(text='C_consistency_ratios:' + str(self.C_array_consistency_ratios),
                                                font=("Arial", 12))
        self.C_consistency_label.pack()

    def run(self):
        self.root.mainloop()
