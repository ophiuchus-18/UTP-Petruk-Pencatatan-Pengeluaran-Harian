def jumlahkan_semua(*args):
    # Menggunakan *args untuk menjumlahkan banyak data angka sekaligus
    total = 0
    for angka in args:
        total += angka
    return total

def buat_record(**kwargs):
    # Menggunakan **kwargs untuk menerima data dinamis dan mengubahnya jadi dictionary
    return kwargs

class Transaksi:
    def __init__(self, tanggal, kategori, nominal):
        self.tanggal = tanggal
        self.kategori = kategori
        self.nominal = nominal

    def ke_teks(self):
        # Mengubah data objek menjadi teks untuk disimpan ke txt
        return f"{self.tanggal};{self.kategori};{self.nominal}\n"
        
    def tampilkan_info(self):
        return f"{self.tanggal} - {self.kategori}: Rp{self.nominal}"

class Laporan:
    def __init__(self, daftar_transaksi):
        self.daftar = daftar_transaksi

    def hitung_total(self):
        # Menyiapkan list nominal untuk dijumlahkan
        list_nominal = []
        for transaksi in self.daftar:
            list_nominal.append(transaksi.nominal)
        
        # Memanggil fungsi *args
        total_pengeluaran = jumlahkan_semua(*list_nominal)
        
        # Menggunakan assert untuk memastikan total hitungan masuk akal
        assert total_pengeluaran >= 0, "Total pengeluaran tidak mungkin negatif"
        return total_pengeluaran

    def pengeluaran_terbesar(self):
        # Menggunakan fungsi lambda untuk mencari nominal paling besar
        if not self.daftar:
            return None
        return max(self.daftar, key=lambda t: t.nominal)
    
    def total_per_kategori(self):
        hasil = {}
        for transaksi in self.daftar:
            if transaksi.kategori in hasil:
                hasil[transaksi.kategori] += transaksi.nominal
            else:
                hasil[transaksi.kategori] = transaksi.nominal
        return hasil
