import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download NLTK data jika belum ada
nltk.download()

# Database jurusan (contoh sederhana)
jurusan = {
    "informatika": {
        "deskripsi": "Belajar tentang komputer dan sistem informasi.",
        "mata_kuliah": "Pemrograman, Algoritma, Struktur Data",
        "prospek_kerja": "Pengembang perangkat lunak, data scientist"
    },
    "psikologi": {
        "deskripsi": "Belajar tentang pikiran dan perilaku manusia.",
        "mata_kuliah": "Psikologi Umum, Psikologi Pendidikan",
        "prospek_kerja": "Psikolog, konselor"
    }
}

# Kata kunci
kata_kunci = {
    "minat": ["suka", "gemar", "tertarik"],
    "bakat": ["jago", "berbakat", "potensi"],
    "mata_kuliah": ["pelajaran", "kuliah", "studi"],
    "kerja": ["kerja", "karir", "pekerjaan"]
}

# Fungsi untuk memproses pertanyaan
def proses_pertanyaan(pertanyaan):
    # Tokenisasi
    tokens = word_tokenize(pertanyaan)
    
    # Stemming (mengubah kata menjadi bentuk dasarnya)
    stemmer = PorterStemmer()
    tokens_stemmed = [stemmer.stem(token) for token in tokens]

    # Mencari kata kunci
    for kata in tokens_stemmed:
        for kunci, nilai in kata_kunci.items():
            if kata in nilai:
                return kunci

    return None

# Fungsi untuk memberikan respons
def berikan_respons(pertanyaan, jurusan_pilihan):
    kunci = proses_pertanyaan(pertanyaan)
    if kunci == "minat":
        return "Jika Anda tertarik dengan {}, mungkin jurusan {} cocok untuk Anda.".format(jurusan_pilihan, jurusan_pilihan)
    elif kunci == "bakat":
        return "Jika Anda memiliki bakat di bidang {}, Anda bisa mempertimbangkan jurusan {}.".format(jurusan_pilihan, jurusan_pilihan)
    elif kunci == "mata_kuliah":
        return "Jurusan {} mencakup mata kuliah seperti {}.".format(jurusan_pilihan, jurusan[jurusan_pilihan]["mata_kuliah"])
    elif kunci == "kerja":
        return "Prospek kerja untuk jurusan {} adalah: {}.".format(jurusan_pilihan, jurusan[jurusan_pilihan]["prospek_kerja"])
    else:
        return "Maaf, saya tidak mengerti pertanyaan Anda. Silakan coba lagi."

# Contoh penggunaan
pertanyaan = "Saya suka belajar tentang komputer, jurusan apa yang cocok untuk saya?"
jurusan_pilihan = "informatika"

respons = berikan_respons(pertanyaan, jurusan_pilihan)
print(respons)
