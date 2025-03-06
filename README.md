# 📦 Aplikasi Manajemen Stok Barang

## 📌 Fitur Utama (Batch 1 - Wajib Dikerjakan Dulu)
**🔹 Tujuan:** Aplikasi bisa digunakan untuk mencatat stok barang, mencari produk dengan barcode, dan memberikan peringatan barang kedaluwarsa.

- ✅ **Manajemen Stok Barang**
  - CRUD (Create, Read, Update, Delete) barang
  - Pencarian barang berdasarkan nama dan barcode
  - Menampilkan jumlah stok yang tersedia

- ✅ **Scan Barcode & Expiry Date**
  - Scan barcode produk menggunakan kamera
  - Backend mengembalikan data produk berdasarkan barcode
  - **Mendeteksi tanggal kedaluwarsa** dari barcode dan memberikan notifikasi

- ✅ **Autentikasi & Social Login**
  - Login dengan Google, Facebook, atau Apple
  - Simpan data pengguna di database
  - Gunakan JWT untuk sesi login

- ✅ **Notifikasi Stok Habis & Barang Kedaluwarsa**
  - Peringatan saat stok hampir habis
  - Notifikasi otomatis jika barang mendekati tanggal kedaluwarsa
  - Bisa memilih metode notifikasi (email, push notification, atau SMS)

- ✅ **To-Do List Belanja Otomatis**
  - Jika stok habis, otomatis masuk ke daftar belanja
  - Bisa menambahkan barang secara manual ke daftar belanja
  - Checklist untuk menandai barang yang sudah dibeli

---

## 🟡 Fitur Pendukung (Batch 2 - Menambah Kenyamanan Pengguna)
**🔹 Tujuan:** Meningkatkan pengalaman pengguna dan otomatisasi manajemen stok.

- ✅ **Multi-User & Sharing List**
  - Bisa berbagi stok dan daftar belanja dengan anggota keluarga
  - Role-based access (Admin, Viewer, Editor)

- ✅ **Statistik & Laporan Pengeluaran**
  - Menampilkan grafik barang masuk & keluar
  - Analisis pengeluaran dan rekomendasi budgeting

- ✅ **Export & Import Data (CSV/Excel)**
  - Backup data stok dalam format Excel / CSV
  - Bisa mengimpor daftar barang dari file Excel

---

## 🟠 Fitur Lanjutan (Batch 3 - Fitur Tambahan & AI)
**🔹 Tujuan:** Meningkatkan efisiensi dengan fitur otomatisasi dan AI.

- ✅ **AI Prediksi Stok & Saran Pembelian**
  - AI menganalisis pola penggunaan barang
  - Menampilkan **perkiraan kapan stok habis**
  - Memberikan rekomendasi jumlah pembelian

- ✅ **Mode Offline (PWA / Local DB di Mobile)**
  - Data tetap bisa diakses tanpa internet
  - Sinkronisasi otomatis saat online kembali

- ✅ **Integrasi dengan E-Commerce / Marketplace**
  - Bisa **langsung beli barang** dari e-commerce (Tokopedia, Shopee, dll.)
  - Notifikasi jika harga barang yang sering dibeli sedang diskon

---

## 🔵 Fitur Tambahan (Batch 4 - Baru Ditambahkan)
**🔹 Tujuan:** Mempermudah pencarian, input data, dan menyediakan rekomendasi belanja.

- ✅ **Kategori & Tag Barang**  
  - Bisa mengelompokkan barang berdasarkan **kategori** (Makanan, Elektronik, Peralatan, dll.)  
  - Bisa menambahkan **tag custom** untuk mempermudah pencarian  
  - Menampilkan **total stok per kategori**  

- ✅ **Scan Struk Belanja (OCR) & Auto-Input Barang**  
  - Menggunakan **OCR (Optical Character Recognition)** untuk membaca struk belanja  
  - Secara otomatis menambahkan barang yang baru dibeli ke stok  
  - Menghitung total pengeluaran bulanan berdasarkan data dari struk  

- ✅ **Fitur Bundling & Resep Masakan**  
  - Bisa mengelompokkan beberapa barang menjadi satu paket (misalnya, "Paket Sarapan" terdiri dari telur, susu, roti)  
  - Menyediakan **daftar bahan masakan** dengan stok yang tersedia  
  - Menampilkan **saran masakan berdasarkan stok barang yang masih ada**  

---