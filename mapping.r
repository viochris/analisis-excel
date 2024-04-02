title_mapping <- c(
    "Mr" = 0, "Miss" = 1, "Mrs" = 2,
    "Master" = 3, "Dr" = 3, "Rev" = 3, "Col" = 3, "Major" = 3, "Mlle" = 3, "Countess" = 3,
    "Ms" = 3, "Lady" = 3, "Jonkheer" = 3, "Don" = 3, "Dona" = 3, "Mme" = 3, "Capt" = 3, "Sir" = 3
)

print(title_mapping)
print(names(title_mapping))
print(as.vector(title_mapping))
cat('\n\n\n')

train <- read.csv("ML/youtube/train.csv", na.strings = c("", "NA"))
test <- read.csv("ML/youtube/test.csv", na.strings = c("", "NA"))

df <- table(train$Embarked)
print(df)
print(names(df))
print(as.vector(df))
cat('\n\n\n')

print(factor(train$Embarked))