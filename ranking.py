import numpy as np


def priority_vector(matrix):
    # work bcs of broadcasting in numpy
    normalized_matrix = matrix / np.sum(matrix, axis=0)
    return np.sum(normalized_matrix, axis=1) / len(normalized_matrix)


# w_array[j] = w_j
# number of features to compare = len(w_array) = len(w_1_2)
# number of altrenatives (job offers) = len(w_j)
def merge_priorities(w_array, w_1_2):
    features = len(w_1_2)
    alternatives = len(w_array[0])
    return [sum(w_1_2[feature] * w_array[feature][alternative]
                for feature in range(features))
            for alternative in range(alternatives)]


def sattys_consistency_index(matrix, priority_vector):
    largest_eigenvalue = np.sum(matrix, axis=0) @ np.array(priority_vector).reshape(-1, 1)
    n = len(matrix)
    return (largest_eigenvalue - n) / (n - 1)


def consistency_ratio(matrix, priority_vector, RI_n_q):
    return sattys_consistency_index(matrix, priority_vector) / RI_n_q[len(matrix)]


def compute_ranking_and_consistency_ratios(C_array, C_1_2, RI_n_q):
    w_1_2 = priority_vector(C_1_2)
    w_array = [priority_vector(C_x) for C_x in C_array]
    ranking = merge_priorities(w_array, w_1_2)
    C_1_2_consistency_ratio = consistency_ratio(C_1_2, w_1_2, RI_n_q)
    C_array_consistency_ratios = [consistency_ratio(C_x, w_x, RI_n_q) for C_x, w_x in zip(C_array, w_array)]
    return ranking, C_1_2_consistency_ratio, C_array_consistency_ratios
