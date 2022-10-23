from pydantic import BaseSettings, BaseModel


class DBSettings(BaseModel):
    host: str = "127.0.0.1"
    port: int = 5432
    db: str = "notifier"
    user: str = "postgres"
    password: str = "postgres"


class EmailSettings(BaseModel):
    smtp_instance: str = "smtp.gmail.com"
    smtp_port: int = 587
    sender_address: str = "sender@gmail.com"
    sender_password: str = "password"
    target_address: str = "target@gmail.com"


class AppSettings(BaseSettings):
    db_settings: DBSettings = DBSettings()
    email_settings: EmailSettings = EmailSettings()

    class Config:
        env_nested_delimiter = "__"
        env_file = ".env"
        env_file_encoding = "utf-8"
