library(tidyverse)

na <- "makanan"

hasil <- str_replace_all(na, 'a', 'e')
print(hasil)

hasil <- str_replace(na, 'a', 'e')
print(hasil)

hasil <- str_replace_all(na, 'makan', 'minum')
print(hasil)

hasil <- str_replace(na, 'makan', 'minum')
print(hasil)

hasil <- str_replace_all(na, 'makanan', 'minuman')
print(hasil)

hasil <- str_replace(na, 'makanan', 'minuman')
print(hasil)