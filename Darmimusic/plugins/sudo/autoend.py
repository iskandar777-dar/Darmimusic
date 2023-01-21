#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters

import config
from strings import get_command
from Darmimusic import app
from Darmimusic.misc import SUDOERS
from Darmimusic.utils.database import autoend_off, autoend_on
from Darmimusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**Penggunaan :**\n\n/autoend [aktifkan|nonaktifkan]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto End Stream Diaktifkan.\n\nBot akan keluar dari obrolan suara secara otomatis setelah 3 menit jika tidak ada yang mendengarkan dengan pesan peringatan.."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Aliran Akhir Otomatis Dinonaktifkan.")
    else:
        await message.reply_text(usage)
