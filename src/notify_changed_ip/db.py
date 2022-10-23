from datetime import datetime

from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database

from config import DBSettings

Base = declarative_base()


class IPAddressDB(Base):
    __tablename__ = "ip_address"

    name = Column(String, unique=True, primary_key=True, index=True)
    ip = Column(String)
    update_time = Column(DateTime)

    def __repr__(self):
        return f"<IPAddressDB(name='{self.name}', ip='{self.name}', upd_time='{self.update_time}')>"


class PostgesDB:
    def __init__(self, settings: DBSettings) -> None:
        self.settings = settings
        db_url = (
            f"postgresql://{settings.user}:{settings.password}"
            f"@{settings.host}:{settings.port}/{settings.db}"
        )
        if not database_exists(db_url):
            create_database(db_url)
        self.engine = create_engine(db_url)
        self.session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_external_ip_item(self, session: Session) -> IPAddressDB:
        return session.query(IPAddressDB).filter_by(name="external_ip").first()

    def get_previous_ip(self) -> str | None:
        with self.session() as sess:
            if ip_raw := self.get_external_ip_item(session=sess):
                return ip_raw.ip
        return None

    def set_current_ip(self, ip_address: str) -> None:
        now = datetime.utcnow()
        with self.session() as sess:
            if ip_item := self.get_external_ip_item(session=sess):
                ip_item.ip = ip_address
                ip_item.update_time = now
            else:
                sess.add(IPAddressDB(name="external_ip", ip=ip_address, update_time=now))
            sess.commit()
