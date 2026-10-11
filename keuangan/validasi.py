class DataTidakValidError(Exception):
    """Exception buatan untuk menangkap data pengeluaran yang salah."""
    pass

def cek_data(tanggal, kategori, nominal):
    # Mengecek apakah ada kolom yang kosong
    if tanggal == "" or kategori == "":
        raise DataTidakValidError("Tanggal atau kategori tidak boleh kosong.")
    
    # Mengecek apakah angka minus
    if nominal < 0:
        raise DataTidakValidError("Nominal pengeluaran tidak boleh negatif.")

# Blok if __name__ untuk menguji file ini secara lokal
if __name__ == '__main__':
    print("-Uji coba fungsi validasi-")
    try:
        cek_data("2026-10-10", "Makan", -5000)
    except DataTidakValidError as error:
        print(f"Error berhasil ditangkap: {error}")
