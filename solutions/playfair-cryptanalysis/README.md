# Kriptanalisis Playfair Cipher

Cyber Fox menemukan dokumen lain yang tampak tidak sesuai dengan pola Vigenère. Struktur karakter yang dihasilkan tidak sepenuhnya masuk akal. Ini membuatnya curiga bahwa sebagian dokumen mungkin telah dienkripsi menggunakan metode lain. Setelah meneliti lebih lanjut, Cyber Fox menyadari bahwa bagian tersebut dienkripsi menggunakan Playfair cipher, metode enkripsi yang menggunakan tabel 5x5 untuk mengenkripsi pasangan huruf.

Untuk membongkar Playfair cipher, Cyber Fox mulai mengidentifikasi digram (pasangan huruf) yang sering muncul dalam ciphertext. Dengan membandingkan frekuensi ini terhadap distribusi normal dalam bahasa yang digunakan, ia mulai menebak isi dari matriks kunci Playfair. Langkah demi langkah, ia membangun kembali tabel kunci yang digunakan untuk mengenkripsi pesan. Mari bantu Cyber Fox menuntaskan misinya!

## Diketahui

- Cipher: Playfair Cipher
- Dimensi tabel Key: 5x5
- Bahasa: Inggris
- Tipe n-gram: Digram
- Ciphertext:
  ```txt
  DCXQCQAIIUFZGRBIIBTKGSTBWCOIQCDNNGTINEDQSOGKRPENTNPOQMNGTIGVGLBPRSCEMNGZRSXSKGCSMCPNTKBFHRSNVTSXBIQDESNVNSPCRMEQDPMNDXWCCBXREFFVIBKOIGTIDMKFGLWCFEIKFCISLIPSNYNFEWHRKGHQCESUPEKGCKPOIKVGDNOAGNXQCWCQDWBLUIGCRNMKSITVCGIKIMWCKCGZDIIBKOIGFGKCRLGWQNQRISUERNNFKDENUMBIPESHNBCWHMGLPEDCXQNGPCRKCWIVLSSIRPMAIUMNRNGKRPLIDUXDXBCOBIXNNFGNRGOQWCKGTNDNGWQNQRISUEWGBPSGLIDGSASNPNLGIBKOIGFGKRLEDNPOMNFNBNZQCEDIPSEPEDZGRGTINBEFRGITBTRZWCOIQRISPVPSTIDICWGCISERNGPCSKRMQFZRIDNFGLNESQFNDUBRAMKDSRPKGNNFGLNEASIDNEAMEYEGNRPEFQWCEFNFNKNERTGWQNQRISUERNZMCTDISHSNGNNPRGLINFRHDCXQCQAIIUEALRDNOAGNXGIBGLSHNSABFEKFCWQADAGAWCPMLVGKBFUSNGKRNMCWQDRSCEDQSOSKIKSKVGGRCQPEAMIDDWOQNSIKNDXRKFBIIBTKGSBLDNOAGNXQIGTNNXNBRMQFPEIDTVNERQCIHIRMKIMBHIIVAMOQNGPCRMEPQDKFPIHISCXFTNGWQNRPLPFNDUBRKFGKSPOIMWFEMQPCRGOQNBAMMLNGKQNGPCNRUEDIRGGLBFMNGZHGGINRUEDINECGWOOKFENEKFFNDKPEKQGWPKNSNHOPCPSKUESHFNRNNRUEDIIMKSGQSGIDTNGWQNIMSGIRQDNBNYNFIRMANEASZNFXGMZKIDUSNATIDGFPPHTNZGKITVRGLVWCFEGEEGKOCKZDSNPNCYSRPCNDDWLIREDIFESRGAENEGKRTKRHZSTNBPPELQWODITNGWQNIKSKVGGRNFKDENUMBIKRLEIDKHMNGZHGGIPEDCXQNGPCFVPIMNPRNGTIERAISUDGFPPHTNWFGRCGSEQKRPLIIKOCDNPCGLAONKNETFBFNHVGUMSIFNEAAMCEDIRLWCBIGHPKHRPBTKSKDWTNPXNGTNPCNFOQWCSIWTGWQNQRISUEGFAOBIDNOAGNWFPXPEBRCPCQTCWQLIDNIDTWHMKGBLPWPCGLCWTIUSKFBPGKRNSKOINENRMNBIIKODPOQMKGNGPCSKNEHFSRSESNGNZY
  ```

## Steps

1. Frekuensi analisis digram
2. Perbandingan hasil frekuensi analisis terhadap distribusi normal
3. Menebak isi matriks kunci Playfair
4. Langkah demi langkah membangun kembali tabel kunci yang digunakan untuk enkripsi pesan

### Notes

- Dalam proses pembuatan ciphertext, seluruh karakter dalam plainteks diubah menjadi huruf kapital. 
- Enkripsi hanya diterapkan pada karakter alfabet (A–Z), sementara karakter nonalfabet seperti angka, spasi, koma, titik, dan simbol lainnya diabaikan dan tidak disertakan dalam hasil enkripsi.
- Diperbolehkan menggunakan pendekatan Brute Force atau Exhaustive Key Search, tetapi hanya sebagai pembanding dengan metode kriptanalisis.

## Solve

1. Frekuensi analisis diagram menggunakan program Python [freq_analysis.py](./freq_analysis/freq_analysis.py) untuk mendapatkan top 20 digram dalam bahasa inggris.

    Hasilnya dapat dilihat pada [freq_analysis/out.txt](./freq_analysis/out.txt)

2. Perbandingan hasil frekuensi analisis terhadap distribusi normal menggunakan program Python ...

3. Menebak isi matriks kunci Playfair

4. Langkah demi langkah membangun kembali tabel kunci yang digunakan untuk enkripsi pesan

## Output

- Tabel frekuensi kemunculan pasangan huruf (digram) dalam bahasa Inggris

  Top 100 bigrams dalam bahasa Inggris:

  ![EN Digrams](assets/en_digrams.png)

  Sumber: [dcode.fr/bigrams](https://www.dcode.fr/bigrams)

- Tabel frekuensi kemunculan pasangan huruf (digram) dalam ciphertext

  [Output hasil analisis digram (EN)](./freq_analysis/out.txt)

- Dokumentasi langkah-langkah analisis dalam pemecahan cipher

  1. Diketahui bahwa bahasa yang digunakan adalah bahasa Inggris dan enkripsi Playfair cipher berbasis bigram

  2. Gunakan program python [freq_analysis.py](freq_analysis/freq_analysis.py) untuk menemukan bigram yang paling umum digunakan

      - Hasilnya dapat dilihat pada [freq_analysis/out.txt](./freq_analysis/out.txt)

  3. Setelah mengetahui bigram paling umum, lakukan analisis frekuensi sebagai berikut:

      i. Bandingkan dengan Frekuensi Digram Bahasa Inggris
      
        - Dalam bahasa Inggris, digram umum seperti TH, HE, IN, ER, AN, RE sering muncul (gunakan tabel digram paling sering muncul di atas)
        - Cocokkan pola digram ciphertext dengan statistik frekuensi bahasa Inggris.

      ii. Identifikasi Pola dalam Ciphertext
      
        - Perhatikan aturan Playfair:

          Satu baris → huruf bergeser ke kiri

          Satu kolom → huruf bergeser ke atas

          Bentuk persegi panjang → huruf bertukar posisi secara diagonal

          Gunakan pola ini untuk menebak kemungkinan huruf asli.

      iii. Tebak dan Rekonstruksi Kunci Playfair (5×5 Grid)
      
        - Gunakan hasil analisis digram untuk menebak sebagian isi matriks kunci.
        - Coba susun huruf yang paling sering muncul sesuai pola grid 5×5.
        - Ingat bahwa Playfair menghilangkan huruf J atau menggabungkannya dengan I.

      iv. Uji Dekripsi dengan Kunci Sementara
      
        - Gunakan kunci yang sudah direkonstruksi untuk mencoba mendekripsi ciphertext.
        - Jika hasilnya belum masuk akal, perbaiki tebakan berdasarkan pola yang muncul.
        - Untuk pengujian ini, saya menggunakan program Python custom yang telah saya buat: [playfair_decrypt.py](./playfair_cipher/playfair_decrypt.py)

      v. Evaluasi dan Koreksi
        
        - Jika plaintext masih tidak masuk akal, ulangi proses dengan memperbaiki tebakan kunci atau menggunakan pendekatan statistik lain.

- Plaintext hasil dekripsi

  ```txt
  CRYPTOGRAPHYISESSENTIALFORPROTECTINGINFORMATIONINCOMPUTINGSYSTEMSANDPLAYSAVITALROLEINTHEDAILYLIVESOFBILXLIONSOFPEOPLEWORLDWIDEBYSECURINGBOTHSTOREDANDTRANSMITXTEDXDATAFUNDAMENTALTOMANYSECURITYPROTOCOLSPARTICULARLYTRANSPORTLAYERSECURITYTLSCRYPTOGRAPHICTECHNIQUESENABLEROBUSTENCRYPTIONACROSXSVARIOUSAPPLICATIONSHOWEVERDESPITEITSIMPORTANCECRYPTOGRAPHYREMAINSFRAGILEITSSECURITYCANBECOMPLETELYUNDERMINEDBYASINGLEDESIGNFLAWORPROGRAMXMINGERRORTRADITIONALSOFTWARETESTINGMETHODSSUCHASUNITTESTINGAREINSUFXFICIENTFORDETECTINGCRYPTOGRAPHICVULNERABILITIESINSTEADCRYPTOGRAPHICSECURITYISESTABLISHEDTHROUGHRIGOROUSMATHEMATICALPROOFSANDFORMALANALYSISTOENSURECOMPLIANCEWITHESSENTIALSECURITYPRINCIPLESOFTENRELYINGONREASONABLEASXSUMPTIONSONEOFTHEXEARLYENCRYPTIONMETHODSTHATIMPROVEDUPONSIMPLESUBSTITUTIONCIPHERSISTHEPLAYFAIRCIPHERINTRODUCEDINTHETHCENTURYUNLIKEMONOALPHABETICCIPHERSPLAYFAIRENCRYPTSPAIRSOFLETXTERSUSINGAXKEYSQUAREMAKINGFREQUENCYANALYSISMOREDIFFICULTWHILEITWASONCECONSIDEREDASIGNIFICANTADVANCEMENTMODERNCRYPTANALYSISTECHNIQUESCANBREAKPLAYFAIRENCRYPTIONBYEXPLOITINGDIGRAMFREQUENCYDISTRIBUTIONSANDRECONSTRUCTINGTHEKEYSQUARETHISUNDERSCORESAFUNDAMENTALCONCEPTINCONTEMPORARYCRYPTOGRAPHYTRUESECURITYDEPENDSNOTONLYONSECRECYBUTALSOXONSTRONGMATHEMATICALPRINCIPLESANDCOMPUTATIONALINFEASIBILITYX
  ```

- Kunci enkripsi

  ```txt
  A S R I G
  K L C N T
  H B D E F
  U M O P Q
  Z V W X Y
  ```

- Kode Python yang digunakan

  - Untuk frekuensi analisis: [req_analysis.py](./freq_analysis/freq_analysis.py)
  - Untuk percobaan dekripsi key matrix: [playfair_decrypt.py](./playfair_cipher/playfair_decrypt.py)

- Waktu kriptanalisis yang dibutuhkan

  Sekitar 6 jam

- Perbandingan dengan pendekatan Brute Force / Exhaustive Key Attack (optional)

  [tidak dilakukan]