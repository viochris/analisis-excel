# Contoh DataFrame
df <- data.frame(ID = c(1, 2, 3, 4),
                Sales = c(100, 150, 80, 200),
                Product = c("A", "B", "C", "D"))

# Mengurutkan DataFrame secara menaik berdasarkan kolom "Sales"
df_asc <- df[order(df$Sales), ]
print("DataFrame setelah diurutkan secara menaik berdasarkan Sales:")
print(df_asc)

# Mengurutkan DataFrame secara menurun berdasarkan kolom "Sales"
df_desc <- df[order(-df$Sales), ]
print("DataFrame setelah diurutkan secara menurun berdasarkan Sales:")
print(df_desc)
