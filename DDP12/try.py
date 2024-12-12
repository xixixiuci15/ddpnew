class Tugas:
    def __init__(self, nama, deadline, status):
        self.nama = nama
        self.deadline = deadline
        self.status = status

    def tampilkan_tugas(self):
        print(f"Nama Tugas: {self.nama}")
        print(f"Deadline: {self.deadline}")
        print(f"Status: {self.status}")

class AplikasiTugas:
    def __init__(self):
        self.daftar_tugas = []

    def tambah_tugas(self, nama, deadline, status):
        tugas = Tugas(nama, deadline, status)
        self.daftar_tugas.append(tugas)

    def tampilkan_daftar_tugas(self):
        for i, tugas in enumerate(self.daftar_tugas, start=1):
            print(f"Tugas {i}:")
            tugas.tampilkan_tugas()
            print()

    def ubah_status_tugas(self, nama_tugas, status_baru):
        for tugas in self.daftar_tugas:
            if tugas.nama == nama_tugas:
                tugas.status = status_baru
                print(f"Status tugas '{nama_tugas}' berhasil diubah menjadi '{status_baru}'")
                return
        print(f"Tugas '{nama_tugas}' tidak ditemukan")

def main():
    aplikasi = AplikasiTugas()

    while True:
        print("Aplikasi Tugas Sederhana")
        print("1. Tambah Tugas")
        print("2. Tampilkan Daftar Tugas")
        print("3. Ubah Status Tugas")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama tugas: ")
            deadline = input("Masukkan deadline tugas: ")
            status = input("Masukkan status tugas: ")
            aplikasi.tambah_tugas(nama, deadline, status)
        elif pilihan == "2":
            aplikasi.tampilkan_daftar_tugas()
        elif pilihan == "3":
            nama_tugas = input("Masukkan nama tugas yang ingin diubah statusnya: ")
            status_baru = input("Masukkan status baru: ")
            aplikasi.ubah_status_tugas(nama_tugas, status_baru)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi tugas sederhana!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()