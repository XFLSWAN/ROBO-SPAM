from telethon import __version__, events, Button

from config import X1


START_BUTTON = [
    [
        Button.url("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", "https://t.me/StrangerSuperbot?startgroup=true")
    ],
    [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/mastiwithfriendsxd"),
        Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/SHIVANSH474")
    ],
    [
        Button.inline("ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", data="help_back")
    ]
]


@X1.on(events.NewMessage(pattern="/sstart"))
async def start(event):              
    if event.is_private:
        Altbot = await event.client.get_me()
        bot_name = Altbot.first_name
        bot_id = Altbot.id
        TEXT = f"**❖ ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ.\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n● ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id}) ʙᴏᴛ.**\n\n"
        TEXT += f"● **sᴛʀᴀɴɢᴇʀʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ ➥** `M3.9/V8`\n"
        TEXT += f"● **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥** `3.11.8`\n"
        TEXT += f"● **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥** `{__version__}`\n\n"
        TEXT += f"❖ **ᴛʜɪs ɪs ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ sᴛʀᴀɴɢᴇʀ-sᴘᴀᴍ ʙᴏᴛ ғᴏʀ ɴᴏɴ sᴛᴏᴘ sᴘᴀᴍᴍɪɴɢ.**"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/29836fd9daa68203f6a0c.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
      )
