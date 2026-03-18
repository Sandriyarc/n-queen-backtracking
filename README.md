# N-Queen Backtracking Visualization

## 📌 Deskripsi
Program ini merupakan implementasi algoritma **Backtracking** untuk menyelesaikan **N-Queen Problem**.  
Visualisasi dibuat menggunakan GUI (Tkinter) yang menampilkan proses pencarian solusi secara **step-by-step**.

---

## 🎯 Tujuan
- Memahami konsep algoritma backtracking
- Menyelesaikan N-Queen Problem
- Menampilkan proses penyelesaian secara visual dan interaktif

---

## ⚙️ Fitur
- Visualisasi papan catur
- Step-by-step solving
- Indikator warna:
  - 🟡 Kuning → posisi sedang dicoba
  - 🟢 Hijau → posisi valid
  - 🔴 Merah → posisi tidak valid / backtracking
- Log proses langkah-langkah
- Status program (Idle, Running, Done)
- Sound effect (opsional)

---

## 🧠 Cara Kerja Algoritma
Algoritma bekerja dengan mencoba menempatkan ratu satu per satu pada setiap baris.  
Jika posisi tidak aman (bertabrakan dengan ratu lain), maka algoritma akan melakukan **backtracking** dan mencoba posisi lain.

---

## ▶️ Cara Menjalankan
1. Pastikan Python sudah terinstall
2. Jalankan file:
   ```bash
   python nqueen.py
