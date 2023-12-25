from PyPDF2 import PdfWriter, PdfReader

# Buka file PdfReader
file_path = r"C:\Users\Mahesa Agung Sejati\Pictures\SKD\TestSKD.pdf"
file = PdfReader(file_path)

# Masukkan password enkripsi
password = "mahesa"

# Buat objek PdfWriter untuk menyimpan file yang sudah dienkripsi
out = PdfWriter()

# Program membaca setiap halaman file sesuai halaman yang diidentifikasi
for idx in range(len(file.pages)):
    out.add_page(file.pages[idx])

# Enkripsi seluruh file
out.encrypt(password)

# Buka file enkripsi "TestSKDbaru.pdf"
output_path = r"C:\Users\Mahesa Agung Sejati\Pictures\SKD\TestSKDbaru.pdf"
with open(output_path, "wb") as f:
    # Simpan pdf
    out.write(f)

# Pastikan untuk menutup file yang sedang dienkripsi
file.stream.close()
