library("readxl")
library(openxlsx)
library(dplyr)
library(tibble)
library(ggplot2)
library(tidyverse)


df <- read_excel('Tes Excel Admin Klinik.xlsx', col_names = c('Nama_pasien', 'Kelas', 'Penanganan', 'Tanggal_masuk', 'Tanggal_keluar'), skip=1, range = "C4:G8")
# df <- na.omit(df) # Menghapus baris dengan nilai NA di seluruh kolom
# Menghapus baris dengan nilai NA di kolom 'Kelas'
# df <- subset(df, !is.na(Kelas))
print(df)

df$Tanggal_masuk <- as.Date(df$Tanggal_masuk, format = "%Y-%m-%d %H:%M:%S")
df$Tanggal_keluar <- as.Date(df$Tanggal_keluar, format = "%Y-%m-%d %H:%M:%S")
df$Tanggal_keluar1 <- ymd(df$Tanggal_keluar)
df$Lama_tinggal <- df$Tanggal_keluar - df$Tanggal_masuk
df$Lama_tinggal_1 <- df$Tanggal_keluar1 - df$Tanggal_masuk
df$Lama_tinggal1 <- day(df$Tanggal_keluar) - day(df$Tanggal_masuk)
# Menghitung selisih antara tanggal keluar dan tanggal masuk
df$Lama_tinggal2 <- difftime(df$Tanggal_keluar, df$Tanggal_masuk, units = "days")



inap <- function(x, y){
    if (x == 'A'){
        return (300000 *y)
    }else if (x == 'B'){
        return (200000*y)
    }else if (x == 'C'){
        return (100000*y)
    }
}
df$inap <- mapply(inap, df$Kelas, df$Lama_tinggal)



# inap <- function(x, y) {
#     switch(x,
#          'A' = 300000 * y,
#          'B' = 200000 * y,
#          'C' = 100000 * y,
#          300000 * y)  # Jika x tidak sama dengan 'A', 'B', atau 'C', maka gunakan 300000 * y
# }
# df$inap <- mapply(inap, df$Kelas, df$Lama_tinggal)



layanan <- function(x,y){
    if (x == 'A'){
        return (150000*y)
    }else if (x == 'B'){
        return (100000*y)
    }else if (x == 'C'){
        return (50000*y)
    }
}
df$layanan <- mapply(layanan, df$Kelas, df$Lama_tinggal)

salin <- function(x,y){
    if(x == 'Dokter'){
        return (200000)
    }else if(x == 'Bidan'){
        return (100000)
    }
}
df$persalinan <- sapply(df$Penanganan, salin)
df$total <- df$inap + df$layanan + df$persalinan
df$Total_Biaya <- rowSums(df[, c('inap', 'layanan', 'persalinan')], na.rm = TRUE)



# df <- df %>% mutate(
#     inap1 = case_when(
#         Kelas == 'A' ~ 300000 * Lama_tinggal,
#         Kelas == 'B' ~ 200000 * Lama_tinggal,
#         Kelas == 'C' ~ 100000 * Lama_tinggal
#     )
# )
# df <- df %>% mutate(
#     layanan1 = case_when(
#         Kelas == 'A' ~ 150000 * Lama_tinggal,
#         Kelas == 'B' ~ 100000 * Lama_tinggal,
#         Kelas == 'C' ~ 50000 * Lama_tinggal
#     )
# )

print(df)


print('total bayar: ')
print(sum(df$Total_Biaya))
cat("\n\n")
print('Biaya Tertinggi: ')
print(max(df$Total_Biaya))
cat("\n\n")
print('Biaya Terendah: ')
print(min(df$Total_Biaya))
cat("\n\n")
tabel1 <- df %>% group_by(Kelas) %>% summarise(jumlah_pasien = n())
tabel2 <- df %>% group_by(Kelas) %>% summarise(jumlah_biaya = sum(Total_Biaya))
tabel_akhir <- inner_join(tabel1, tabel2, by = 'Kelas', relationship = "many-to-many")
print(tabel_akhir)
cat('\n\n')
tabel_akhir <- column_to_rownames(tabel_akhir, var='Kelas') 
print(tabel_akhir)

write.xlsx(df, 'admin_1.xlsx')