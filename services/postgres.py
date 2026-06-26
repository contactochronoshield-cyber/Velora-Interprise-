import os
import pg8000

def connect():

    return pg8000.connect(
        host=os.getenv("PG_HOST","localhost"),
        port=int(os.getenv("PG_PORT","5432")),
        user=os.getenv("PG_USER","velora"),
        password=os.getenv("PG_PASSWORD","velora"),
        database=os.getenv("PG_DATABASE","velora")
    )
