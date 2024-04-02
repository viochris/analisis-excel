df <- data.frame(
    nama = c('Niko', 'vio', 'Gaby', 'Maria'),
    kelas = c(4201, 4201, 4201, NA),
    pasangan = c('Yes', NA,'Yes', 'No')
)
print(df)
df1 <- na.omit(df)
print(df1)
df2 <- subset(df, !is.na(pasangan))
print(df2)
df3 <- df[is.na(df$pasangan), ]
print(df3)
df3 <- df[!is.na(df$pasangan), ]
print(df3)
df4 <- df[,colSums(is.na(df))==0]
print(df4)
df5 <- df[, !colSums(is.na(df) > 0)]
print(df5)
df5 <- df[rowSums(is.na(df)) >0, ]
print(df5)
df5 <- df[!rowSums(is.na(df)) >0, ]
print(df5)
df5 <- df[, colSums(is.na(df)) >0]
print(df5)

