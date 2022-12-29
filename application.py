from job_adding_gui import JobAddingWindow
from ranking import RankingCalculator


class Application:
    def __init__(self):
        self.ranking_calculator = RankingCalculator()

        self.job_adding_window = JobAddingWindow(self.ranking_calculator)

    def run(self):
        self.job_adding_window.mainloop()
        print('essa')
        self.comparition_widnow.mainloop()
        self.results_window.mainloop()
