from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot import CMD_HELP


@register(outgoing=True, pattern="^.gps(?: |$)(.*)", disable_errors=True)
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await eor(event, "What should I find? Give me a location.")

    await eor(event, "Finding...")

    geolocator = Nominatim(user_agent="telebot")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await eor(event, "Sorry, I coudn't find it")


CMD_HELP.update({"gps": ".gps <location>\nUse - Locate the place in the map."})
