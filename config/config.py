#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Dapatkan dari my.telegram.org
API_ID = int(getenv("API_ID", "9894136"))
API_HASH = getenv("API_HASH", "b2c0593b734249a1b27589e93707d776")

# Dapatkan dari @Botfather di Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5661784900:AAHRsreMNSArNM2uU-auqG4pWTWY9LYQdp4")

# Basis data untuk menyimpan obrolan dan statistik Anda... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://dano1:dano1@cluster0.ajshk2h.mongodb.net/?retryWrites=true&w=majority")

# Durasi audio (musik) maks khusus untuk obrolan suara. setel DURATION_LIMIT dalam variabel dengan waktu Anda sendiri (menit), Default ke 60 menit.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "60")
)  # Ingatlah untuk memberi nilai dalam Menit

# Batas Durasi Download Lagu dalam format MP3 atau MP4 dari bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Ingatlah untuk memberi nilai dalam Menit

# Anda memerlukan ID Grup Pribadi untuk ini.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001546280719"))

# Nama untuk bot Musik Anda.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Darmimusik")

# ID Pengguna Anda.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "2099942562").split())
)  # Jenis input harus interger

# Dapatkan dari http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# Anda harus memasukkan nama aplikasi yang Anda berikan untuk mengidentifikasi Bot Musik Anda di Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# Untuk Repositori yang disesuaikan atau dimodifikasi
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/iskandar777-dar/Darmimusik",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# GIT TOKEN (jika repo Anda yang diedit bersifat pribadi)
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Hanya format Tautan yang diterima untuk nilai Var ini.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", None
)  # Contoh:- https://t.me/medchannell
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", None
)  # Contoh:- https://t.me/medSupportt

# Setel ke True jika Anda ingin meninggalkan asisten Anda setelah jangka waktu tertentu. [Setel waktu melalui AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

# Waktu setelah akun asisten Anda akan meninggalkan obrolan secara otomatis.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)  # Ingatlah untuk memberi nilai dalam Detik

# Waktu setelah itu bot akan menyarankan obrolan acak tentang perintah bot.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400")
)  # Ingatlah untuk memberi nilai dalam Detik

# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", None)

# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes

# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", False)

# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @YukkiStringBot
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#   __  __ _    _  _____ _____ _____   ____   ____ _______
#  |  \/  | |  | |/ ____|_   _/ ____| |  _ \ / __ \__   __|
#  | \  / | |  | | (___   | || |      | |_) | |  | | | |
#  | |\/| | |  | |\___ \  | || |      |  _ <| |  | | | |
#  | |  | | |__| |____) |_| || |____  | |_) | |__| | | |
#  |_|  |_|\____/|_____/|_____\_____| |____/ \____/  |_|


### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
START_IMG_URL = getenv("START_IMG_URL", None)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - URL SUPPORT_CHANNEL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - URL SUPPORT_GROUP Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Url UPSTREAM_REPO Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Url GITHUB_REPO Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
        )
        sys.exit()


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Url PING_IMG_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Url PLAYLIST_IMG_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Url GLOBAL_IMG_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Url STATS_IMG_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Url TELEGRAM_AUDIO_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - URL STREAM_IMG_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Url SOUNCLOUD_IMG_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Url YOUTUBE_IMG_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Url YOUTUBE_IMG_URL Anda salah. Harap pastikan bahwa itu dimulai dengan https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[ERROR] - Anda salah menentukan MUSIC_BOT_NAME. Tolong jangan gunakan karakter khusus atau font khusus untuk ini... Tetap sederhana dan kecil."
    )
    sys.exit()
