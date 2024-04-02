library(tidyverse)

df = data.frame(
    EmbarkedS = c(1,2,3,4,5),
    EmbarkedQ = c(1,2,3,4,5),
    EmbarkedR = c(1,2,3,4,5)
)
print(df)
# colnames(df) <- gsub('Embarked', ' ', colnames(df))
# print(df)
# print(df$` S`)


# colnames(df) <- trimws(gsub('Embarked', ' ', colnames(df)))
# print(df)
# print(df$S)


# colnames(df) <- str_replace_all(colnames(df), 'Embarked', ' ')
# print(df)
# print(df$` S`)


colnames(df) <- trimws(str_replace_all(colnames(df), 'Embarked', ' '))
print(df)
print(df$S)