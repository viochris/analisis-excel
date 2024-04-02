import numpy as np

np.random.seed(42)

# Menghasilkan angka acak dalam distribusi uniform antara 0 dan 1
random_uniform = np.random.rand(4, 3)
print("Random Uniform:\n", random_uniform)
random_uniform = np.random.rand(3)
print("Random Uniform:\n", random_uniform)
# Contoh hasil:
# Random Uniform:
#  [[0.12345678 0.98765432 0.54321098]
#  [0.87654321 0.23456789 0.45678901]
#  [0.34567891 0.67890123 0.90123457]]
#  [0.34567891 0.67890123 0.90123457]]

# Menghasilkan angka acak dalam distribusi normal standar
random_normal = np.random.randn(4, 3)
print("\nRandom Normal:\n", random_normal)
random_normal = np.random.randn(4)
print("\nRandom Normal:\n", random_normal)
# Contoh hasil:
# Random Normal:
#  [[ 0.12345678 -0.98765432  0.54321098]
#  [ 0.87654321 -0.23456789 -0.45678901]
#  [ 0.34567891  0.67890123  0.90123457]]
#  [ 0.34567891  0.67890123  0.90123457]]

random_standard_normal = np.random.standard_normal((3, 3))
print("np.random.standard_normal():")
print(random_standard_normal)

# Menghasilkan bilangan bulat acak dalam rentang tertentu
random_integers = np.random.randint(1, 100, size=(4, 3))
print("\nRandom Integers:\n", random_integers)
random_integers = np.random.randint(1, 100, 3)
print("\nRandom Integers:\n", random_integers)
# Contoh hasil:
# Random Integers:
#  [[73 34  4]
#  [25 65 82]
#  [47 31 85]]
#  [47 31 85]]


# 4. np.random.random()
# 5. np.random.random_sample()
# 6. np.random.ranf()
# 7. np.random.sample()
# Semua fungsi ini menghasilkan angka acak dalam distribusi uniform antara 0 dan 1.
random_val = np.random.random((4, 3))
print("\nnp.random.random():", random_val)
random_val = np.random.random(4)
print("\nnp.random.random():", random_val)
random_sample_val = np.random.random_sample((4,3))
print("np.random.random_sample():", random_sample_val)
random_sample_val = np.random.random_sample(4)
print("np.random.random_sample():", random_sample_val)
ranf_val = np.random.ranf((4,3))
print("np.random.ranf():", ranf_val)
ranf_val = np.random.ranf(4)
print("np.random.ranf():", ranf_val)
sample_val = np.random.sample((4,3))
print("np.random.sample():", sample_val)
sample_val = np.random.sample(4)
print("np.random.sample():", sample_val)



# Mengambil sampel acak dari array
array = np.array([1, 2, 3, 4, 5])
random_sample = np.random.choice(array, size=3)
print("\nRandom Sample:\n", random_sample)
random_sample = np.random.choice(array, size=(2, 3))
print("\nRandom Sample:\n", random_sample)
# Contoh hasil:
# Random Sample:
#  [4 2 5]

# Mengacak urutan elemen dalam array
array_to_shuffle = np.array([1, 2, 3, 4, 5])
np.random.shuffle(array_to_shuffle)
print("\nShuffled Array:\n", array_to_shuffle)
# Contoh hasil:
# Shuffled Array:
#  [5 1 3 4 2]

# Mengembalikan permutasi acak dari array
array_to_permute = np.array([1, 2, 3, 4, 5])
random_permutation = np.random.permutation(array_to_permute)
print("\nRandom Permutation:\n", random_permutation)
# Contoh hasil:
# Random Permutation:
#  [3 5 1 4 2]

# Menghasilkan angka acak dalam distribusi normal
random_normal_distribution = np.random.normal(loc=0, scale=2, size=(4, 3))
print("\nRandom Normal Distribution:\n", random_normal_distribution)
# Contoh hasil:
# Random Normal Distribution:
#  [[ 0.04259431  1.36376995 -0.30344422]
#  [-0.08979307 -0.29957131  0.27445671]
#  [ 1.10297957 -0.92443742 -1.37780648]]



# Menghasilkan angka acak dalam distribusi uniform dalam rentang tertentu
random_uniform_range = np.random.uniform(low=0, high=10, size=(3, 3))
print("\nRandom Uniform Range:\n", random_uniform_range)
random_uniform_range = np.random.uniform(0, 19, 4)
print("\nRandom Uniform Range:\n", random_uniform_range)
# Contoh hasil:
# Random Uniform Range:
#  [[5.7767368  6.46924667 9.46672448]
#  [1.72931243 6.39254734 1.38503599]
#  [8.01280984 4.30589634 7.2304792 ]]
