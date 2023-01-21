#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.


import asyncio

from pyrogram import Client as c

API_ID = input("\nMasukkan API_ID:\n > ")
API_HASH = input("\nMasukkan API_HASH:\n > ")

print("\n\n Masukkan nomor telepon saat diminta.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    xx = f"DI SINI ADALAH SESI STRING ANDA, SALIN, JANGAN DIBAGIKAN!!\n\n`{ss}`\n\nDIHASILKAN OLEH DARMI"
    ok = await i.send_message("me", xx)
    print("\nDI SINI ADALAH SESI STRING ANDA, SALIN, JANGAN DIBAGIKAN!!\n")
    print(f"\n{ss}\n") 
    print("\nDIHASILKAN OLEH DARMI\n")


asyncio.run(main())
