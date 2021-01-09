import asyncio

from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    YouBlockedUserError,
)
from telethon.tl.functions.messages import ImportChatInviteRequest

from userbot import CMD_HELP


@register(outgoing=True, pattern="^.sdd(?: |$)(.*)", disable_errors=True)
async def _(event):

    if event.fwd_from:

        return

    d_link = event.pattern_match.group(1)

    if ".com" not in d_link:

        await eor(event, "` I need a link to download something pro.`**(._.)**")

    else:

        await eor(event, "🎶**Initiating Download!**🎶")

    async with borg.conversation("@DeezLoadBot") as conv:

        try:

            await conv.send_message("/start")

            await conv.get_response()

            try:

                await borg(ImportChatInviteRequest("AAAAAFZPuYvdW1A8mrT8Pg"))

            except UserAlreadyParticipantError:

                await asyncio.sleep(0.00000069420)

            await conv.send_message(d_link)

            details = await conv.get_response()

            await borg.send_message(event.chat_id, details)

            await conv.get_response()

            songh = await conv.get_response()

            await borg.send_file(
                event.chat_id,
                songh,
                caption="🔆**Here's the requested song!**🔆\n`Check out` [Paraboy](https://t.me/topglobal_epep)",
            )

            await event.delete()

        except YouBlockedUserError:

            await eor(event, "**Error:** `unblock` @DeezLoadBot `and retry!`")


CMD_HELP.update(
    {"spotifydl": ".sdd <link>\nUse - Download song from spotify/deezer."}
)
