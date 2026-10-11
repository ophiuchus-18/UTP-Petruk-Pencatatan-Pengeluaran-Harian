from keuangan import fileio, processing

def main():
    print("=PROGRAM PENCATATAN PENGELUARAN=")
    FILE_DATA = "pengeluaran.txt"
    FILE_LAPORAN = "laporan.txt"
    
    # 1. Membuat file data (Menggunakan Mode 'x' di dalam fileio)
    fileio.buat_file_baru(FILE_DATA)
    
    # 2. Menerapkan Keyword Argument saat memanggil fungsi dan **kwargs di background
    print("\nMenambahkan transaksi baru...")
    data_baru = processing.buat_record(tanggal="2026-10-05", kategori="hiburan", nominal=50000)
    
    transaksi_baru = processing.Transaksi(data_baru["tanggal"], data_baru["kategori"], data_baru["nominal"])
    # Menambah data (Menggunakan Mode 'a' di dalam fileio)
    fileio.tambah_transaksi(FILE_DATA, transaksi_baru.ke_teks())
    
    # 3. Membaca data iteratif (Menggunakan Mode 'r' di dalam fileio)
    print("\nMembaca seluruh data (baris error akan dilewati):")
    daftar_transaksi = fileio.baca_transaksi(FILE_DATA)
    
    # 4. Eksekusi Analisis
    if daftar_transaksi:
        laporan = processing.Laporan(daftar_transaksi)
        
        teks_laporan = f"LAPORAN PENGELUARAN\n"
        teks_laporan += f"Total: Rp{laporan.hitung_total()}\n"
        
        terbesar = laporan.pengeluaran_terbesar()
        teks_laporan += f"Terbesar: {terbesar.tampilkan_info()}\n"
        
        teks_laporan += "\nRincian Kategori:\n"
        for kat, jml in laporan.total_per_kategori().items():
            teks_laporan += f"- {kat}: Rp{jml}\n"
            
        # 5. Menulis hasil laporan (Menggunakan Mode 'w' di dalam fileio)
        fileio.tulis_laporan(FILE_LAPORAN, teks_laporan)
        print(f"\nAnalisis selesai. Hasil disimpan di '{FILE_LAPORAN}'")
        
        # Tampilkan laporan ke konsol
        print("\n--- ISI LAPORAN ---")
        with open(FILE_LAPORAN, 'r') as f:
            print(f.read())
    else:
        print("Tidak ada data yang valid untuk diproses.")

if __name__ == '__main__':
    main()
    