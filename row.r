library("readxl")
library(openxlsx)
library(dplyr)
library(tibble)
library(ggplot2)
library(tidyverse)


df <- data.frame(A = c(1, 2, 3),
                    B = c(4, 5, 6),
                    C = c(7, 8, 9))
print(df)
cat()


print(colnames(df))
print(rownames(df))
row_sums <- rowSums(df)
print(row_sums)
row_means <- rowMeans(df)
print(row_means)
row_maxs <- apply(df, 1, max)
print(row_maxs)
row_mins <- apply(df, 1, min)
print(row_mins)
row_medians <- apply(df, 1, median)
print(row_medians)

cat('\n\n')

col_maxs <- apply(df, 2, max)
print(col_maxs)
col_mins <- apply(df, 2, min)
print(col_mins)
col_medians <- apply(df, 2, median)
print(col_medians)

cat('\n\n')
num_rows <- nrow(df)
print(num_rows)
num_cols <- ncol(df)
print(num_cols)
dim_df <- dim(df)
print(dim_df)
dim_df <- dimnames(df)
print(dim_df)

print(lapply(df, class))
print(sum(df))