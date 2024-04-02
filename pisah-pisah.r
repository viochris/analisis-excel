library(tidyverse)

# Data awal dengan data terpisah-pisah
data <- data.frame(nama = c("a   l i     c    e", "b  o b", "c  a r o l"))


# Menghapus spasi ekstra
data <- data %>%
    mutate(nama1 = str_replace_all(nama, "\\s+", ""))

# Menghapus karakter non-alfanumerik
data <- data %>%
    mutate(nama2 = str_replace_all(nama, "[^[:alnum:]]", ""))




# Menampilkan hasil
print(data)
