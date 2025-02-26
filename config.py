import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22928570")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "60bb37bddecb48c27c3e86906a077603") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7292841969:AAFkyQHkP8dRs-SabfnLhEhZbVIgXzINR7k") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002254715548') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://free4gb:Free4GBRenameBot@free4gbrenamebot-1.hyqjm.mongodb.net/?retryWrites=true&w=majority&appName=free4gbrenamebot-1")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","free4gbrenamebot-1") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "2010016480")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002310704668')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://envs.sh/Vm.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
