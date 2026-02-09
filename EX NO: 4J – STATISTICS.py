import statistics

sample = (1, 1.3, 1.2, 1.9, 2.5, 2.2)
m = statistics.mean(sample)
print("Variance of sample set is", statistics.variance(sample, xbar=m))
