from OpsAi import Ai
from asyncio import sleep as rest 
from datetime import datetime 
from Bikash import app
from pyrogram import filters



@app.on_message(filters.command("ask"))
async def ai_bot(_, message):
     if message.reply_to_message:
      queri = message.reply_to_message.text
      gonb = Ai(query=queri)
      await message.reply(gonb.chat())
     elif len(message.command) == 1:
      return await message.reply("ʜᴇʟʟᴏ 🥀\nɪ'ᴍ ᴀ ᴀɪ ᴀssɪsᴛᴀɴᴛ Fᴏʀ Aɴsᴡᴇʀ Yᴏᴜʀ Aɴʏ ǫᴜᴇsᴛɪᴏɴs, ʜᴏᴡ ᴄᴀɴ ɪ ʜᴇʟᴘ ʏᴏᴜ \n\nᴊᴏɪɴ [Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ](https://t.me/BikashGadgetsTech)")
     elif len(message.command) > 1:
      queri = message.text.split(None,1)[1]
     gonb = Ai(query=queri)
     x = Ai(query=queri)
     me = await message.reply_text("ᴘʀᴏᴄᴇssᴇs.....")
     await rest(2)
     mee = await me.edit_text("ᴀʟʟ ᴍᴏsᴛ ᴅᴏɴᴇ ....")
     await mee.delete()
     await rest(1)
     await message.reply(gonb.chat())
