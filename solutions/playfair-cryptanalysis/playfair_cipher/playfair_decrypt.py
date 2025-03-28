"""Program python untuk dekripsi playfair cipher text"""

ROW_N = 5
COL_N = 5

def decrypt_playfair(cipher_t, k_matrix):
    """fungsi untuk dekripsi playfair cipher jika key matrix diketahui"""
    key_map = {k_matrix[row][col]: (row, col) for row in range(ROW_N) for col in range(COL_N)}
    decrypted = ""

    for i in range(0, len(cipher_t), 2):
        a, b = cipher_t[i], cipher_t[i + 1]
        r1, c1 = key_map[a]
        r2, c2 = key_map[b]

        if r1 == r2:
            decrypted += k_matrix[r1][(c1 - 1) % ROW_N] + k_matrix[r2][(c2 - 1) % COL_N]
        elif c1 == c2:
            decrypted += k_matrix[(r1 - 1) % ROW_N][c1] + k_matrix[(r2 - 1) % COL_N][c2]
        else:
            decrypted += k_matrix[r1][c2] + k_matrix[r2][c1]

    return decrypted

if __name__ == "__main__":
    # Key matrix 5 x 5
    key_matrix = [
        ["A", "S", "R", "I", "G"],
        ["K", "L", "C", "N", "T"],
        ["H", "B", "D", "E", "F"],
        ["U", "M", "O", "P", "Q"],
        ["Z", "V", "W", "X", "Y"]
    ]

    f = open("../cipher.txt", "r", encoding="utf-8")

    ciphertext = f.read()
    plaintext = decrypt_playfair(ciphertext, key_matrix)
    print("Plaintext hasil dekripsi Playfair Cipher:", plaintext)

    f.close()