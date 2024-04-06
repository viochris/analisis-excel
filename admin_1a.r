library("readxl")
library(openxlsx)
library(dplyr)
library(tibble)
library(ggplot2)
library(tidyverse)

df <- read_excel('Tes Excel Admin Klinik.xlsx',col_names = c('Nama Pasien', 'Kelas', 'Penanganan', 'Tanggal Masuk', 'Tanggal Keluar'), range = 'C4:G8')
print(df)

df$`Tanggal Masuk` <- as.Date(df$`Tanggal Masuk`)
df$`Tanggal Keluar` <- ymd(df$`Tanggal Keluar`)
df$lama_tinggal <- df$`Tanggal Keluar` - df$`Tanggal Masuk`
df$lama_tinggal2 <- days(df$`Tanggal Keluar`) - days(df$`Tanggal Masuk`)
df$lama_tinggal3 <- day(df$`Tanggal Keluar`) - day(df$`Tanggal Masuk`)
df <- df %>% mutate(
    Inap = case_when(
        Kelas == 'A' ~ 300000*lama_tinggal,
        Kelas == 'B' ~ 200000*lama_tinggal,
        Kelas == 'C' ~ 100000*lama_tinggal
    )
)
df$Inap <- as.numeric(df$Inap)
df$layanan <- case_when(
    df$Kelas == 'A' ~ 150000*df$lama_tinggal,
    df$Kelas == 'B' ~ 100000*df$lama_tinggal,
    df$Kelas == 'C' ~ 50000*df$lama_tinggal
)
df$layanan <- as.numeric(df$layanan)
df$persalinan <- recode(
    df$Penanganan,
    'Dokter' = 200000,
    'Bidan' = 100000
)
df$total_biaya <- df$Inap + df$layanan + df$persalinan
df$total_biaya2 <- rowSums(df[c('Inap', 'layanan', 'persalinan')])
print(df)

print('Total Bayar: ')
print(sum(df$total_biaya))
print('Biaya Tertinggi: ')
print(max(df$total_biaya))
print('Biaya Terendah: ')
print(min(df$total_biaya))

tabel1 <- df %>% group_by(Kelas) %>% summarise(jumlah_pasien = n())
tabel2 <- df %>% group_by(Kelas) %>% summarise(jumlah_biaya = sum(total_biaya))
tabel_akhir <- merge(tabel1, tabel2, by='Kelas')
print(tabel_akhir)
tabel_akhir <- column_to_rownames(tabel_akhir, var='Kelas')
print(tabel_akhir)

write.xlsx(df, 'admin_1a.xlsx')