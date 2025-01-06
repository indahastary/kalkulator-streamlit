def kalkulator():
    print("Selamat datang di kalkulator sederhana!")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan in ['1', '2', '3', '4']:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == '1':
                print(f"Hasil: {angka1} + {angka2} = {angka1 + angka2}")
            elif pilihan == '2':
                print(f"Hasil: {angka1} - {angka2} = {angka1 - angka2}")
            elif pilihan == '3':
                print(f"Hasil: {angka1} * {angka2} = {angka1 * angka2}")
            elif pilihan == '4':
                if angka2 != 0:
                    print(f"Hasil: {angka1} / {angka2} = {angka1 / angka2}")
                else:
                    print("Error: Pembagian dengan nol tidak diperbolehkan!")
        except ValueError:
            print("Error: Masukkan angka yang valid!")
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

    ulang = input("Apakah Anda ingin menghitung lagi? (y/n): ")
    if ulang.lower() == 'y':
        kalkulator()
    else:
        print("Terima kasih telah menggunakan kalkulator ini!")

if __name__ == "__main__":
    kalkulator()