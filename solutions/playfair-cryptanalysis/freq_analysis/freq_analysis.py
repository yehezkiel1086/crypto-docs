"""Modul frekuensi analisis kriptografi"""
from collections import Counter
import re

def digram_analysis(cipher_txt) -> list[tuple[str, float]]:
    """Fungsi untuk analisis digram"""
    # hapus karakter-karakter non alphabet dan jadikan uppercase
    cipher_txt = re.sub(r'[^A-Za-z]', '', cipher_txt).upper()

    # ekstraksi digram
    digrams = [cipher_txt[i:i+2] for i in range(len(cipher_txt)-1)]

    # hitung total digram
    digram_counts = Counter(digrams)
    total_digrams = sum(digram_counts.values())

    # hitung persentase frekuensi
    digram_frequencies = {digram: (count / total_digrams) * 100 for digram, count in digram_counts.items()}

    # urutkan frekuensi dari paling besar ke kecil
    res = sorted(digram_frequencies.items(), key=lambda x: x[1], reverse=True)

    return res

if __name__ == "__main__":
    f = open("../cipher.txt", "r", encoding="utf-8")
    r = open("out.txt", "w+", encoding="utf-8")
    cipher = f.read()

    digram_freq = digram_analysis(cipher)

    # Tampilkan top 20 digram
    print("Digram analisis frekuensi:")
    for digram, freq in digram_freq[:20]:
        st = f"{digram}: {freq:.2f}%\n"
        print(st, end="")
        r.write(st)

    f.close()
    r.close()
