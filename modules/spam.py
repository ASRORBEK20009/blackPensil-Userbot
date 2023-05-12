import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix

commands = ["spam", "statspam", "slowspam", "fastspam"]


@Client.on_message(filters.command(commands, prefix) & filters.me)
async def spam(client: Client, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])

    cooldown = {"spam": 0.15, "statspam": 0.1, "slowspam": 0.9, "fastspam": 0}

    await message.delete()

    for msg in range(amount):
        if message.reply_to_message:
            sent = await message.reply_to_message.reply(text)
        else:
            sent = await client.send_message(message.chat.id, text)

        if message.command[0] == "statspam":
            await asyncio.sleep(0.1)
            await sent.delete()

        await asyncio.sleep(cooldown[message.command[0]])


modules_help["spam"] = {
    "spam [amount] [text]": "Start spam",
    "statspam [amount] [text]": "Send and delete",
    "fastspam [amount] [text]": "Start fast spam",
    "slowspam [amount] [text]": "Start slow spam",
}
