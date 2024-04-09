# Membuat DataFrame contoh
df <- data.frame(
    Nama = c("John", "Doe", "Jane", "Smith", "John", NA, "Bari", "Jan"),
    Usia = c(30, 25, 35, 40, 30, 34, NA, 35)
)



tabel <- table(df$Nama)
print(tabel)

hasil <- prop.table(table(df$Nama))
print(hasil)

print(names(tabel))
print(as.vector(tabel))
print(names(hasil))
print(as.vector(hasil))

print(sum(as.vector(hasil)))
cat('\n\n\n\n\n\n\n')


tabel <- table(df)
print(tabel)

tabel <- table(df[c('Nama', 'Usia')])
print(tabel)

hasil <- prop.table(table(df))
print(hasil)



hasil <- prop.table(table(df[c('Nama', 'Usia')]))
print(hasil)


cat('\n\n')

print(dim(tabel))
print(dimnames(tabel))
print(as.vector(tabel))
print(dim(hasil))
print(dimnames(hasil))
print(as.vector(hasil))

print(sum(as.vector(hasil)))
