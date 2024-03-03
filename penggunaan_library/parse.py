import argparse
import datetime

def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def get_title(age):
    if age < 30:
        return "Kakak"
    else:
        return "Bapak"

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan Tanggal Lahir (dd-mm-yyyy)")
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()


try:
    birth_date = datetime.datetime.strptime(args.tanggallahir, "%d-%m-%Y").date()
    age = calculate_age(birth_date)
    title = get_title(age)
    print("Terima kasih telah menggunakan panggildicoding.py, " + title + " " + args.nama)
    output_message = "Halo, ini merupakan sebuah output dari panggildicoding.py" if args.output else ""
    print(output_message)
except ValueError:
    print("Format tanggal lahir tidak valid. Gunakan format dd-mm-yyyy.")