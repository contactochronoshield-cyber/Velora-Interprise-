import os
import jwt
from datetime import datetime,timedelta

SECRET=os.getenv("SECRET_KEY","velora-secret")

def create_token(user):

    payload={

        "user":user,

        "exp":datetime.utcnow()+timedelta(days=1)

    }

    return jwt.encode(
        payload,
        SECRET,
        algorithm="HS256"
    )

def verify(token):

    return jwt.decode(
        token,
        SECRET,
        algorithms=["HS256"]
    )
