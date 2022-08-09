import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1950760508:AAG4l3c79ZHK7TvygxVJOGfuTylr2S91eLE")

    APP_ID = int(os.environ.get("APP_ID", 1911873))

    API_HASH = os.environ.get("API_HASH", "0ce89b116962bb612dd09fbbb9a9316d")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "TSNM_CHNLS")
