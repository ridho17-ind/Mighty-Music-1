# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEJX5NgelpPxIp7TxBi31AWY0e6awyNoAACrwIAAiZaqFetusa6iC_gHx8E")
    await message.reply_text(
        f"""**┗┓| VCG BOT MUSIK |┏┛**

**Hallo {message.from_user.first_name} **🙋‍♂
Nama saya adalah __[Music Asssistant Bot](https://t.me/MightyMusicV2_bot)__
Saya bisa memutar musik di Voice Call Grup kamu
━━━━━━━━━━━━━━━━━━━━
Dikelola oleh **[Yunus Zend](https://t.me/ZendYNS)** 👨‍💻

❖ __Tambahkan **__[Music Assistant](https://t.me/MightyMusicV2)__** __dan__ **__[Music Bot](https://t.me/MightyMusicV2_bot)__** __ke grup Anda, dan rasakan sensasi mendengar musik di__ __**VC Group**__ __anda!!__
""",

# Edit Yang Perlu diganti saja agar tak terjadi kesalahan
# Ganti teks link bagian dalam dari tanda ()
# Dengan link akun asisten mu dan link bot kamu sesuai tempat yg seharusnya yah

        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📇 Command yang tersedia 📇", url="https://t.me/botinfochannel/5")
                  ],[
                    InlineKeyboardButton(
                        "💭 Group Support", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Creator 👨‍💻", url="https://t.me/ZendYNS"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔉", url="https://t.me/botinfochannel"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Iya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Cara Menggunakan BOT 📜", url="https://t.me/botinfochannel/5"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ **Bot berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💭 Group Support", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Owner", url="https://t.me/ZendYNS"
                    )
                ]
            ]
        )
   )
