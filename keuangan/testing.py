import unittest
import os
from .processing import Laporan, Transaksi
from .validasi import cek_data, DataTidakValidError
from .fileio import baca_transaksi

class TestKeuangan(unittest.TestCase):
    def test_total_pengeluaran(self):
        # 1. Menguji logika penjumlahan
        t1 = Transaksi("2026-10-01", "makan", 10000)
        t2 = Transaksi("2026-10-02", "transport", 5000)
        laporan = Laporan([t1, t2])
        self.assertEqual(laporan.hitung_total(), 15000)

    def test_validasi_nominal_negatif(self):
        # 2. Menguji exception jika nominal minus
        with self.assertRaises(DataTidakValidError):
            cek_data("2026-10-01", "makan", -5000)

    def test_validasi_field_kosong(self):
        # 3. Menguji exception jika string kosong
        with self.assertRaises(DataTidakValidError):
            cek_data("2026-10-01", "", 10000)

    def test_file_tidak_ditemukan(self):
        # 4. Memastikan error tertangkap dan hanya mengembalikan list kosong
        hasil = baca_transaksi("file_asal.txt")
        self.assertEqual(hasil, [])
        
    def test_baris_rusak_dilewati(self):
        # 5. Membuat file txt sementara, mengisinya dengan data salah ('abc'), lalu mengeceknya
        nama_file_test = "test_data.txt"
        with open(nama_file_test, "w") as f:
            f.write("2026-10-01;makan;10000\n2026-10-02;jajan;abc\n")
        
        hasil = baca_transaksi(nama_file_test)
        os.remove(nama_file_test) # Hapus lagi filenya setelah selesai dibaca
        
        # 'abc' akan dilewati sehingga panjang list yang valid hanya 1
        self.assertEqual(len(hasil), 1)

if __name__ == '__main__':
    unittest.main()

# Run menggunakan python -m unittest keuangan.testing -v