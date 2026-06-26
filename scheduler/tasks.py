import time
from services.health import status
from services.backup import create
from services.notifications import notify

while True:

    s=status()

    if s["cpu"]>90:
        notify(
            "High CPU",
            str(s["cpu"])
        )

    if s["disk"]>90:
        notify(
            "Disk Warning",
            str(s["disk"])
        )

    create()

    time.sleep(3600)

