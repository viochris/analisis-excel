lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")
    
print('Selamat') if lulus else print('Perbaiki')

kelulusan = ('Perbaiki, anda belum lulus', 'Selamat, anda lulus')[lulus]
print(kelulusan)