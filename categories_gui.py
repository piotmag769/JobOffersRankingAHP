import tkinter as tk

from comparision_gui import CompWindow

categories = ["salary", "qualifications", "travel_cost", "benefits", "development_opportunities"]
class CategoriesWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Comparision for categories')
        self.current_i = 0
        self.current_j = 1
        self.comparision_ctr = 1

        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)
        frame3 = tk.Frame(self.root)
        frame4 = tk.Frame(self.root)

        self.label = tk.Label(self.root, text="Comparing... 1/10",font=("Arial", 25))
        self.label.pack(side = tk.TOP)


        self.categories_names = tk.Label(frame1, text=self._generate_label(), font=("Arial", 15))
        self.categories_names.pack()

        self.spin_box = tk.Spinbox(frame2,from_=0,to=50,values=["1/9","1/8","1/7","1/6","1/5","1/4","1/3","1/2","1","2","3","4","5","6","7","8","9"],wrap=True)
        self.spin_box.pack()

        self.next_button = tk.Button(frame3, text="Next", command=self._next_comparision,bg="#ccffff")
        self.next_button.pack(ipadx=30,ipady=15,side =tk.BOTTOM)

        self.done_button = tk.Button(frame4, text="Done", command=self._open_results_gui, bg="#ccffff")
        self.done_button.pack(ipadx=30, ipady=15, side=tk.BOTTOM)

        frame1.pack(side =tk.LEFT)
        frame2.pack(side=tk.LEFT)
        frame3.pack(side=tk.LEFT)
        frame4.pack(side=tk.LEFT)
        self.root.mainloop()


    def _generate_label(self):
        return categories[self.current_i] + " / " + categories[self.current_j] + " = "

    def _next_comparision(self):
        if self.current_j == 4:
            self.current_i += 1
            self.current_j = self.current_i+1
        else:
            self.current_j += 1
        self.comparision_ctr += 1
        self.categories_names.config(text=self._generate_label(), font=("Arial", 15))
        self.label.config(text = "Comparing..." + str(self.comparision_ctr) + "/10")



    def _open_results_gui(self):
        self.root.destroy()
        gui = CompWindow()

