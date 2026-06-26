import shutil
from datetime import datetime

def create():

    shutil.copy(
        "database/velora.db",
        "backups/daily/velora_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".db"
    )
