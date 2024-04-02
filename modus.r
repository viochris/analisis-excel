# Contoh data
train <- data.frame(
  PassengerId = c(1, 2, 3, 4, 5),
    Survived = c(0, 1, 1, 1, 0),
    Pclass = c(3, 1, 3, 1, 3),
    Name = c("Braund, Mr. Owen Harris", "Cumings, Mrs. John Bradley (Florence Briggs Thayer)", "Heikkinen, Miss. Laina", "Futrelle, Mrs. Jacques Heath (Lily May Peel)", "Allen, Mr. William Henry"),
    Sex = c("male", "female", "female", "female", "male"),
    Age = c(22, 38, 26, 35, NA),
    Cabin = c(NA, "C85", NA, "C123", NA),
    Embarked = c("S", "C", "S", NA, "S")
)

print(table(train$Embarked))
print(which.max(table(train$Embarked)))
print(names(which.max(table(train$Embarked))))

# Mengisi nilai yang hilang dengan modus
modus <- names(which.max(table(train$Embarked)))
train$Embarked[is.na(train$Embarked)] <- modus

# Menampilkan dataframe setelah pengisian nilai yang hilang
print(train)
cat('\n\n\n\n')


print(train[rownames(train) == 4,])
cat('\n\n')
print(train[4,])
cat('\n\n')
print(train[, colnames(train) == 'Name'])
cat('\n\n')
print(train[rownames(train) == 4, colnames(train) == 'Name'])
cat('\n\n')
print(train$Name)
cat('\n\n')
print(train[, 'Name'])
cat('\n\n')
print(train[4, 4])
cat('\n\n')
print(train[4, 'Name'])
# cat('\n\n')
# print(train[1:3, 1:3])
# cat('\n\n')
# print(train[1:3, c("PassengerId", "Survived", "Pclass")])
