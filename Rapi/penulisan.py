"""

Statement Gabungan
Saat Anda membuat program dengan banyak statement, usahakan untuk 
tidak menggabungkan >1 statement pada baris yang sama

if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()


Penggunaan Trailing Commas
FILES = ('setup.cfg',)


FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
            error=True,
            )


    """
from typing import List

from numpy import average

def hitung_rata_rata(data: List[float]) -> float:
    """Fungsi untuk menghitung rata-rata dari sejumlah bilangan.

    Args:
        data (List[float]): Sebuah list yang berisi bilangan-bilangan.

    Returns:
        float: Rata-rata dari bilangan-bilangan dalam list.
    """
    if not data:
        return 0.0
    return sum(data) / len(data)

# Contoh penggunaan fungsi
data_list = [1.5, 2.5, 3.5, 4.5]
rata_rata = hitung_rata_rata(data_list)
print("Rata-rata:", rata_rata)

data_list = [1.5, 2.5, 3.5, 4.5]
hasil = average(data_list)
print('Rata-rata: ', hasil)
