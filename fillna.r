df <- data.frame(
    nama = c('Niko', 'vio', 'Gaby', 'Maria'),
    kelas = c(4201, 4201, 4201, NA),
    pasangan = c('Yes', NA,'Yes', 'No')
)
print(df)

df[is.na(df)] <- 0
df[df == 0] <- 'YOOOO'
print(df)