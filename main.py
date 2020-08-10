import logging
import sys
from threading import Thread

from app.controllers.webserver import start
from app.models import user_info_access

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == '__main__':
    # user_info.create_table()
    # user_info.init_add()

    serverThread = Thread(target=start)
    serverThread.start()
    serverThread.join()







