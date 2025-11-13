from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("19337121"))
API_HASH = getenv("a01b330cd8a1820dc8f130e797739fcb")

BOT_TOKEN = getenv("8524160412:AAFMKvTksUFjDEN1GTQYpXjzktQbTZ92Kbc", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("8121531844"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1ec3d81dccec214225b72.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1ec3d81dccec214225b72.jpg")

SESSION = getenv("AgEnD6EAEL5cRh-Ubias6cm2iIJ2LsxSk1cIDWmkh9YEv9SG7NwMgaT6rnravzRFXahk9UavbA-6XcqwcyGnxwa1BkVuEyoh5sgQduFg44K6ZDdJXyg3A8Aq71TxNtwz_LdFBoPsSZDMVannHhhg_8zAZb_ONK1dMl4yk5ttvHiaIAfY2ilAqoYWN0t54ANoQmjvqlEQXbkiR0p4kikcqs9njvG7jsKtGn9CERd5a6hIVk27IG0srtOZ0LiaCxruJ_tOloz854HYDNK2tFk35Cuqs8dcjNfMuH_cEFV_ZKDnecv8BmjsPqg9aB4O8Rl01qFg8JvcWUwA-BkwcRTyA4FH9D2_ywAAAAHkFL3EAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/IS1SA")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/IS1SA")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6730935472").split()))


FAILED = "https://telegra.ph/file/1ec3d81dccec214225b72.jpg"

