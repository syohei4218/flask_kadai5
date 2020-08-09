import logging
import sys
from threading import Thread

from app.controllers.webserver import start
from app.models import model

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == '__main__':
    # model.create_table()
    # model.add_user_info()

    serverThread = Thread(target=start)
    serverThread.start()
    serverThread.join()







