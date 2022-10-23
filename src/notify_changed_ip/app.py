import os
import logging
from urllib import request

from config import AppSettings
from db import PostgesDB
from mail import EmailNotifier

logging.basicConfig(
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    level=os.environ.get("LOGGING", "INFO"),
)


# Application
class Application:
    def __init__(self) -> None:
        self.settings = AppSettings()
        self.db_client = PostgesDB(settings=self.settings.db_settings)
        self.email_client = EmailNotifier(settings=self.settings.email_settings)

    def run(self) -> None:
        prev_ip = self.db_client.get_previous_ip()
        if not (cur_ip := self.get_external_ip()):
            logging.error("Unfortunatly we can't get current ip address.")
            return
        if cur_ip == prev_ip:
            logging.info("Our IP is not changed.")
            return

        logging.info("IP address changed from %s to %s notify about that...", prev_ip, cur_ip)
        if not self.email_client.send_notify(ip_address=cur_ip):
            logging.error("Unfortunatly we can't send notify")
            return

        self.db_client.set_current_ip(ip_address=cur_ip)

    def get_external_ip(self) -> str:
        return request.urlopen("https://ident.me").read().decode("utf8")


if __name__ == "__main__":
    logging.info("Start syncronize job")
    APP = Application()
    APP.run()
    logging.info("Finished job")
