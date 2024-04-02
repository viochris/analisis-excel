# Mengimpor paket-paket yang diperlukan
library(dplyr)
library(tidyr)

# Membuat tabel data frame
df_asal <- data.frame(
    AREA = c("A", "A", "B", "B", "A", "B"),
    CUSTOMER_NAME = c("Cust1", "Cust2", "Cust1", "Cust2", "Cust1", "Cust2"),
    CUSTOMER_NAME2 = c("Cust3", "Cust4", "Cust3", "Cust4", "Cust3", "Cust4"),
    BOX_QTY = c(10, 20, 15, 25, 30, 35),
    TOTAL_WEIGHT = c(100, 200, 150, 250, 300, 350)
)

# Melakukan transformasi data
pivot <- df_asal %>%
    group_by(AREA, CUSTOMER_NAME) %>%
    summarise(BOX_QTY = sum(BOX_QTY), TOTAL_WEIGHT = sum(TOTAL_WEIGHT)) %>%
    pivot_wider(names_from = AREA, values_from = c(BOX_QTY, TOTAL_WEIGHT))

# Menampilkan tabel pivot
print(pivot)




# Membuat tabel pivot menggunakan xtabs
pivot_xtabs <- xtabs(cbind(BOX_QTY, TOTAL_WEIGHT) ~ AREA + CUSTOMER_NAME, data = df_asal)
print(pivot_xtabs)

cat('\n\n\n')
# Membuat tabel pivot menggunakan xtabs
pivot_xtabs <- ftable(xtabs(cbind(BOX_QTY, TOTAL_WEIGHT) ~ AREA + CUSTOMER_NAME, data = df_asal))
# Menampilkan tabel pivot
print(pivot_xtabs)
cat('\n\n\n')



pivot_xtabs <- ftable(xtabs(cbind(BOX_QTY, TOTAL_WEIGHT) ~ ., data = df_asal, addNA = TRUE))
# Menampilkan tabel pivot
print(pivot_xtabs)
# pivot_xtabs[pivot_xtabs == 0] <- NA
# print(pivot_xtabs)