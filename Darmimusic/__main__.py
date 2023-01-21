#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Darmimusic import LOGGER, app, userbot
from Darmimusic.core.call import Yukki
from Darmimusic.plugins import ALL_MODULES
from Darmimusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Darmimusic").error(
            "Tidak Ada Asisten Klien Yang Ditentukan Vars!.. Proses Keluar."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Darmimusic").warning(
            "Tidak ada Spotify Vars yang ditentukan. Bot Anda tidak akan dapat memutar kueri spotify."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Darmimusic.plugins" + all_module)
    LOGGER("Darmimusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Yukki.start()
    try:
        await Yukki.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Darmimusic").error(
            "[ERROR] - \n\nHarap aktifkan Panggilan Suara Grup Pencatat Anda. Pastikan Anda tidak pernah menutup/mengakhiri panggilan suara di grup log Anda"
        )
        sys.exit()
    except:
        pass
    await Yukki.decorators()
    LOGGER("Darmimusic").info("Bot Musik Darmi Dimulai dengan Sukses")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Darmimusic").info("Menghentikan Bot Musik Darmi! Selamat tinggal")
