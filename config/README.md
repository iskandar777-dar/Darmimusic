# Yukki Music Bot Configs

Config vars pada dasarnya adalah variabel yang mengonfigurasi atau memodifikasi bot agar berfungsi, yang merupakan kebutuhan dasar plugin atau kode agar berfungsi. Anda harus mengatur var wajib yang tepat untuk membuatnya berfungsi dan memulai fitur dasar bot.

### Kenali semua vars ini secara mendalam dari Docs kami. [Baca Sekarang dari Sini](https://notreallyshikhar.gitbook.io/yukkimusicbot/config-vars/available-vars)

## Var Wajib

- Ini adalah vars minimum yang diperlukan untuk menyiapkan agar Bot Musik Yukki berfungsi.

1. `API_ID` : Dapatkan dari my.telegram.org
2. `API_HASH` : Dapatkan dari my.telegram.org
3. `BOT_TOKEN` : Dapatkan dari [@Botfather](http://t.me/BotFather) di Telegram
4. `MONGO_DB_URI` : Dapatkan mongo db [dari sini.](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb)
5. `LOG_GROUP_ID` ​​: Anda memerlukan ID Grup Pribadi untuk ini. Supergrup Dibutuhkan dengan id mulai dari -100
6. `MUSIC_BOT_NAME` : Nama untuk bot Musik Anda.
7. `OWNER_ID` : ID Pemilik Anda untuk mengelola bot Anda.
8. `STRING_SESSION` : Diperlukan Sesi Pyrogram, Hasilkan string dari [@darmimusikbot](http://t.me/darmimusikot) di Telegram.

## Vars Tidak Wajib

- Ini adalah var tambahan untuk fitur tambahan di dalam Bot Musik. Anda dapat meninggalkan var yang tidak wajib untuk saat ini dan dapat menambahkannya nanti.

1. `DURATION_LIMIT` : Durasi audio(musik) maks khusus untuk obrolan suara. Default ke 60 menit.
2. `SONG_DOWNLOAD_DURATION_LIMIT` : Batas Durasi Download Lagu dalam format MP3 atau MP4 dari bot. Default ke 180 menit.
3. `VIDEO_STREAM_LIMIT` : Jumlah maksimum panggilan video yang diizinkan di bot. Anda bisa mengaturnya nanti melalui /set_video_limit di telegram. Default ke 3 obrolan.
4. `SERVER_PLAYLIST_LIMIT` : Batas Maksimum Pengguna dapat menyimpan daftar putar di server bot. Default ke 30
5. `PLAYLIST_FETCH_LIMIT` : Batas maksimum untuk mengambil track playlist dari link youtube, spotify, apple. Default ke 25
6. `CLEANMODE_MINS` : Waktu Cleanmode setelah bot akan menghapus pesan lamanya dari obrolan. Default ke 5 Menit.
7. `SUPPORT_CHANNEL` : Jika Anda memiliki saluran untuk bot musik Anda, isi dengan tautan saluran Anda
8. `SUPPORT_GROUP` : Jika Anda memiliki dukungan grup untuk bot musik Anda, isi dengan tautan grup Anda

## Mainkan FileSize Limit Vars

- Batas ukuran file maksimum untuk audio dan video yang dapat diputar pengguna dari bot Anda. [Hanya Ukuran Byte yang Diterima]
> Anda dapat mengonversi mb menjadi byte dari https://www.gbmb.org/mb-to-bytes dan menggunakannya di sini

1. `TG_AUDIO_FILESIZE_LIMIT` : Batas ukuran file maksimum untuk file audio yang dapat dialirkan melalui vc. Default ke 104857600 byte, yaitu 100MB
2. `TG_VIDEO_FILESIZE_LIMIT` : Batas maksimal ukuran file untuk file video yang dapat diputar. Default ke 1073741824 byte, yaitu 1024MB atau 1GB


## Bot Var

- Semua var ini digunakan untuk menyiapkan bot. Anda dapat mengedit vars ini jika Anda mau, jika tidak biarkan semuanya apa adanya.

1. `PRIVATE_BOT_MODE` : Setel ke `True` jika Anda ingin bot Anda hanya bersifat pribadi atau Salah untuk semua grup. Default ke Salah
2. `YOUTUBE_EDIT_SLEEP` : Durasi waktu tidur Untuk Pengunduh Youtube. Default ke 3 detik
3. `TELEGRAM_EDIT_SLEEP` : Durasi waktu tidur Untuk Pengunduh Telegram. Default ke 5 detik
4. `AUTO_LEAVING_ASSISTANT` : Setel ke `True` jika Anda ingin meninggalkan asisten setelah jangka waktu tertentu.
5. `ASSISTANT_LEAVE_TIME` : Waktu setelah akun asisten Anda akan meninggalkan obrolan yang disajikan secara otomatis. Default ke 5400 detik, yaitu 90 Menit
6. `AUTO_DOWNLOADS_CLEAR` : Setel ke `True` jika Anda ingin menghapus unduhan setelah pemutaran musik berakhir.
7. `AUTO_SUGGESTION_MODE` : Setel ke `True` jika Anda ingin bot menyarankan tentang perintah bot ke obrolan acak bot Anda.
9. `AUTO_SUGGESTION_TIME` : Waktu setelah bot Anda akan menyarankan 1/10 obrolan acak dari obrolan yang Anda layani tentang perintah bot. Default ke 5400 detik, yaitu 90 Menit
10. `SET_CMDS` : Setel ke `True` jika Anda ingin bot Anda menyetel perintah untuk menu obrolan secara otomatis. [Referensi](https://i.postimg.cc/Bbg3LQTG/image.png)

## Spotify Vars

- Anda dapat memutar trek atau daftar putar dari spotify dari bot Musik Yukki
- Anda memerlukan dua var ini agar permainan spotify berfungsi. Ini tidak penting, Anda dapat mengosongkannya jika mau.

### Bagaimana cara mendapatkannya? [Baca dari sini](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/spotify)


1. `SPOTIFY_CLIENT_ID` : Dapatkan dari https://developer.spotify.com/dashboard
2. `SPOTIFY_CLIENT_SECRET` : Dapatkan dari https://developer.spotify.com/dashboard


## Heroku Vars

- Untuk mengerjakan beberapa modul yang kompatibel dengan Heroku, nilai var ini diperlukan untuk Mengakses akun Anda untuk menggunakan perintah `get_log`, `usage`, `update` dll.
- Anda dapat mengisi var ini menggunakan kunci API atau token Otorisasi Anda.

### Bagaimana cara mendapatkannya? [Baca dari sini](https://notreallyshikhar.gitbook.io/yukkimusicbot/config-vars/heroku-vars)

1. `HEROKU_API_KEY` : Dapatkan dari http://dashboard.heroku.com/account
2. `HEROKU_APP_NAME` : Anda harus memasukkan nama aplikasi yang Anda berikan untuk mengidentifikasi Bot Musik Anda di Heroku.


## Var Repo Kustom

- Jika Anda berencana untuk menggunakan Bot Musik Yukki dengan kode Anda yang disesuaikan atau dimodifikasi.

1. `UPSTREAM_REPO` : URL Repo Hulu atau Forked Repo Anda.
2. `UPSTREAM_BRANCH` : Cabang Default URL Repo Hulu atau Forked Repo Anda.
3. `GIT_TOKEN` : GIT TOKEN Anda jika repo hulu Anda bersifat pribadi
4. `GITHUB_REPO` : URL Repo Github Anda, yang akan ditampilkan di /start command



## Gambar/Thumbnail Vars

- Anda dapat mengubah gambar yang digunakan di Bot Musik Yukki.
- Anda dapat membuat tautan telegaf dari [@YukkiTelegraphBot](http://t.me/YukkiTelegraphBot) dan menggunakannya di sini.

1. `START_IMG_URL` : Gambar yang muncul pada /memulai perintah dalam pesan pribadi bot.
2. `PING_IMG_URL` : Gambar yang muncul pada perintah /ping bot.
3. `PLAYLIST_IMG_URL` : Gambar yang muncul pada perintah /play bot.
4. `GLOBAL_IMG_URL` : Gambar yang muncul pada perintah /stats bot.
5. `STATS_IMG_URL` : Gambar yang muncul pada perintah /stats bot.
6. `TELEGRAM_AUDIO_URL` : Gambar ini muncul saat seseorang memutar audio dari telegram.
7. `TELEGRAM_VIDEO_URL` : Gambar ini muncul saat seseorang memutar video dari telegram.
8. `STREAM_IMG_URL` : gambarnya muncul saat seseorang memainkan m3u8 atau tautan indeks.
9. `SOUNCLOUD_IMG_URL` : Gambar ini muncul saat seseorang memutar musik dari soundcloud.
10. `YOUTUBE_IMG_URL` : Gambar ini muncul jika pembuat thumbnail gagal membuat jempol.
11. `SPOTIFY_ARTIST_IMG_URL` : Gambar ini muncul saat seseorang memutar artis Spotify melalui tautan dalam mode sebaris.
12. `SPOTIFY_ALBUM_IMG_URL` : Gambar ini muncul saat seseorang memutar album Spotify melalui tautan dalam mode sebaris.
13. `SPOTIFY_PLAYLIST_IMG_URL` : Gambar ini muncul saat seseorang memutar album Spotify melalui tautan dalam mode sebaris.

## Mode Multi Asisten

- Anda dapat menggunakan hingga 5 Asisten Klien (memungkinkan bot Anda bekerja setidaknya dalam 2000-2500 obrolan sekaligus)

1. `STRING_SESSION2` : Diperlukan Sesi Pyrogram, Hasilkan string dari [@YukkiStringBot](http://t.me/YukkiStringBot) di Telegram.
2. `STRING_SESSION3` : Diperlukan Sesi Pyrogram, Hasilkan string dari [@YukkiStringBot](http://t.me/YukkiStringBot) di Telegram.
3. `STRING_SESSION4` : Diperlukan Sesi Pyrogram, Hasilkan string dari [@YukkiStringBot](http://t.me/YukkiStringBot) di Telegram.
4. `STRING_SESSION5` : Diperlukan Sesi Pyrogram, Hasilkan string dari [@YukkiStringBot](http://t.me/YukkiStringBot) di Telegram.
