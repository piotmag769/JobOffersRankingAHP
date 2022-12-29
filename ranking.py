import numpy as np


class RankingCalculator:
    RI_n_9 = [0, 0, 0, 0.546, 0.83, 1.08, 1.26, 1.33, 1.41, 1.45, 1.47]

    def __init__(self):
        self.C_array = None
        self.C_1_2 = None

    @staticmethod
    def _priority_vector(matrix):
        # work bcs of broadcasting in numpy
        normalized_matrix = matrix / np.sum(matrix, axis=0)
        return np.sum(normalized_matrix, axis=1) / len(normalized_matrix)

    # w_array[j] = w_j
    # number of features to compare = len(w_array) = len(w_1_2)
    # number of altrenatives (job offers) = len(w_j)
    @staticmethod
    def _merge_priorities(w_array, w_1_2):
        features = len(w_1_2)
        alternatives = len(w_array[0])
        return [sum(w_1_2[feature] * w_array[feature][alternative]
                    for feature in range(features))
                for alternative in range(alternatives)]

    @staticmethod
    def _sattys_consistency_index(matrix, priority_vector):
        largest_eigenvalue = np.sum(
            matrix, axis=0) @ np.array(priority_vector).reshape(-1, 1)
        n = len(matrix)
        return (largest_eigenvalue - n) / (n - 1)

    @staticmethod
    def _consistency_ratio(matrix, priority_vector):
        return RankingCalculator._sattys_consistency_index(matrix, priority_vector) / RankingCalculator.RI_n_9[len(matrix)]

    def compute_ranking_and_consistency_ratios(self):
        w_1_2 = RankingCalculator._priority_vector(self.C_1_2)

        w_array = [RankingCalculator._priority_vector(
            C_x) for C_x in self.C_array]

        ranking = RankingCalculator._merge_priorities(w_array, w_1_2)

        C_1_2_consistency_ratio = RankingCalculator._consistency_ratio(
            self.C_1_2, w_1_2)

        C_array_consistency_ratios = [RankingCalculator._consistency_ratio(
            C_x, w_x) for C_x, w_x in zip(self.C_array, w_array)]

        return ranking, C_1_2_consistency_ratio, C_array_consistency_ratios
