nama <- 'John'
umur <- 30

pesan <- paste("Nama:", nama, ',',"Umur:", umur)
print(pesan)


pesan <- sprintf("Nama: %s, Umur: %i", nama, umur)
print(pesan)
pesan <- sprintf("Nama: '%s', Umur: '%i'", nama, umur)
print(pesan)
