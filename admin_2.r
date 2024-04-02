library("readxl")
library(openxlsx)
library(dplyr)
library(tibble)
library(ggplot2)
library(tidyverse)

df <- read_excel("Tes Excel Admin Klinik 2.xlsx", range = "C4:G9", col_names = c("Nama_pasien", "Kelas", "Persalinan", "Tanggal_masuk", "Tanggal_keluar"))
print(df)


df$Tanggal_masuk <- as.Date(df$Tanggal_masuk)
df$Tanggal_keluar <- as.Date(df$Tanggal_keluar)
df$Lama_inap <- df$Tanggal_keluar - df$Tanggal_masuk


inap <- function(x, y) {
    if (x == "BPJS") {
        return(300000 * y)
    } else if (x == "Umum") {
        return(900000 * y)
    }
}
df$inap <- mapply(inap, df$Kelas, df$Lama_inap)


inap <- function(x, y) {
    case_when(
        x == "BPJS" ~ 300000 * y,
        x == "Umum" ~ 900000 * y
    )
}
df$inap1 <- mapply(inap, df$Kelas, df$Lama_inap)

df <- df %>% mutate(
    inap2 = case_when(
        Kelas == "BPJS" ~ 300000 * as.numeric(Lama_inap),
        Kelas == "Umum" ~ 900000 * as.numeric(Lama_inap)
    )
)
df$inap3 <- recode(df$Kelas, BPJS = 300000 * as.numeric(df$Lama_inap), Umum = 900000 * as.numeric(df$Lama_inap))
df$inap4 <- recode(df$Kelas, BPJS = 300000, Umum = 900000) * as.numeric(df$Lama_inap)
df <- df %>% mutate(
    inap5 = recode(Kelas, BPJS = 300000, Umum = 900000) * Lama_inap
)
df <- df %>% mutate(
    inap6 = recode(Kelas, BPJS = 300000 * Lama_inap, Umum = 900000 * Lama_inap)
)
df$inap7 <- ifelse(df$Kelas == 'BPJS', 300000 * as.numeric(df$Lama_inap), ifelse(df$Kelas == 'Umum', 900000 * as.numeric(df$Lama_inap), 0))






layanan <- function(x, y) {
    if (x == "BPJS") {
        return(150000 * y)
    } else if (x == "Umum") {
        return(300000 * y)
    }
}
df$layanan <- mapply(layanan, df$Kelas, df$Lama_inap)

layanan <- function(x, y) {
    switch(x,
        "BPJS" = 150000 * y,
        "Umum" = 300000 * y
    )
}
df$layanan2 <- mapply(layanan, df$Kelas, df$Lama_inap)



df$layanan3 <- recode(df$Kelas, BPJS = 150000 * as.numeric(df$Lama_inap), Umum = 300000 * as.numeric(df$Lama_inap))
df$layanan4 <- recode(df$Kelas, BPJS = 150000, Umum = 300000) * as.numeric(df$Lama_inap)
df <- df %>% mutate(
    layanan5 = recode(Kelas, BPJS = 150000, Umum = 300000) * Lama_inap
)
df <- df %>% mutate(
    layanan6 = recode(Kelas, BPJS = 150000 * Lama_inap, Umum = 300000 * Lama_inap)
)
layanan <- function(x, y) {
    recode(x, BPJS = 150000, Umum = 300000) * y
}
df$layanan7 <- mapply(layanan, df$Kelas, df$Lama_inap)
layanan <- function(x, y) {
    recode(x, 
    BPJS = 150000 * y, 
    Umum = 300000 * y)
}
df$layanan8 <- mapply(layanan, df$Kelas, df$Lama_inap)





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


persalinan <- function(x, y) {
    if (x == "BPJS" & y == "Dokter") {
        return(1000000)
    } else if (x == "BPJS" & y == "Bidan") {
        return(500000)
    } else if (x == "Umum" & y == "Dokter") {
        return(1500000)
    } else if (x == "Umum" & y == "Bidan") {
        return(700000)
    }
}
df$biaya_persalinan5 <- mapply(persalinan, df$Kelas, df$Persalinan)


persalinan <- function(x, y) {
    case_when(
        x == "BPJS" & y == "Dokter" ~ 1000000,
        x == "BPJS" & y == "Bidan" ~ 500000,
        x == "Umum" & y == "Dokter" ~ 1500000,
        x == "Umum" & y == "Bidan" ~ 700000
    )
}
df$biaya_persalinan1 <- mapply(persalinan, df$Kelas, df$Persalinan)


persalinan <- function(x, y) {
    switch(paste(x, y),
        "BPJS Dokter" = 1000000,
        "BPJS Bidan" = 500000,
        "Umum Dokter" = 1500000,
        "Umum Bidan" = 700000
    )
}
df$biaya_persalinan2 <- mapply(persalinan, df$Kelas, df$Persalinan)




df <- df %>% mutate(
    persalinan3 = case_when(
        Kelas == "BPJS" & Persalinan == "Dokter" ~ 1000000,
        Kelas == "BPJS" & Persalinan == "Bidan" ~ 500000,
        Kelas == "Umum" & Persalinan == "Dokter" ~ 1500000,
        Kelas == "Umum" & Persalinan == "Bidan" ~ 700000
    )
)

df$persalinan4 <- recode(
    df$Kelas,
    BPJS = ifelse(df$Persalinan == "Dokter", 1000000, 500000),
    Umum = ifelse(df$Persalinan == "Dokter", 1500000, 700000)
)

df <- df %>% mutate(
    persalinan6 = recode(Kelas,
        "BPJS" = ifelse(Persalinan == "Dokter", 1000000, 500000),
        "Umum" = ifelse(Persalinan == "Dokter", 1500000, 700000)
    )
)
layanan <- function(x, y) {
    recode(x,
        "BPJS" = ifelse(y == "Dokter", 1000000, 500000),
        "Umum" = ifelse(y == "Dokter", 1500000, 700000)
    )
}
df$persalinan36 <- mapply(layanan, df$Kelas, df$Persalinan)

df <- df %>%
    mutate(
        persalinan37 = ifelse(
        Kelas == "BPJS" & Persalinan == "Dokter", 1000000,
        ifelse(
            Kelas == "BPJS" & Persalinan == "Bidan", 500000,
            ifelse(
            Kelas == "Umum" & Persalinan == "Dokter", 1500000,
            ifelse(
                Kelas == "Umum" & Persalinan == "Bidan", 700000,
                NA # Jika tidak ada kondisi yang cocok
            )
            )
        )
        )
    )



df$Total_Biaya <- rowSums(df[, c("inap", "layanan", "biaya_persalinan")], na.rm = TRUE)
df$Total_Biaya2 <- rowSums(df[, c("inap3", "layanan3", "biaya_persalinan")], na.rm = TRUE)
df$Total_biaya3 <- df$inap4 + df$layanan4 + df$biaya_persalinan
df$Total_biaya4 <- df$inap5 + df$layanan5 + df$biaya_persalinan
print(df)
print(data.frame(sapply(df, class)))


print("total bayar: ")
print(sum(df$Total_Biaya))
cat("\n\n")
print("Rata-rata: ")
print(mean(df$Total_Biaya))
cat("\n\n")
print("Biaya Tertinggi: ")
print(max(df$Total_Biaya))
cat("\n\n")
print("Biaya Terendah: ")
print(min(df$Total_Biaya))
cat("\n\n")


tabel_akhir1 <- df %>%
    group_by(Kelas) %>%
    summarise(Jumlah_pasien = n())
tabel_akhir2 <- df %>%
    group_by(Kelas) %>%
    summarise(total_biaya = sum(Total_Biaya))
tabel_akhir <- inner_join(tabel_akhir1, tabel_akhir2, by = "Kelas", relationship = "many-to-many")
print(tabel_akhir)
tabel_akhir <- column_to_rownames(tabel_akhir, var = "Kelas")
print(tabel_akhir)


write.xlsx(df, "admin_2.xlsx")
