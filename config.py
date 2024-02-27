import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()



#Basic-Setup
OWNER_ID = 6295947116
LOGGER_ID = -1001947276976

#Bot-Setup
BOT_TOKEN = "6189399999:AAFaN1Z_TD3kq16I87EMeuD_TMu23Lpqq_k"

#MongoDB-Setup
MONGO_DB_URI = "mongodb+srv://gotouhitoriii:Zd4BtpM6JC7hWDc0@suika.al7oyue.mongodb.net/?retryWrites=true&w=majority&appName=Suika"

#Assistant-Setup
API_ID = 22069422
API_HASH = "a2b3891c2041a4326fcb4e77b54fb32a"

STRING1 = "AQExX0YAsiyPsOjlKh7SMf9FEeIBVaI_9FWLYz4fEgATyid7kl7DORMSqKiaqFkQMi3j4lBFlotE3GrZ0ORSNpu-Ry-A6rgA1WCheVEE3rHKtv1wMkZ9oZU_u7NZxGyRWzcoiS-ZEnUo3FX0ygPChG-s8kbPzmwyhjsP5vR19AbcCc0Q4ZiyVaUCbPg0a0PABp__Jm76OmKTaitV4uY2cVR6WK6K37DEUOXcpn3_ow_78tysZcN-jifh30fLYaT_kXbYdny-9b4ZgQ1jjAttHCigJmwkDo4aYHDkUyK5L3pS0nPokvQWQ4oBNulpXnql8kr1cSkDTN8SbHmlL5IHypKKAvJ0hAAAAAFqyyBcAA"
STRING2 = "AQExX0YAsdC2f4A841hwcQfoUgM4Ck1m1_LjwofrtE1HhCs2GkKo_Uvdb4E5JnhxAY80bJxleUq9NkOZ8n5xhmdZU3VCYHuFtk9Jy_gccvCzmwwABbR_QH8wNLZTyLMwdM75CCJvjCdcP1okVqNrhm7T9GlBVyNmS0Lv1JACENVuDda-gp9wa4sAiCVxwqMYSWgtXbkgKBBBxrBfyxs2rymlNm0wECWw7ZQUmBsbcCXfQZzrCV56bgDUCLVGo6WwMQCQwqaxeb4RKDOENyB4IM-OZQtYFCXUVlPs90lAOM37hCU8ug7ITqqlbQVeFx_gTTiEn8bi0nJ-3ZThh_OnoKopK9lk8AAAAAFqyyBcAA"
STRING3 = "AQExX0YAPGP26w-NRrCCo6NWSDsFK-0g6jVl4jItVXjnU-ODRxjwzWmm4R7zPCuLYibQBr3CWHFDNz8oef4W4bG6ytFfjEMJ1Bs3CL1_F2aEml3KmYaQpPfgDyW_RSXbxsZSVSUxzbxzlgnYoED7dW83G00CUlmPBmp8Brz8JgygKhnzfXa64HeUzRm_T9dnhOmh1Gc8MsGNOx8aXf31bwo1zj4ghJdpOwhmPoAjvw2tSgs0myWgiCkZ5ZqRWX9UEj-H6wVGdLNMY171xJYAdolRs3owZzpYznu51JrKsImRULTdbwvSpSKMtG0l8eGl4EUfzR7UcLwjnxajH6K07tC9Eh8exAAAAAFqyyBcAA"
STRING4 = "AQExX0YAXi9wzFFWfXAQwl_0_YVriQSPTMfxeGiUcpSu44Wken5yNMmsHA3zOSc-YoajpHcBm34pG8Dlh-9t-LmJaGB9fgL2sS_w6KXEzJMEgrXLFHRLmO7v7MNPS5ap3zT-Eq_GDcCQiWHrBZtwhnOSwn1rmjv2p80vBeRzNQLosz67RMHCfIfSfFCytXQf6crsZcQLsyRHMfQ2MIn06vhXF_eaxoyeCcBiZq_km2RpizertWLjqo5ET0IXk1H5Dzu06WlGgXFJ3PgLvvUJz-nPXNBHztjzhb3lym17Bjwp8Z3Ix0AkbnmUufMBIT6mXKgyT-ImNumEK7jlGmAHQAijhYxR2gAAAAFqyyBcAA"
STRING5 = "AQExX0YAYQSaxN4mnSskvbScI-1ZWPU_KOS1ZqDbQEYe9C_fpV4EpI0r90A3kwwQ0RitiGU13PXKhrRQQHgISXuWlPkll9AtODbmXgABLy_nLk-z42BV0fVtbgxooU9Ei6i8iycNMBslI5VzLIh3e3NI5I3CCSO3oww7gVF5SIBy-EhNqb00X0vqskEsJS7lMa44xv8aZyb7zgXGeVOXcWk7DUzbmJ72uXcxrSMEoyr1V5aF1nbjjhiPwAZbjBXaHcuUCrWajujfvZlYxgfNA5jwkmXV183jZGSWnExKMVemYGV6X-n_rCzxyu3Kg5P86rnWsq481kNYaIMgiadW-v2piMANNQAAAAFqyyBcAA"
AUTO_LEAVING_ASSISTANT = bool("True")



SUPPORT_CHANNEL = "SUPPORT_CHANNEL", "https://t.me/CHATHV3N"
SUPPORT_CHAT = "SUPPORT_CHAT", "https://t.me/CHATHV3N"

SPOTIFY_CLIENT_ID = "6a376276a5ab4ce88428cdb8f76eaf8b"
SPOTIFY_CLIENT_SECRET = "86e6b8e2e4a74f89a7774e3856871944"

HEROKU_APP_NAME = "HEROKU_APP_NAME"
HEROKU_API_KEY = "HEROKU_API_KEY"

UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/JustAyu/Aest")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

#Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2500))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 1000))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "START_IMG_URL", "https://te.legra.ph/file/192f102f7d6a7a4561c82.jpg"
PING_IMG_URL = "PING_IMG_URL", "https://te.legra.ph/file/5ca09da4f777b791cc128.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e1ba3681120abf59e99ef.jpg"
PLAYLIST_IMG_URL = "https://te.legra.ph/file/f4f35a6b0409d13ef2432.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/a87bfaa9891a5eeee1c0b.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/a87bfaa9891a5eeee1c0b.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/015bc41c2ca1c2f78d1c9.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/b599dbbe7e487b79ed8ba.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/fe33856d0222b08beb04c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/fe33856d0222b08beb04c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/fe33856d0222b08beb04c.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
