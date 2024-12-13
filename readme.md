# Dokumentasi Cloud Computing Team

Dokumentasi ini berisi penjelasan mengenai rancangan sistem dari tim Cloud Computing pada project Capstone. Dokumentasi mencakup arsitektur, service-service yang digunakan, serta cara menjalankan sistem secara keseluruhan.

## Daftar Service

### 1. API Service
Service ini menangani request API dari client. Dibuat menggunakan FastAPI framework untuk Python.

**Dokumentasi API Lengkap:**
Untuk dokumentasi API yang lebih lengkap dan interaktif, silakan kunjungi:
https://api.truecolor.my.id/docs

**Endpoint yang tersedia:**

1. `/api/`
- Method: GET
- Deskripsi: Endpoint default yang menampilkan pesan selamat datang
- Response: JSON dengan pesan welcome

2. `/api/predicted`
- Method: POST
- Deskripsi: Endpoint untuk memprediksi warna dari gambar yang diunggah
- Content-Type: multipart/form-data
- Parameter:
  - file: File gambar yang akan diprediksi (required)
  - format: jpg, png, jpeg
  - max size: 10MB
- Response:
  - 200: Prediksi berhasil
  - 400: File tidak ditemukan atau format tidak valid
  - 413: Ukuran file terlalu besar (max 10MB)
  - 500: Internal server error

## Arsitektur Sistem

<img src="assets/architechture.svg" alt="Arsitektur Sistem" title="Arsitektur Sistem">

Sistem ini menggunakan arsitektur microservice dimana setiap service berjalan secara independen dan berkomunikasi melalui API.

## Cara Menjalankan

Setiap service memiliki dokumentasi dan cara menjalankan masing-masing. Silakan merujuk ke dokumentasi tiap service untuk detail lebih lanjut.

## Kontribusi

Untuk berkontribusi pada project ini, silakan buat pull request dengan deskripsi perubahan yang jelas.

### Contributors
<div align="center">
  <img src="assets/contributors.png" alt="Contributors" title="Contributors">

   [Hardianto](https://github.com/hardianto01)
   [Petra Slent](https://github.com/petraslent)
</div>

## Lisensi

Project ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail lebih lanjut.