import platform
import socket
import psutil

def info():

    return {

        "hostname":socket.gethostname(),

        "platform":platform.system(),

        "release":platform.release(),

        "cpu":psutil.cpu_percent(),

        "ram":psutil.virtual_memory().percent,

        "disk":psutil.disk_usage("/").percent

    }

