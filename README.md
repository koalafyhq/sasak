<div align="center">
  <h1>sasak</h1>
  <p>Sundanese — Jembatan</p>
  <img src="https://i.imgur.com/9IKDUaD.jpg" alt="Jembatan">
</div>

sasak adalah aplikasi Flask yang pada dasarnya hanyalah *proxy* untuk memuat gambar, sangat ter-inspirasi dari
[camo](https://github.com/atmos/camo) nya GitHub yang mana ditulis menggunakan CoffeeScript.

Aplikasi ini hanya memiliki 1 *endpoint*: `GET /<digest>/<url_hex>`, dimana:
- `digest` adalah *signature* dari url gambar yang ingin dimuat, nilai diambil dari
  `hmac_sha1(secret, url)`
- `url_hex` adalah url gambar yang sudah di *encode* ke format hex

Logika lain (termasuk tambahan keamanan) sangat bergantung kepada konfigurasi yang anda
lakukan di level *load balancer*, jadi, pastikan kamu sudah mengatur konfigurasi yang benar
seperti terkait kompresi, kontrol tembolok, dsb

## Instalasi

Unduh dependensi yang digunakan dengan menjalankan perintah berikut:

```bash
pip3 install -r requirements.txt
```

Pastikan menggunakan *virtual environment* untuk tetap menjaga dependensi tidak tercampur dan berantakan 
dengan lingkungan global (OS)

## Penggunaan

Aplikasi ini adalah bagian dari aplikasi "bookmarking" yang sudah dibahas sedikit
[disini](https://faultable.dev/email-sebagai-platform/). Aplikasi ini bertujuan untuk:

- Menyembunyikan informasi pribadi pengguna ketika memuat gambar
- Memastikan semua *request* terkait gambar menggunakan protokol HTTPS
- Mengurangi permintaan ke pihak ketiga untuk level pengguna 

Aplikasi "bookmarking" tersebut target platform utamanya adalah *email client*, dan sebagaimana yang
kita tahu bahwa satu-satunya cara untuk melacak pengguna adalah dengan memuat gambar eksternal di
*email*.

Meskipun kemungkinan terjadinya kasus diatas sangat minim, setidaknya poin 2-3 dapat tercapai demi
efektivitas operasional aplikasi

## Development

Setelah dependensi selesai dipasang, kamu bisa menjalankan perintah berikut:

```bash
FLASK_APP=sasak FLASK_ENV=development flask run
```

Jika kamu menggunakan Fish, perintah yang tepat adalah seperti ini:

```bash
env FLASK_APP=sasak FLASK_ENV=development flask run
```

Sila kunjungi `localhost:5000/<digest>/<url_hex>` dan lihat yang terjadi

Catatan:

Bagaimana untuk mendapatkan `digest` dan `[url_hex](url_hex)` tanpa repot?

1. Siapkan url lengkap gambar
2. Hash url tersebut menjadi bentuk SHA1 dengan secret yang sudah ditentukan, bisa dilakukan
   [disini](https://www.freeformatter.com/hmac-generator.html)
3. Ubah url sebelumnya menjadi hex, bisa [disini](https://www.rapidtables.com/convert/number/ascii-to-hex.html)
4. Tinggal copas deh

## Test

Kita test menggunakan `unittest` nya Python, untuk menjalankannya, bisa
menggunakan perintah ini:

```bash
python3 -m unittest discover -v
```

Jika ingin melakukan *code coverage*, sila memasang
[coverage](https://coverage.readthedocs.io/en/coverage-5.2.1/) di global environment lalu jalankan
perintah berikut:

```bash
coverage run -m unittest discover -v
```

## Lisensi

MIT

