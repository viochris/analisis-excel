# Membuat DataFrame contoh
df <- data.frame(
    Nama = c("John", "Doe", "Jane", "Smith", "John", NA, "Bari", "Jan"),
    Usia = c(30, 25, 35, 40, 30, 34, NA, 35)
)
print(colnames(df))
print(rownames(df))
print(row.names(df))
print(names(df))
cat('\n\n')


tabel <- prop.table(table(df$Nama))
print(tabel)

print(names(tabel))
print(as.vector(tabel))
print(row.names(tabel))
print(rownames(tabel))



# YANG BARI, DOE, ETC, BUKANLAH KOLOM TAPI BARIS. WALAUPUN LETAKNYA SEPERTI KOLOM. BUKTINYA, UTNUK MELIHAT
# YANG ITU, HARUS MENGGUNAKAN ROWNAMES.
#      Bari       Doe       Jan      Jane      John     Smith 
# 0.1428571 0.1428571 0.1428571 0.1428571 0.2857143 0.1428571 