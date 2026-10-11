from .processing import Transaksi
from .validasi import cek_data, DataTidakValidError

def buat_file_baru(nama_file):
    # Mode 'x': Membuat file pertama kali. Mencegah data lama hangus.
    try:
        with open(nama_file, 'x') as file:
            # Data awal sengaja disisipkan 2 data yang formatnya salah untuk uji coba try/except
            file.write("2026-10-01;makan;20000\n")
            file.write("2026-10-01;transport;15000\n")
            file.write("2026-10-02;belanja;abc\n") # Sengaja salah tipe
            file.write("2026-10-03;makan\n")       # Sengaja salah format
        print(f"File '{nama_file}' berhasil dibuat.")
    except FileExistsError:
        print(f"File '{nama_file}' sudah ada, sistem tidak menimpanya.")

def tambah_transaksi(nama_file, teks_transaksi):
    # Mode 'a': Menambah data di baris paling bawah tanpa menghapus data lama
    with open(nama_file, 'a') as file:
        file.write(teks_transaksi)

def baca_transaksi(nama_file):
    daftar = []
    try:
        # Mode 'r': Membaca data baris demi baris agar hemat memori
        with open(nama_file, 'r') as file:
            for baris in file:
                try:
                    # Menghapus enter di ujung teks dan memecahnya
                    tgl, kat, nom = baris.strip().split(";")
                    nominal_angka = int(nom) # Dapat memicu ValueError jika berisi huruf
                    
                    # Validasi (Dapat memicu DataTidakValidError)
                    cek_data(tgl, kat, nominal_angka)
                    
                    transaksi_baru = Transaksi(tgl, kat, nominal_angka)
                    daftar.append(transaksi_baru)
                    
                except ValueError:
                    print(f"Baris dilewati (bukan angka): {baris.strip()}")
                except DataTidakValidError as e:
                    print(f"Baris dilewati ({e}): {baris.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan! Silakan buat file dulu.")
    
    return daftar

def tulis_laporan(nama_file, teks_laporan):
    # Mode 'w': Menulis ulang file untuk laporan terbaru
    with open(nama_file, 'w') as file:
        file.write(teks_laporan)


