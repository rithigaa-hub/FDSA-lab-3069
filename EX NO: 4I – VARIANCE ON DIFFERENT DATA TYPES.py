from statistics import variance
from fractions import Fraction

sample1 = (1, 2, 5, 4, 8, 9, 12)
sample2 = (-2, -4, -3, -1, -5, -6)
sample3 = (-9, -1, 0, 2, 1, 3, 4, 19)
sample4 = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(5, 6))
sample5 = (1.23, 1.45, 2.1, 2.2, 1.9)

print(variance(sample1))
print(variance(sample2))
print(variance(sample3))
print(variance(sample4))
print(variance(sample5))
