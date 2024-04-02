library(dplyr)


# Contoh vektor
vektor <- c(1, 2, 3, 2, 4, 3)

# Menggunakan duplicated() untuk menemukan baris yang duplikat
duplikat <- duplicated(vektor)
print(duplikat)

# Contoh frame data
df <- data.frame(
    Customer_Code = c('A001', 'A002', 'A003', 'A002', 'A004', 'A001', 'A005'),
    Customer_Name = c('John', 'Doe', 'Jane', 'Doe', 'Smith', 'Nita', 'Alice')
)


hasil1 <- df[!duplicated(df$Customer_Code), ]
print(hasil1)
hasil2 <- df[duplicated(df$Customer_Code), ]
print(hasil2)
hasil3 <- df[!duplicated(df), ]
print(hasil3)
hasil4 <- df[duplicated(df), ]
print(hasil4)

cat('\n\n\n\n\n')

#keduanya dihilangkan, dalam hal ini, yang ke 2 dan ke 4 sama-sama dihilangkan!!!
# df_unique <- df[!duplicated(df) & !duplicated(df, fromLast = TRUE), ]
# print(df_unique)


print('kolom tertentu')
tabel1 <- df %>% distinct(Customer_Code)
print(tabel1)
tabel1 <- df %>% distinct(Customer_Code, .keep_all=TRUE)
print(tabel1)
tabel1 <- distinct(df, Customer_Code)
print(tabel1)
tabel1 <- distinct(df, Customer_Code, .keep_all=TRUE)
print(tabel1)


cat('\n\n\n')
print('untuk semua')
#baik diberi .kepp_all atau tidak, sama saja untuk yang distinct(), alias distinct tanpa isi
tabel1 <- df %>% distinct()
print(tabel1)
tabel1 <- df %>% distinct(.keep_all=TRUE)
print(tabel1)
tabel1 <- distinct(df)
print(tabel1)
tabel1 <- distinct(df, .keep_all=TRUE)
print(tabel1)