#Orginal module by HamkerChat and Red-Aura and TeamdaisyX changes by HeLLxGodLike, UserLazy and zYxDevs
import re
import requests
import emoji

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
import re

import aiohttp
from googletrans import Translator as google_translator
# from google_trans_new import google_translator
from pyrogram import filters

from LaylaRobot.helper_extra.aichat import add_chat, get_session, remove_chat
from LaylaRobot.utils.arqapi import arq
from LaylaRobot.pyrogramee.pluginshelper import admins_only, edit_or_reply
from LaylaRobot.pyrogramee.errors import capture_err
from LaylaRobot import pbot as daisyx
from LaylaRobot import BOT_ID

translator = google_translator()

async def lunaQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


async def fetch(url):
    try:
        async with aiohttp.Timeout(10.0):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    try:
                        data = await resp.json()
                    except:
                        data = await resp.text()
            return data
    except:
        print("AI response Timeout")
        return


daisy_chats = []
en_chats = []
# AI Chat (C) 2020-2021 by @InukaAsith


@daisyx.on_message(
    filters.command("chatbot") & ~filters.edited & ~filters.bot & ~filters.private
)
@admins_only
async def hmm(_, message):
    global daisy_chats
    if len(message.command) != 2:
        await message.reply_text(
            "I only recognize `/chatbot on` and /chatbot `off only`"
        )
        message.continue_propagation()
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("Tanya AI Already Activated In This Chat")
            return
        await lel.edit(
            f"Tanya AI Successfully Added For Users In The Chat"
        )

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("Tanya AI Was Not Activated In This Chat")
            return
        await lel.edit(
            f"Tanya AI Successfully Deactivated For Users In The Chat"
        )

    elif status == "EN" or status == "en" or status == "english":
        if not chat_id in en_chats:
            en_chats.append(chat_id)
            await message.reply_text("English AI chat Enabled!")
            return
        await message.reply_text("English AI chat is Already Enabled.")
        message.continue_propagation()
    else:
        await message.reply_text(
            "I only recognize `/chatbot on` and /chatbot `off only`"
        )


@daisyx.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
@capture_err
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        return
    if not message.reply_to_message:
        return
    try:
        senderr = message.reply_to_message.from_user.id
    except:
        return
    if senderr != BOT_ID:
        return
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("Tanya", "Aco")
        test = test.replace("tanya", "aco")
        test = test.replace("Tanya", "Luna") #
        test = test.replace("Tanya", "luna") #
        test = test.replace("19", "9") #
        test = test.replace("@Llogvbiu adalah suamiku.", "Saya lajang.")
        test = test.replace("My husband is @Llogvbiu", "I'm single.")
        test = test.replace("@trashzz_bot", "Tanyabot.ai")
        test = test.replace("I was created by @Llogvbiu", "I made myself")
        test = test.replace("Hello there I am Tanya...nice to meet u", "Hi, my friend! Do you want me to tell you a joke?")
        test = test.replace("@Yoga_CIC is my owner" , "Have the control right.")
        test = test.replace("Hi, My name is Tanya Nice to meet you." , "Hi, my friend, what can I do for you today?")
       
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "Tanya")
        response = response.replace("aco", "Tanya")
        response = response.replace("Luna", "Tanya") #
        response = response.replace("luna", "tanya") #
        response = response.replace("9", "19") #
        response = response.replace("Saya lajang.", "@Llogvbiu adalah suamiku.")
        response = response.replace("I'm single.", "My husband is @Llogvbiu")
        response = response.replace("Tanyabot.ai", "@trashzz_bot")
        response = response.replace("I made myself", "I was Created by @Llogvbiu")
        response = response.replace("Hi, my friend! Do you want me to tell you a joke?", "Hello there I am Tanya...nice to meet u")
        response = response.replace("Have the control right." , "@Llogvbiu is my owner.")
        response = response.replace("Hi, my friend, what can I do for you today?" , "Hi, My name is Tanya Nice to meet you")
        pro = response
        try:
            await daisyx.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return

    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
        try:
            lan = translator.detect(rm)
            lan = lan.lang
        except:
            return
        test = rm
        if not "en" in lan and not lan == "":
            try:
                test = translator.translate(test, dest="en")
                test = test.text
            except:
                return
        # test = emoji.demojize(test.strip())

        test = test.replace("Tanya", "Aco")
        test = test.replace("Tanya", "aco")
        test = test.replace("Tanya", "Luna") #
        test = test.replace("Tanya", "luna") #
        test = test.replace("@Llogvbiu adalah suamiku.", "Saya lajang.")
        test = test.replace("My husband is @Llogvbiu", "I'm single.")
        test = test.replace("19", "9") #
        test = test.replace("@trashzz_bot", "Tanyabot.ai")
        test = test.replace("I was created by @Llogvbiu", "I made myself")
        test = test.replace("Hello there I am Tanya...nice to meet u", "Hi, my friend! Do you want me to tell you a joke?")
        test = test.replace("@Llogvbiu is my owner" , "Have the control right.")
        test = test.replace("Hi, My name is Tanya Nice to meet you." , "Hi, my friend, what can I do for you today?")
        response = await lunaQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "Tanya")
        response = response.replace("aco", "Tanya")
        response = response.replace("Luna", "   Tanya")
        response = response.replace("luna", "Tanya")
        response = response.replace("8", "19") #
        response = response.replace("Saya lajang.", "@Llogvbiu adalah suamiku.")
        response = response.replace("I'm single.", "My husband is @Llogvbiu")
        response = response.replace("Tanyabot.ai", "@trashzz_bot")
        response = response.replace("I made myself", "I was Created by @Llogvbiu")
        response = response.replace("Hi, my friend! Do you want me to tell you a joke?", "Hello there I am Tanya...nice to meet u")
        response = response.replace("Have the control right." , "@Tanya is my owner.")
        response = response.replace("Hi, my friend, what can I do for you today?" , "Hi, My name is Tanya Nice to meet you")
        pro = response
        if not "en" in lan and not lan == "":
            try:
                pro = translator.translate(pro, dest=lan)
                pro = pro.text
            except:
                return
        try:
            await daisyx.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return


@daisyx.on_message(
    filters.text & filters.private & ~filters.edited & filters.reply & ~filters.bot
)
@capture_err
async def inuka(client, message):
    if not get_session(int(message.chat.id)):
        return #
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return

    # test = emoji.demojize(test.strip())

    # Kang with the credits bitches @InukaASiTH
    test = test.replace("Asuna", "Aco")
    test = test.replace("asuna", "aco")
    test = test.replace("Asuna", "Luna") #
    test = test.replace("asuna", "luna") #
    test = test.replace("@Yoga_CIC adalah suamiku.", "Saya lajang.")
    test = test.replace("My husband is @Yoga_CIC", "I'm single.")
    test = test.replace("18", "9") #
    test = test.replace("@YBotsSupport", "Asunabot.ai")
    test = test.replace("I was created by @Yoga_CIC", "I made myself")
    test = test.replace("Hello there I am Asuna...nice to meet u", "Hi, my friend! Do you want me to tell you a joke?")
    test = test.replace("@Yoga_CIC is my owner" , "Have the control right.")
    test = test.replace("Hi, My name is Asuna Nice to meet you." , "Hi, my friend, what can I do for you today?")

    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Aco", "Tanya")
    response = response.replace("aco", "tanya")
    response = response.replace("Luna", "Tanya") #
    response = response.replace("luna", "tanya") #
    response = response.replace("9", "19") #
    response = response.replace("Saya lajang.", "@Llogvbiu adalah suamiku.")
    response = response.replace("I'm single.", "My husband is @Llogvbiu")
    response = response.replace("Tanyabot.ai", "@trashzz_bot")
    response = response.replace("I made myself", "I was Created by @Llogvbiu")
    response = response.replace("Hi, my friend! Do you want me to tell you a joke?", "Hello there I am Tanya...nice to meet u")
    response = response.replace("Have the control right." , "@Llogvbiu is my owner.")
    response = response.replace("Hi, my friend, what can I do for you today?" , "Hi, My name is Tanya Nice to meet you")

    pro = response
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, dest=lan)
        pro = pro.text
    try:
        await daisyx.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


@daisyx.on_message(
    filters.regex("TANYABOT|Tanya|TANYA|TanyaRobot|Tanyabot|Tanyachan|tanya")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
    & ~filters.edited
)
@capture_err
async def inuka(client, message):
    if not get_session(int(message.chat.id)):
        return #
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return

    # test = emoji.demojize(test.strip())

    test = test.replace("Tanya", "Aco")
    test = test.replace("tanya", "aco")
    test = test.replace("Tanya", "Luna") #
    test = test.replace("tanya", "luna") #
    test = test.replace("19", "9") #
    test = test.replace("@Llogvbiu adalah suamiku.", "Saya lajang.")
    test = test.replace("My husband is @Llogvbiu", "I'm single.")
    test = test.replace("@trashzz_bot", "Tanyabot.ai")
    test = test.replace("I was created by @Llogvbiu", "I made myself")
    test = test.replace("Hello there I am Tanya...nice to meet u", "Hi, my friend! Do you want me to tell you a joke?")
    test = test.replace("@Llogvbiu is my owner" , "Have the control right.")
    test = test.replace("Hi, My name is Asuna Nice to meet you." , "Hi, my friend, what can I do for you today?")

    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Aco", "Tanya")
    response = response.replace("aco", "tanya")
    response = response.replace("Luna", "Tanya") #
    response = response.replace("luna", "tanya") #
    response = response.replace("9", "19") #
    response = response.replace("Saya lajang.", "@Llogvbiu adalah suamiku.")
    response = response.replace("I'm single.", "My husband is @Llogvbiu")
    response = response.replace("Tanyabot.ai", "@trashzz_bot")
    response = response.replace("I made myself", "I was Created by @Llogvbiu")
    response = response.replace("Hi, my friend! Do you want me to tell you a joke?", "Hello there I am Tanya...nice to meet u")
    response = response.replace("Have the control right." , "@Llogvbiu is my owner.")
    response = response.replace("Hi, my friend, what can I do for you today?" , "Hi, My name is Tanya Nice to meet you")

    pro = response
    if not "en" in lan and not lan == "":
        try:
            pro = translator.translate(pro, dest=lan)
            pro = pro.text
        except Exception:
            return
    try:
        await daisyx.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return

__help__ = """
TANYA AI 3.0 IS THE ONLY AI SYSTEM WHICH CAN DETECT & REPLY UPTO 200 LANGUAGES
 - /chatbot ON/OFF: Enables and disables AI Chat mode (EXCLUSIVE)
 - /chatbot EN : Enables English only chatbot
 
*Asking*
 - <regex> <your question>
 Example:
 • Tanya who is Donald Trump

*Regex List*
 • `Tanya`, `tanya`, `TANYA`, `BotTanya`, `BOTTANYA`, `TanyaChan`, `tanyarobot`
 
*Assistant*
 - /ask [question]: Ask question from Asuna

Reports bugs at @trashzz_bot
"""

__mod_name__ = "ChatBot"
