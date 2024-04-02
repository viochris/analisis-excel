library("readxl")
library(openxlsx)
library(dplyr)
library(ggplot2)


df <- read_excel('umkm.xlsx')
# df <- subset(df, select=-No.)
df <- select(df, -No.)

# df$Nilai <- as.numeric(gsub(',', '.',df$Nilai))
df <- mutate(df, Nilai = as.numeric(gsub(',', '.',df$Nilai)))
colnames(df) <- c('Nama_Data', 'Nilai')
print(df)

# Menyiapkan data
x <- df$Nama_Data
y <- df$Nilai



# Membuat plot bar horizontal
bp <- barplot(df$Nilai, 
        # horiz = TRUE, 
        names.arg = df$Nama_Data, 
        col = "skyblue", 
        main = "Preferensi Pembelian Produk UMKM", 
        xlab = "Persentase (%)", 
        cex.names = 0.8)

# Menambahkan label angka di tengah bar
for (i in 1:nrow(df)) {
    text(bp[i], df$Nilai[i], labels = paste0(round(df$Nilai[i], 2), "%"), pos = 3, cex = 0.8, xpd = TRUE)
}