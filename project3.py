
def wordsCount(kalimat):
    # Memisahkan kata-kata menggunakan split()
    kata_kunci = kalimat.split()

    # Menghitung jumlah kata
    jumlah_kata = len(kata_kunci)

    return jumlah_kata

# Meminta pengguna untuk memasukkan kalimat
user = input("Masukkan kalimat: ")

# Memanggil fungsi wordsCount dan menampilkan hasil
jumlah_kata = wordsCount(user)
print(f"Jumlah kata: {jumlah_kata}")
