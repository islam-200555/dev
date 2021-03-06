# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ูุชูุญ ูู ุชุดุบูู ุงูููุณููู ูุงูููุฏูู ูู ูุฌููุนุงุช ูู ุฎูุงู ูุญุงุฏุซุงุช ุงูููุฏูู ุงูุฌุฏูุฏุฉ ูู Telegram!**

๐ก **ููุนุฑูุฉ ุฌููุน ุงูุงูุฑ ุงูุจูุช ุงุถุบุท ุนูู ยป ๐ ุฒุฑุงุฑ ุงูุงูุงูุฑ!**

๐** ููุนุฑูู ุทุฑููู ุงุณุชุฎุฏุงู ุงุถุบุท ุนูู ูููู  ยป โ ุฒุฑุงุฑ ุงูุฏููู ุงูุงุณุงุณู!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ุงุถููู ุงูู ูุฌููุนุชู โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โ ุงูุฏููู ุงูุงุณุงุณู", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ ุงูุงูุงูุฑ", callback_data="cbcmds"),
                    InlineKeyboardButton("โค๏ธ ุงููุงูู", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ ุฌุฑูุจ ุงูุฏุนู", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ ุงูููุงุฉ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ ูุจุฑูุฌ ุงูุณูุฑุณ [V e R s O n ,]", url="https://t.me/Q_X_I_T"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **Basic Guide for using this bot:**

1.) **ุงููุง ุงุถููู ุงูู ุงููุฌููุนู.**
2.) **ุซุงููุง ุงุฑูุนูู ุงุฏูู .ุงูู ุงููุฌููุนู ุซู ุฑูููู ุงุฏูู .**
3.) **ุจุนุฏ ุงูุชุฑููู ุงูุชุจ reloadูุงุนุงุฏุฉ ุชุดุบูู ุงูุจูุช ุจุดูู ุฌูุฏ.**
3.) **ุถูู @{ASSISTANT_NAME} ุญุณุงุจ ุงููุณุงุนุฏ ุงู ุงูุชุจ ุงูุถู ุนูุดุงู ูุฏุฎู .**
4.) **ุจุนุฏ ููุง ุชุถููู ุงูุชุจ ุดุบู ูุชุดุบูู ุงุบุงูู ุงู ุงูุชุจ ููุฏูู ูุชุดุบูู ููุฏูู ุงู ูุงูุบ .**
5.) **ูู ูุชุฑู ุงุนูู reload ุนูุดุงู ูู ูู ุฎุทุง ูุชุตูุญ.**

๐ **If the userbot not joined to video chat, make sure if the video chat already turned on, or type ุงุฎุฑุงุฌ ุงููู then type /userbotjoin again.**

๐ก **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุงูุฑุฌูุน", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **press the button below to read the explanation and see the list of available commands !**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป ุงูุงูุฑ ุงุฏูู ุงูุฌุฑูุจ", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป ุงููุทูุ ุงูุงุณุงุณู", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ ุงูุงูุงูุฑ ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ ุงูุฑุฌูุน", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ุงูุงูุฑ ูุงู ุดุฎุต:

ยป ุดุบู (song name/link) - play music on video chat
ยป ููุฏูู (video name/link) - play video on video chat
ยป ูุงูู - play live video from yt live/m3u8
ยป ูุงุฆูุฉ ุงูุชุดุบูู - show you the playlist
ยป ุชุญููู ููุฏูู (query) - download video from youtube
ยป ุชุญููู (query) - download song from youtube
ยป /lyric (query) - scrap the song lyric
ยป /search (query) - search a youtube video link

ยป ุจูู - show the bot ping status
ยป ููุช ุงูุชุดุบูู - show the bot uptime status
ยป ุญุงูุฉ ุงูุจูุช - show the bot alive info (in group)

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ุงูุงูุฑ ุงุฏูู ุงูุฌุฑูุจ:

ยป ููู - pause the stream
ยป ููู - resume the stream
ยป ุชุฎุทู - switch to next stream
ยป ุงููุงู - stop the streaming
ยป /ูุชู - mute the userbot on voice chat
ยป ุงูุบุงุก ูุชู - unmute the userbot on voice chat
ยป /ุงูุตูุช `1-200` - adjust the volume of music (userbot must be admin)
ยป reload - reload bot and refresh the admin data
ยป ุงูุถู - invite the userbot to join group
ยป ุงุฎุฑุฌ - order userbot to leave from group

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ุงูุงูุฑ ุงููุทูุฑ ุงูุงุณุงุณู:

ยป /rmw - clean all raw files
ยป /rmd - clean all downloaded files
ยป ูุนูููุงุช ุงูุณูุฑูุฑ - show the system information
ยป ุชุญุฏูุซ - update your bot to latest version
ยป ุงุนุงุฏุฉ ุงูุชุดุบูู - restart your bot
ยป ุฎุฑูุฌ ุงููู - order userbot to leave from all group

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nยป revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **ุงูุงุนุฏุงุฏุงุช** {query.message.chat.title}\n\nโธ : pause stream\nโถ๏ธ : resume stream\n๐ : mute userbot\n๐ : unmute userbot\nโน : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
