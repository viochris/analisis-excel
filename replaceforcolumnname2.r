library(tidyverse)

df = data.frame(
    EmbarkedS = c(1,2,3,4,5),
    EmbarkedQ = c(1,2,3,4,5),
    EmbarkedR = c(1,2,3,4,5)
)
print(df)
colnames(df) <- gsub('Embarked', '', colnames(df))
print(df)