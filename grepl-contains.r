# Buat vektor karakter
words <- c("apple", "banana", "grape", "orange", "pineapple")

# Cocokkan pola 'apple' dalam vektor
hasil <- grepl("apple", words)
# Output: TRUE FALSE FALSE FALSE  TRUE
print(hasil)

# Cocokkan pola 'an' dalam vektor
hasil <- grepl("an", words)
# Output: FALSE TRUE FALSE TRUE FALSE
print(hasil)

# Cocokkan pola 'pear' dalam vektor
hasil <- grepl("pear", words)
# Output: FALSE FALSE FALSE FALSE FALSE
print(hasil)