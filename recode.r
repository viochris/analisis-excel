library(dplyr) # For data manipulation
library(tidyverse) # Collection of useful R packages
library(readr) # For CSV reading
library(arules) # For association rule mining

num_vec <- c(1:4, NA)
print(num_vec)
print(class(num_vec))
num_vec <- as.numeric(num_vec)

hasil1 <- dplyr::recode(num_vec, "a", "b", "c", "d")
print(hasil1)
hasil2 <- dplyr::recode(c(1,4,5,2,3), "a", "b", "c", "d", .default = "nothing")
print(hasil2)