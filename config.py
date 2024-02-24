import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()



#Basic-Setup
OWNER_ID = int(getenv("6295947116"))
LOGGER_ID = int(getenv("-1001947276976", None))

#Bot-Setup
BOT_TOKEN = getenv("6189399999:AAFaN1Z_TD3kq16I87EMeuD_TMu23Lpqq_k")

#MongoDB-Setup
MONGO_DB_URI = getenv("mongodb+srv://gotouhitoriii:D0ybqrDVq6MuKiqh@suika.al7oyue.mongodb.net/?retryWrites=true&w=majority&appName=Suika", None)

#Assistant-Setup
API_ID = int(getenv("22069422"))
API_HASH = getenv("a2b3891c2041a4326fcb4e77b54fb32a")

STRING1 = getenv("AQExX0YAsiyPsOjlKh7SMf9FEeIBVaI_9FWLYz4fEgATyid7kl7DORMSqKiaqFkQMi3j4lBFlotE3GrZ0ORSNpu-Ry-A6rgA1WCheVEE3rHKtv1wMkZ9oZU_u7NZxGyRWzcoiS-ZEnUo3FX0ygPChG-s8kbPzmwyhjsP5vR19AbcCc0Q4ZiyVaUCbPg0a0PABp__Jm76OmKTaitV4uY2cVR6WK6K37DEUOXcpn3_ow_78tysZcN-jifh30fLYaT_kXbYdny-9b4ZgQ1jjAttHCigJmwkDo4aYHDkUyK5L3pS0nPokvQWQ4oBNulpXnql8kr1cSkDTN8SbHmlL5IHypKKAvJ0hAAAAAFqyyBcAA")
STRING2 = getenv("AQExX0YAsdC2f4A841hwcQfoUgM4Ck1m1_LjwofrtE1HhCs2GkKo_Uvdb4E5JnhxAY80bJxleUq9NkOZ8n5xhmdZU3VCYHuFtk9Jy_gccvCzmwwABbR_QH8wNLZTyLMwdM75CCJvjCdcP1okVqNrhm7T9GlBVyNmS0Lv1JACENVuDda-gp9wa4sAiCVxwqMYSWgtXbkgKBBBxrBfyxs2rymlNm0wECWw7ZQUmBsbcCXfQZzrCV56bgDUCLVGo6WwMQCQwqaxeb4RKDOENyB4IM-OZQtYFCXUVlPs90lAOM37hCU8ug7ITqqlbQVeFx_gTTiEn8bi0nJ-3ZThh_OnoKopK9lk8AAAAAFqyyBcAA")
STRING3 = getenv("AQExX0YAPGP26w-NRrCCo6NWSDsFK-0g6jVl4jItVXjnU-ODRxjwzWmm4R7zPCuLYibQBr3CWHFDNz8oef4W4bG6ytFfjEMJ1Bs3CL1_F2aEml3KmYaQpPfgDyW_RSXbxsZSVSUxzbxzlgnYoED7dW83G00CUlmPBmp8Brz8JgygKhnzfXa64HeUzRm_T9dnhOmh1Gc8MsGNOx8aXf31bwo1zj4ghJdpOwhmPoAjvw2tSgs0myWgiCkZ5ZqRWX9UEj-H6wVGdLNMY171xJYAdolRs3owZzpYznu51JrKsImRULTdbwvSpSKMtG0l8eGl4EUfzR7UcLwjnxajH6K07tC9Eh8exAAAAAFqyyBcAA")
STRING4 = getenv("AQExX0YAXi9wzFFWfXAQwl_0_YVriQSPTMfxeGiUcpSu44Wken5yNMmsHA3zOSc-YoajpHcBm34pG8Dlh-9t-LmJaGB9fgL2sS_w6KXEzJMEgrXLFHRLmO7v7MNPS5ap3zT-Eq_GDcCQiWHrBZtwhnOSwn1rmjv2p80vBeRzNQLosz67RMHCfIfSfFCytXQf6crsZcQLsyRHMfQ2MIn06vhXF_eaxoyeCcBiZq_km2RpizertWLjqo5ET0IXk1H5Dzu06WlGgXFJ3PgLvvUJz-nPXNBHztjzhb3lym17Bjwp8Z3Ix0AkbnmUufMBIT6mXKgyT-ImNumEK7jlGmAHQAijhYxR2gAAAAFqyyBcAA")
STRING5 = getenv("AQExX0YAYQSaxN4mnSskvbScI-1ZWPU_KOS1ZqDbQEYe9C_fpV4EpI0r90A3kwwQ0RitiGU13PXKhrRQQHgISXuWlPkll9AtODbmXgABLy_nLk-z42BV0fVtbgxooU9Ei6i8iycNMBslI5VzLIh3e3NI5I3CCSO3oww7gVF5SIBy-EhNqb00X0vqskEsJS7lMa44xv8aZyb7zgXGeVOXcWk7DUzbmJ72uXcxrSMEoyr1V5aF1nbjjhiPwAZbjBXaHcuUCrWajujfvZlYxgfNA5jwkmXV183jZGSWnExKMVemYGV6X-n_rCzxyu3Kg5P86rnWsq481kNYaIMgiadW-v2piMANNQAAAAFqyyBcAA")
AUTO_LEAVING_ASSISTANT = bool(getenv("True")) 



SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CHATHV3N")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/CHATH3VN")

SPOTIFY_CLIENT_ID = getenv("6a376276a5ab4ce88428cdb8f76eaf8b")
SPOTIFY_CLIENT_SECRET = getenv("86e6b8e2e4a74f89a7774e3856871944")

#HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
#HEROKU_API_KEY = getenv("HEROKU_API_KEY")

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


START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.pinimg.com/236x/57/ec/22/57ec223ee51d8753168de1af3ede1aeb.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.pinimg.com/564x/d9/b5/46/d9b5464b3de60b9b1df325e41cf22fd3.jpg"
)
STATS_IMG_URL = "https://i.pinimg.com/originals/2f/b8/d3/2fb8d33c12f3816e5bfed7fe614d447a.jpg"
PLAYLIST_IMG_URL = "https://i.pinimg.com/736x/ea/e1/e3/eae1e38f90928b64acf67a85462667ea.jpg"
TELEGRAM_AUDIO_URL = "https://i.pinimg.com/736x/71/e8/4b/71e84b0169197bece76520e3979cf899.jpg"
TELEGRAM_VIDEO_URL = "https://i.pinimg.com/736x/71/e8/4b/71e84b0169197bece76520e3979cf899.jpg"
STREAM_IMG_URL = "https://i.pinimg.com/originals/03/e8/db/03e8db879f8e9a0a83514b135260e182.jpg"
YOUTUBE_IMG_URL = "https://i.pinimg.com/originals/d0/30/eb/d030ebe0b24de823dda499ac37301eb2.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://w0.peakpx.com/wallpaper/407/1022/HD-wallpaper-wets-female-wet-brown-eyes-sexy-cute-short-hair-girl-anime-hot-anime-girl-black-hair-night.jpg"
SPOTIFY_ALBUM_IMG_URL = SPOTIFY_ARTIST_IMG_URL
SPOTIFY_PLAYLIST_IMG_URL = SPOTIFY_ARTIST_IMG_URL


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
