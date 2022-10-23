import smtplib
import logging

from config import EmailSettings


class EmailNotifier:
    def __init__(self, settings: EmailSettings) -> None:
        self.settings = settings

    def send_notify(self, ip_address: str) -> bool:
        try:
            smtp = smtplib.SMTP(self.settings.smtp_instance, self.settings.smtp_port)
            smtp.starttls()
            smtp.login(self.settings.sender_address, self.settings.sender_password)
            body = "\r\n".join(
                (
                    "From: Server notification",
                    f"To: {self.settings.target_address}",
                    "Subject: IP address changed",
                    "",
                    f"IP address of server changed to {ip_address}",
                )
            )
            smtp.sendmail(self.settings.sender_address, self.settings.target_address, body)
            smtp.quit()
            return True
        except Exception as exc:
            logging.error("Error during send notification. Error: %s", exc)
            return False
