# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 


API_ID = os.getenv("27581835", "")
API_HASH = os.getenv("184a11c9b4af04d78d4c1c181781498b", "")
BOT_TOKEN = os.getenv(" 8074485587:AAFxiOkQb4NJpoc-3HTWy3lN-EGiHUXxzjU", "")
MONGO_DB = os.getenv("MONGO_DB", "")
OWNER_ID = list(map(int, os.getenv("6965618585", "").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")

LOG_GROUP = int(os.getenv("LOG_GROUP", "-1003139136725")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1003072916786")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption





