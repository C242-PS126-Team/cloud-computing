Dokumentasi ini berisi penjelasan mengenai rancangan sistem dari tim Cloud Computing pada project Capstone. Dokumentasi mencakup arsitektur, service-service yang digunakan, serta cara menjalankan sistem secara keseluruhan.

## Daftar Service

### 1. API Service
Service ini menangani request API dari client. Dibuat menggunakan FastAPI framework.

**Endpoint yang tersedia:**
- `/` - Endpoint default yang menampilkan pesan "Hello, World!"
- `/api/` - Endpoint untuk mengakses API dengan pesan "Hello, this page for api!"
- `/api/generate-plate` - Endpoint untuk menghasilkan gambar berdasarkan parameter yang diberikan.

**Contoh Body Request untuk `/api/generate-plate`:**
```json
{
    "radioSubmitway": "numberoption",
    "numberselector": 69,
    "background_colorslider": "#ffffff",
    "iterationslider": 30000,
    "min_radius": 4,
    "max_radius": 15,
    "use_shift": "on",
    "shiftslider": 30,
    "use_light": "on",
    "lightschwiftslider": 120,
    "use_blackwhite": "on",
    "first_colorslider": "#89af23",
    "second_colorslider": "#db5e2e",
    "use_grad": "on",
    "gradientshiftslider": 25,
    "doCrop": "on"
}
```

**Penjelasan untuk `radioSubmitway` dan `numberselector`:**
- `radioSubmitway` adalah opsi untuk memilih jenis input. Jika `radioSubmitway` diatur ke "numberoption", maka `numberselector` akan digunakan untuk menentukan nomor plat. Jika `radioSubmitway` diatur ke "fileoption", maka `numberselector` akan digunakan untuk mengunggah file gambar plat.

[Dokumentasi lengkap API Service](api-service/readme.md)

### 2. ML Service (Coming Soon)
Service yang akan menangani proses machine learning dan prediksi.

## Arsitektur Sistem

<img src="assets/architechture.svg" alt="Arsitektur Sistem" title="Arsitektur Sistem">

Sistem ini menggunakan arsitektur microservice dimana setiap service berjalan secara independen dan berkomunikasi melalui API.

## Cara Menjalankan

Setiap service memiliki dokumentasi dan cara menjalankan masing-masing. Silakan merujuk ke dokumentasi tiap service untuk detail lebih lanjut.

## Kontribusi

Untuk berkontribusi pada project ini, silakan buat pull request dengan deskripsi perubahan yang jelas.

## Lisensi

Project ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail lebih lanjut.
