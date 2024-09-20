import math

# Q1 Calculation
# Q1 = L + (C/F)*(iN/4 - M)
# L = lower bound, C = class width, F = frequency, N = total frequency, M = cumulative

# Grouped data frequency
grouped_data = [1, 3, 11, 21, 43, 32, 9]
grouped_quartile = []

# Quartile calculations (using made-up L, C, F values for example)
q_1 = 30 + (1 / 1) * (1 * 120 / 4 - 1)  # Example values for L, C, F
q_2 = 60 + (1 / 21) * (3 * 120 / 4 - 26)  # Example values for L, C, F
q_3 = -(q_2 - q_1)

print(f'Q1 = {q_1:.2f} | Q2 = {q_2:.2f} | Q3 = {q_3:.2f}')

# Relative Dispersion Calculation
stats_m = 78
stats_sd = 8
alge_m = 73
alge_sd = 7.6

stats_dis = (stats_sd / stats_m) * 100
alge_dis = (alge_sd / alge_m) * 100

print(
    f'Relative Dispersion - Stats: {stats_dis:.2f}% | Algebra: {alge_dis:.2f}%'
)
print(
    'Algebra had the higher relative dispersion while Stats had the higher absolute dispersion.'
)

# Z-Score Calculation
data_set = [6, 2, 8, 7, 5]
mean = sum(data_set) / len(data_set)
standard_div = math.sqrt(sum((x - mean)**2 for x in data_set) / len(data_set))

standard_scores = [(x - mean) / standard_div for x in data_set]

print(f'Z-Scores: {standard_scores}')

mean_of_z_score = sum(standard_scores) / len(standard_scores)
stdev_of_z_score = math.sqrt(
    sum((x - mean_of_z_score)**2
        for x in standard_scores) / len(standard_scores))

print(
    f'Mean of Z-Scores: {mean_of_z_score:.2f} | Standard Deviation of Z-Scores: {stdev_of_z_score:.2f}'
)

# Mass and Standard Deviation Calculation
mass_values = [20.48, 35.97, 62.34]
std_devs = [0.21, 0.46, 0.54]

mean_mass = sum(mass_values) / len(mass_values)
print(f'Mean of the mass: {mean_mass:.2f}')

std_dev_mass = math.sqrt(sum(sd**2 for sd in std_devs) / len(std_devs))
print(f'Standard Deviation of the mass: {std_dev_mass:.2f}')

# Probability and Mean Calculation
set_x = [6, 9, 12, 15, 18]
prob_x = [0.1, 0.2, 0.4, 0.2, 0.1]

mean_x = sum(x * p for x, p in zip(set_x, prob_x))
variance_x = sum((x - mean_x)**2 * p for x, p in zip(set_x, prob_x))

print(f'Mean of X: {mean_x:.2f} | Variance of X: {variance_x:.2f}')

# Generating sets of pairs from set_x
set_of_sets = [(set_x[i], set_x[j]) for i in range(len(set_x))
               for j in range(len(set_x))]

print(f'Sets of pairs: {set_of_sets}')

# Mean and Probability of pairs
mean_of_sets = []
probability_of_sets = []

for i, (m, n) in enumerate(zip(set_x, prob_x)):
  for j, (x, y) in enumerate(zip(set_x, prob_x)):
    mean_of_sets.append(m * n + x * y)
    probability_of_sets.append((prob_x[i] + prob_x[j]) / 10)

print(f'Mean of pairs: {mean_of_sets}')
print(f'Probabilities of pairs: {probability_of_sets}')
