library("readxl")
library(openxlsx)
library(dplyr)
library(tibble)
library(ggplot2)
library(tidyverse)

df <- read_excel('latihanR/Tes Excel Admin Klinik 2.xlsx', range="C4:G9", col_names = c('Nama_pasien', 'Kelas', 'Persalinan', 'Tanggal_masuk', 'Tanggal_keluar'))
print(df)


df$Tanggal_masuk <- as.Date(df$Tanggal_masuk)
df$Tanggal_keluar <- as.Date(df$Tanggal_keluar)
df$Lama_inap <- df$Tanggal_keluar - df$Tanggal_masuk


inap <- function(x){
    if (x == "BPJS"){
        return(300000)
    }else if (x == "Umum") {
        return(900000)
    }
}
df$inap <- sapply(df$Kelas, inap)*df$Lama_inap


layanan <- function(x,y) {
    if (x == "BPJS"){
        return(150000*y)
    }else if(x == "Umum"){
        return(300000*y)
    }
}
df$layanan <- mapply(layanan, df$Kelas, df$Persalinan)


persalinan <- function(x,y){
    if(x == "BPJS"){
        if(y == "Dokter"){
            return(1000000)
        }else if(y == 'Bidan'){
            return(500000)
        }
    }else if(x == "Umum"){
        if(y == "Dokter"){
            return(1500000)
        }else if(y == 'Bidan'){
            return(700000)
        }
    }
}
df$biaya_persalinan <- mapply(persalinan, df$Kelas, df$Persalinan)
df$Total_Biaya <- rowSums(df[,c('inap', 'layanan', 'biaya_persalinan')], na.rm=TRUE)
print(df)


print('total bayar: ')
print(sum(df$Total_Biaya))
cat("\n\n")
print('Rata-rata: ')
print(mean(df$Total_Biaya))
cat("\n\n")
print('Biaya Tertinggi: ')
print(max(df$Total_Biaya))
cat("\n\n")
print('Biaya Terendah: ')
print(min(df$Total_Biaya))
cat("\n\n")


tabel_akhir1 <- df %>% group_by(Kelas) %>% summarise(Jumlah_pasien = n())
tabel_akhir2 <- df %>% group_by(Kelas) %>% summarise(total_biaya = sum(Total_Biaya))
tabel_akhir <- inner_join(tabel_akhir1, tabel_akhir2, by = 'Kelas', relationship = "many-to-many")
print(tabel_akhir)
tabel_akhir <- column_to_rownames(tabel_akhir, var = 'Kelas')
print(tabel_akhir)


write.xlsx(df, 'admin_2.xlsx')