# 📌 Stocky

## 🚀 Batch 1 - Fitur Prioritas
### ✅ 1️⃣ Manajemen Stok Barang
**Deskripsi:** CRUD barang dan pencarian berdasarkan nama/barcode.  

#### 📌 Task Breakdown:
#### 🔹 Backend:
- [ ] Membuat model database untuk tabel **products** dan **stock**
- [ ] API untuk **menambahkan produk baru**
- [ ] API untuk **mengupdate produk** (nama, deskripsi, kategori)
- [ ] API untuk **menghapus produk**
- [ ] API untuk **menambahkan stok produk**
- [ ] API untuk **mengurangi stok produk**
- [ ] API untuk **mendapatkan daftar produk berdasarkan nama/barcode**
- [ ] API untuk **menampilkan jumlah stok yang tersedia**
- [ ] Middleware untuk validasi input  

#### 🔹 Frontend (Mobile/Web):
- [ ] UI form untuk menambahkan produk  
- [ ] UI daftar produk dengan fitur pencarian  
- [ ] UI untuk menampilkan jumlah stok  

---

### ✅ 2️⃣ Scan Barcode & Expiry Date
**Deskripsi:** Scan barcode untuk mencari produk dan mendeteksi tanggal kedaluwarsa jika tersedia.  

#### 📌 Task Breakdown:
#### 🔹 Backend:
- [ ] API untuk **mencari produk berdasarkan barcode**
- [ ] API untuk **menyimpan batch barang dengan tanggal kedaluwarsa**
- [ ] API untuk **mengembalikan tanggal kedaluwarsa jika tersedia**
- [ ] Validasi format barcode  

#### 🔹 Frontend (Mobile/Web):
- [ ] Implementasi **barcode scanner** (contoh: `ML Kit`, `ZXing`)
- [ ] Menampilkan **hasil scan barcode**
- [ ] Jika tidak ada data barcode → UI untuk menambahkan produk  

---

### ✅ 3️⃣ Notifikasi Stok Habis & Barang Kedaluwarsa
**Deskripsi:** Notifikasi saat stok hampir habis atau barang mendekati tanggal kedaluwarsa.  

#### 📌 Task Breakdown:
#### 🔹 Backend:
- [ ] Scheduler untuk **mengecek stok yang hampir habis**
- [ ] Scheduler untuk **mengecek barang yang hampir expired**
- [ ] API untuk **mengelola metode notifikasi (email, push, SMS)**
- [ ] API untuk **mengambil daftar notifikasi**
- [ ] API untuk **menandai notifikasi sebagai terbaca**  

#### 🔹 Frontend (Mobile/Web):
- [ ] UI daftar notifikasi  
- [ ] UI untuk memilih metode notifikasi  
- [ ] UI untuk menampilkan detail notifikasi  

---

## 💡 Batch 2 - Fitur Tambahan
### ✅ 4️⃣ Todo List Belanja
**Deskripsi:** Jika stok habis, pengguna bisa menambahkannya ke daftar belanja.  

#### 📌 Task Breakdown:
#### 🔹 Backend:
- [ ] Model database untuk **shopping_list**
- [ ] API untuk **menambahkan produk ke daftar belanja**
- [ ] API untuk **menghapus produk dari daftar belanja**
- [ ] API untuk **mengambil daftar belanja**  

#### 🔹 Frontend (Mobile/Web):
- [ ] UI daftar belanja  
- [ ] UI untuk menambahkan item ke daftar belanja  
- [ ] Notifikasi pengingat untuk belanja  

---

### ✅ 5️⃣ Social Login (Google, Apple, Facebook, dll.)
**Deskripsi:** Memungkinkan pengguna login menggunakan akun sosial media.  

#### 📌 Task Breakdown:
#### 🔹 Backend:
- [ ] API untuk **mengautentikasi pengguna via OAuth2**
- [ ] API untuk **menghubungkan akun sosial ke akun sistem**
- [ ] Menyimpan token akses untuk sesi pengguna  

#### 🔹 Frontend (Mobile/Web):
- [ ] Implementasi tombol login dengan Google/Facebook/Apple  
- [ ] Menyimpan token sesi pengguna  
- [ ] UI logout dan profil pengguna  

---

## 📈 Batch 3 - Fitur Opsional & Optimalisasi
### ✅ 6️⃣ Laporan Stok & Penggunaan Barang
**Deskripsi:** Laporan jumlah stok dan histori penggunaan barang.  

#### 📌 Task Breakdown:
#### 🔹 Backend:
- [ ] Model database untuk **histori penggunaan barang**
- [ ] API untuk **mengambil laporan stok**
- [ ] API untuk **melihat histori penggunaan barang**  

#### 🔹 Frontend (Mobile/Web):
- [ ] UI untuk laporan stok  
- [ ] UI untuk histori penggunaan  

---