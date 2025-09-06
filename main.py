# =========================
# main.py
# Program Konversi Suhu Interaktif
# =========================
from utils import konversi_suhu

def menu():
    print("\n=== Program Konversi Suhu ===")
    print("1. Celsius → Fahrenheit")
    print("2. Celsius → Kelvin")
    print("3. Fahrenheit → Celsius")
    print("4. Fahrenheit → Kelvin")
    print("5. Kelvin → Celsius")
    print("6. Kelvin → Fahrenheit")
    print("0. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu (0-6): ")

    if pilihan == "0":
        print("Terima kasih, program selesai.")
        break

    try:
        nilai = float(input("Masukkan nilai suhu: "))
    except ValueError:
        print("❌ Error: nilai suhu harus berupa angka.")
        continue

    if pilihan == "1":
        hasil = konversi_suhu(nilai, "c", "f")
        print(f"{nilai} °C = {hasil:.2f} °F")
    elif pilihan == "2":
        hasil = konversi_suhu(nilai, "c", "k")
        print(f"{nilai} °C = {hasil:.2f} K")
    elif pilihan == "3":
        hasil = konversi_suhu(nilai, "f", "c")
        print(f"{nilai} °F = {hasil:.2f} °C")
    elif pilihan == "4":
        hasil = konversi_suhu(nilai, "f", "k")
        print(f"{nilai} °F = {hasil:.2f} K")
    elif pilihan == "5":
        hasil = konversi_suhu(nilai, "k", "c")
        print(f"{nilai} K = {hasil:.2f} °C")
    elif pilihan == "6":
        hasil = konversi_suhu(nilai, "k", "f")
        print(f"{nilai} K = {hasil:.2f} °F")
    else:
        print("❌ Pilihan tidak valid, coba lagi.")
