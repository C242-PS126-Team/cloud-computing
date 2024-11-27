Dokumentasi ini berisi penjelasan mengenai rancangan sistem dari tim Cloud Computing pada project Capstone. Dokumentasi mencakup arsitektur, service-service yang digunakan, serta cara menjalankan sistem secara keseluruhan.

## Daftar Service

### 1. API Service
Service ini menangani request API dari client. Dibuat menggunakan FastAPI framework.

**Endpoint yang tersedia:**
- `/` - Endpoint default yang menampilkan pesan "Hello, World!"
- `/api/` - Endpoint untuk mengakses API dengan pesan "Hello, this page for api!"

[Dokumentasi lengkap API Service](api-service/readme.md)

### 2. ML Service (Coming Soon)
Service yang akan menangani proses machine learning dan prediksi.

## Arsitektur Sistem

Sistem ini menggunakan arsitektur microservice dimana setiap service berjalan secara independen dan berkomunikasi melalui API.

## Cara Menjalankan

Setiap service memiliki dokumentasi dan cara menjalankan masing-masing. Silakan merujuk ke dokumentasi tiap service untuk detail lebih lanjut.

## Kontribusi

Untuk berkontribusi pada project ini, silakan buat pull request dengan deskripsi perubahan yang jelas.



## Lisensi

Project ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail lebih lanjut.
