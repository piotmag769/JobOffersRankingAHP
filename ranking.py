import numpy as np


class RankingCalculator:
    RI_n_9 = [0, 0, 0, 0.546, 0.83, 1.08, 1.26, 1.33, 1.41, 1.45, 1.47]

    def __init__(self, alternatives_count, features_count, experts_count=1):
        self.C_array = None
        self.C_1_2 = np.ones((features_count, features_count), float)
        self.C_arrays_per_expert = np.ones(
            (experts_count, features_count, alternatives_count, alternatives_count), float)

    def _calculate_C_array(self):
        self.C_array = np.prod(a=self.C_arrays_per_expert,
                               axis=0) ** (1.0 / self.C_arrays_per_expert.shape[0])

    @staticmethod
    def _priority_vector(matrix: np.ndarray):
        # work bcs of broadcasting in numpy
        normalized_matrix = matrix / np.sum(matrix, axis=0)
        return np.sum(normalized_matrix, axis=1) / normalized_matrix.shape[0]

    # w_array[j] = w_j
    # number of features to compare = len(w_array) = len(w_1_2)
    # number of altrenatives (job offers) = len(w_j)
    @staticmethod
    def _merge_priorities(w_array: np.ndarray, w_1_2: np.ndarray):
        features = w_1_2.shape[0]
        alternatives = w_array.shape[1]
        return [sum(w_1_2[feature] * w_array[feature][alternative]
                    for feature in range(features))
                for alternative in range(alternatives)]

    @staticmethod
    def _sattys_consistency_index(matrix: np.ndarray):
        priority_vector = RankingCalculator._priority_vector(matrix)
        largest_eigenvalue = (np.sum(matrix, axis=0) @
                              priority_vector.reshape(-1, 1))[0]
        n = matrix.shape[0]
        return (largest_eigenvalue - n) / (n - 1)

    @staticmethod
    def _consistency_ratio(matrix: np.ndarray):
        return RankingCalculator._sattys_consistency_index(matrix) / RankingCalculator.RI_n_9[matrix.shape[0]]

    def compute_ranking_and_consistency_ratios(self):
        self._calculate_C_array()

        w_1_2 = RankingCalculator._priority_vector(self.C_1_2)

        w_array = np.array([RankingCalculator._priority_vector(
            C_x) for C_x in self.C_array])

        ranking = RankingCalculator._merge_priorities(w_array, w_1_2)

        C_1_2_consistency_ratio = RankingCalculator._consistency_ratio(
            self.C_1_2)

        C_array_consistency_ratios = [RankingCalculator._consistency_ratio(C_x) for C_x in self.C_array]

        C_arrays_per_expert_consistency_ratios = [[RankingCalculator._consistency_ratio(
            expert_feature_rating) for expert_feature_rating in expert_C_array] for expert_C_array in self.C_arrays_per_expert]

        return ranking, C_1_2_consistency_ratio, C_array_consistency_ratios, C_arrays_per_expert_consistency_ratios
