library("readxl")
library(openxlsx)
library(dplyr)
library(tibble)
library(ggplot2)
library(tidyverse)

df <- read_excel("Tes Excel Admin Klinik 2.xlsx", col_names = c("Nama Pasien", "Kelas", "Persalinan", "Tanggal Masuk", "Tanggal Keluar"), range = "C4:G9")
print(df)

df$`Tanggal Masuk` <- as.Date(df$`Tanggal Masuk`)
df$`Tanggal Keluar` <- ymd(df$`Tanggal Keluar`)
df$lama_inap <- df$`Tanggal Keluar` - df$`Tanggal Masuk`


df <- df %>% mutate(
    inap = recode(
        Kelas,
        BPJS = 300000 * as.numeric(lama_inap),
        Umum = 900000 * as.numeric(lama_inap)
    )
)
layanan <- function(x,y){
    switch(x,
    "BPJS" = 150000 * as.numeric(y),
    "Umum" = 300000 * as.numeric(y))
}
df$layanan <- mapply(layanan, df$Kelas, df$lama_inap)
# df <- df %>% mutate(
#     layanan = switch(
#         Kelas,
#         "BPJS" = 150000 * as.numeric(lama_inap),
#         "Umum" = 300000 * as.numeric(lama_inap)
#     )
# ) #TIDAK BISA
persalinan <- function(x, y) {
    if (x == "BPJS") {
        if (y == "Dokter") {
            return(1000000)
        } else if (y == "Bidan") {
            return(500000)
        }
    } else if (x == "Umum") {
        if (y == "Dokter") {
            return(1500000)
        } else if (y == "Bidan") {
            return(700000)
        }
    }
}
df$biaya_persalinan <- mapply(persalinan, df$Kelas, df$Persalinan)
df <- df %>% mutate(
    persalinan3 = case_when(
        Kelas == "BPJS" & Persalinan == "Dokter" ~ 1000000,
        Kelas == "BPJS" & Persalinan == "Bidan" ~ 500000,
        Kelas == "Umum" & Persalinan == "Dokter" ~ 1500000,
        Kelas == "Umum" & Persalinan == "Bidan" ~ 700000
    )
)
persalinan <- function(x,y){
    if(x == 'BPJS' & y == 'Dokter'){
        return(1000000)
    }else if(x == 'BPJS' & y == 'Bidan'){
        return(500000)
    }else if(x == 'Umum' & y == 'Dokter'){
        return(1500000)
    }else if(x == 'Umum' & y == 'Bidan'){
        return(700000)
    }
}
df$biaya_persalinan5 <- mapply(persalinan, df$Kelas, df$Persalinan)
print(sapply(df, class))
df$total_biaya <- rowSums(df[c('inap', 'layanan', 'biaya_persalinan')])
df$total_biaya2 <- rowSums(df[c('inap', 'layanan', 'persalinan3')])
df$total_biaya2a <- rowSums(df[c('inap', 'layanan', 'biaya_persalinan5')])
df$total_biaya3 <- df$inap + df$layanan + df$biaya_persalinan5
print(df)




cat('Total Bayar: ', sum(df$total_biaya), '\n\n')
cat('Rata-rata Bayar: ', mean(df$total_biaya), '\n\n')
cat('Biaya Tertinggi: ', max(df$total_biaya), '\n\n')
cat('Biaya Terendah: ', min(df$total_biaya), '\n\n')

tabel1 <- df %>% group_by(Kelas) %>% summarise(jumlah_pasien = n())
tabel2 <- df %>% group_by(Kelas) %>% summarise(jumlah_biaya = sum(total_biaya))
tabel_akhir <- inner_join(tabel1, tabel2, by = 'Kelas')
print(tabel_akhir)
tabel_akhir <- column_to_rownames(tabel_akhir, var = 'Kelas')
print(tabel_akhir)

write.xlsx(df, 'admin_2a.xlsx')