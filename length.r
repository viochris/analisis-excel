# Membuat DataFrame contoh
df <- data.frame(
    Nama = c("John", "Doe", "Jane", "Smith", "John", NA, "Bari", "Jan"),
    Usia = c(30, 25, 35, 40, 30, 34, NA, 35)
)

# Menghitung jumlah baris dalam dataframe
jumlah_baris <- nrow(df)
print(jumlah_baris)

# Menghitung jumlah kolom dalam dataframe
jumlah_kolom <- ncol(df)
print(jumlah_kolom)

print(dim(df))
print(dim(df)[1])
print(dim(df)[2])
print(dimnames(df))
cat('\n\n')
cat('\n\n')
print(dimnames(df)[1])
print(dimnames(df)[2])

# Menghitung panjang kolom 'Nama'
panjang_nama <- length(df$Nama)
print(panjang_nama)


print(nchar(df$Nama))

