#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Perintah Admin:</u>**

**c** adalah singkatan dari pemutaran saluran.

/pause atau /cpause - Menjeda pemutaran musik.
/resume atau /cresume- Melanjutkan musik yang dijeda.
/mute atau /cmute- Membisukan musik yang diputar.
/unmute atau /cunmute- Suarakan musik yang dibisukan.
/skip atau /cskip- Lewati musik yang sedang diputar.
/stop atau /cstop- Menghentikan pemutaran musik.
/shuffle atau /cshuffle- Secara acak mengocok daftar putar yang antri.
/seek atau /cseek - Teruskan Mencari musik sesuai durasi Anda
/seekback atau /cseekback - Mundur Mencari musik sesuai durasi Anda
/restart - Mulai ulang bot untuk obrolan Anda.


✅<u>**Lewati Spesifik:**</u>
/skip atau /cskip [Angka(contoh: 3)]
    - Lewati musik ke nomor antrean yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrean ketiga dan akan mengabaikan musik 1 dan 2 dalam antrean.

✅<u>**Putar Berulang:**</u>
/loop atau /cloop [aktifkan/nonaktifkan] atau [Angka antara 1-10]
    - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default ke 10 kali.

✅<u>**Pengguna Resmi:**</u>
Pengguna Autentikasi dapat menggunakan perintah admin tanpa hak admin di obrolan Anda.

/auth [Nama Pengguna] - Menambahkan pengguna ke DAFTAR AUTH grup.
/unauth [Username] - Menghapus pengguna dari AUTH LIST grup.
/authusers - Periksa DAFTAR AUTH grup."""


HELP_2 = """✅<u>**Mainkan Perintah:**</u>

Perintah yang Tersedia = play , vplay , cplay

Perintah ForcePlay = playforce , vplayforce , cplayforce

**c** adalah singkatan dari pemutaran saluran.
**v** adalah singkatan dari pemutaran video.
**force** adalah singkatan dari force play.

/play atau /vplay atau /cplay - Bot akan mulai memutar kueri yang Anda berikan pada obrolan suara atau Streaming tautan langsung pada obrolan suara.

/playforce atau /vplayforce atau /cplayforce - **Force Play** menghentikan trek yang sedang diputar di obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/menghapus antrean.

/channelplay [Nama pengguna atau id Obrolan] atau [Nonaktifkan] - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.


✅**<u>Daftar Putar Server Bot:</u>**
/ daftar putar - Periksa Daftar Putar Tersimpan Anda Di Server.
/deleteplaylist - Hapus musik yang disimpan di daftar putar Anda
/putar - Mulai mainkan Daftar Putar Tersimpan Anda dari Server."""


HELP_3 = """✅<u>**Perintah Bot:**</u>

/stats - Dapatkan 10 Lagu Teratas Statistik Global, 10 Pengguna bot Teratas, 10 Obrolan Teratas di bot, 10 Teratas Dimainkan dalam obrolan, dll.

/sudolist - Periksa Pengguna Sudo Bot Musik Yukki

/ lirik [Nama Musik] - Mencari Lirik Musik tertentu di web.

/lagu [Nama Lagu] atau [Tautan YT] - Unduh lagu apa pun dari youtube dalam format mp3 atau mp4.

/ pemain - Dapatkan Panel Bermain interaktif.

**c** adalah singkatan dari pemutaran saluran.

/queue atau /cqueue- Periksa Daftar Antrian Musik."""

HELP_4 = """✅<u>**Perintah Ekstra:**</u>
/ mulai - Mulai Bot Musik.
/help - Dapatkan Menu Pembantu Perintah dengan penjelasan rinci tentang perintah.
/ ping- Ping Bot dan periksa statistik Ram, CPU, dll dari Bot.

✅<u>**Pengaturan Grup:**</u>
/ pengaturan - Dapatkan pengaturan grup lengkap dengan tombol sebaris

🔗 **Pilihan di Pengaturan:**

1️⃣ Anda dapat mengatur **Kualitas Audio** yang ingin Anda streaming di obrolan suara.

2️⃣ Anda dapat mengatur **Kualitas Video** yang ingin Anda streaming di obrolan suara.

3️⃣ **Pengguna Resmi**:- Anda dapat mengubah mode perintah admin dari sini ke semua orang atau admin saja. Jika semua orang, siapa pun yang hadir di grup Anda akan dapat menggunakan perintah admin (seperti /lewati, /berhenti dll)

4️⃣ **Mode Bersih:** Jika diaktifkan, hapus pesan bot setelah 5 menit dari grup Anda untuk memastikan obrolan Anda tetap bersih dan baik.

5️⃣ **Command Clean** : Saat diaktifkan, Bot akan segera menghapus perintah yang dieksekusi (/play, /pause, /shuffle, /stop dll).

6️⃣ **Pengaturan Putar:**

/playmode - Dapatkan panel pengaturan permainan lengkap dengan tombol tempat Anda dapat mengatur pengaturan permainan grup Anda.

<u>Opsi dalam mode putar:</u>

1️⃣ **Mode Pencarian** [Langsung atau Sebaris] - Mengubah mode pencarian Anda saat Anda memberi / mode putar.

2️⃣ **Perintah Admin** [Semua Orang atau Admin] - Jika semua orang, siapa pun yang ada di grup Anda akan dapat menggunakan perintah admin (seperti /lewati, /berhenti dll)

3️⃣ **Jenis Putar** [Semua Orang atau Admin] - Jika admin, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara."""

HELP_5 = """🔰**<u>TAMBAH & HAPUS PENGGUNA SUDO :</u>**
/addsudo [Nama Pengguna atau Balas ke pengguna]
/delsudo [Nama Pengguna atau Balas ke pengguna]

🛃**<u>HEROKU:</u>**
/ penggunaan - Penggunaan Dyno.

🌐**<u>VAR KONFIG:</u>**
/get_var - Dapatkan config var dari Heroku atau .env.
/del_var - Hapus semua var di Heroku atau .env.
/set_var [Var Name] [Value] - Tetapkan Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Nilainya dengan spasi.

🤖**<u>PERINTAH BOT:</u>**
/reboot - Mulai ulang Bot Anda.
/ perbarui - Perbarui Bot.
/speedtest - Periksa kecepatan server
/ pemeliharaan [aktifkan / nonaktifkan]
/ logger [aktifkan / nonaktifkan] - Bot mencatat kueri yang dicari di grup logger.
/get_log [Jumlah Baris] - Dapatkan log bot Anda dari heroku atau vps. Bekerja untuk keduanya.
/autoend [aktifkan|nonaktifkan] - Aktifkan pengakhiran streaming otomatis setelah 3 menit jika tidak ada yang mendengarkan.

📈**<u>PERINTAH STATS:</u>**
/ suara aktif - Periksa obrolan suara aktif di bot.
/ video aktif - Periksa panggilan video aktif di bot.
/stats - Periksa Statistik Bot

⚠️**<u>FUNGSI CHAT DAFTAR HITAM:</u>**
/blacklistchat [CHAT_ID] - Daftar hitam semua chat agar tidak menggunakan Bot Musik
/whitelistchat [CHAT_ID] - Mengizinkan semua obrolan yang masuk daftar hitam menggunakan Bot Musik
/blacklistedchat - Periksa semua obrolan yang masuk daftar hitam.

👤**<u>FUNGSI YANG DIBLOKIR:</u>**
/ blokir [Nama Pengguna atau Balas ke pengguna] - Mencegah pengguna menggunakan perintah bot.
/ buka blokir [Nama Pengguna atau Balas ke pengguna] - Hapus pengguna dari Daftar Blok Bot.
/blockedusers - Periksa Daftar Pengguna yang diblokir

👤**<u>FUNGSI GBAN:</u>**
/gban [Nama Pengguna atau Balas ke pengguna] - Gban pengguna dari obrolan yang dilayani bot dan hentikan dia menggunakan bot Anda.
/ ungban [Nama Pengguna atau Balas ke pengguna] - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia untuk menggunakan bot Anda
/gbannedusers - Periksa Daftar Pengguna Gbanned

🎥**<u>FUNGSI VIDEOCALL:</u>**
/set_video_limit [Jumlah Obrolan] - Tetapkan jumlah maksimum Obrolan yang diizinkan untuk Panggilan Video dalam satu waktu. Default ke 3 obrolan.
/videomode [unduh|m3u8] - Jika mode unduh diaktifkan, Bot akan mengunduh video alih-alih memutarnya dalam bentuk M3u8. Secara Default ke M3u8. Anda dapat menggunakan mode unduh saat kueri apa pun tidak diputar dalam mode m3u8.

⚡️**<u>FUNGSI BOT PRIBADI:</u>**
/otorisasi [CHAT_ID] - Izinkan obrolan untuk menggunakan bot Anda.
/ batalkan otorisasi [CHAT_ID] - Larang obrolan menggunakan bot Anda.
/ resmi - Periksa semua obrolan bot Anda yang diizinkan.

🌐**<u>FUNGSI SIARAN:</u>**
/broadcast [Pesan atau Balas Pesan] - Menyiarkan pesan apa pun ke Obrolan yang Disajikan Bot.

<u>opsi untuk siaran:</u>
**-pin** : Ini akan menyematkan pesan Anda
**-pinloud** : Ini akan menyematkan pesan Anda dengan pemberitahuan keras
**-user** : Ini akan menyiarkan pesan Anda ke pengguna yang telah memulai bot Anda.
**-asisten** : Ini akan menyiarkan pesan Anda dari akun asisten bot Anda.
**-nobot** : Ini akan memaksa bot Anda untuk tidak menyiarkan pesan

**Contoh:** `/broadcast -user -assistant -pin Hello Testing`
"""
