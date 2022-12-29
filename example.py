from ranking import compute_ranking_and_consistency_ratios


# RI_n_9[x] - RI_x_9 where x = len(matrix)
RI_n_9 = [0, 0, 0, 0.546, 0.83, 1.08, 1.26, 1.33, 1.41, 1.45, 1.47]

C_1 = [
    [1, 1/7, 1/5],
    [7, 1, 3],
    [5, 1/3, 1]
]

C_2 = [
    [1, 5, 9],
    [1/5, 1, 4],
    [1/9, 1/4, 1]
]

C_3 = [
    [1, 4, 1/5],
    [1/4, 1, 1/9],
    [5, 9, 1]
]

C_4 = [
    [1, 9, 4],
    [1/9, 1, 1/4],
    [1/4, 4, 1]]

C_5 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

C_6 = [
    [1, 6, 4],
    [1/6, 1, 1/3],
    [1/4, 3, 1]
]

C_7 = [
    [1, 9, 6],
    [1/9, 1, 1/3],
    [1/6, 3, 1]
]

C_8 = [
    [1, 1/2, 1/2],
    [2, 1, 1],
    [2, 1, 1]
]

C_array = [C_1, C_2, C_3, C_4, C_5, C_6, C_7, C_8]

C_1_2 = [
    [1, 4, 7, 5, 8, 6, 6, 2],
    [1 / 4, 1, 5, 3, 7, 6, 6, 1 / 3],
    [1 / 7, 1 / 5, 1, 1 / 3, 5, 3, 3, 1 / 5],
    [1 / 5, 1 / 3, 3, 1, 6, 3, 4, 1 / 2],
    [1 / 8, 1 / 7, 1 / 5, 1 / 6, 1, 1 / 3, 1 / 4, 1 / 7],
    [1 / 6, 1 / 6, 1 / 3, 1 / 3, 3, 1, 1 / 2, 1 / 5],
    [1 / 6, 1 / 6, 1 / 3, 1 / 4, 4, 2, 1, 1 / 5],
    [1 / 2, 3, 5, 2, 7, 5, 5, 1]
]


print(compute_ranking_and_consistency_ratios(C_array, C_1_2, RI_n_9))


# categories
# 1. salary
# 2. qualifications
# 3. travel_cost
# 4. benefits
# 5. development_opportunities