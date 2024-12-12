import logging

from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class Database(BaseSettings):
    """Reads and parses settings from the environment."""

    database: SecretStr
    host: SecretStr
    port: SecretStr
    user: SecretStr
    password: SecretStr

    class Config:
        frozen = True
        env_prefix = "DB_"

    @property
    def postgres_dsn(self) -> PostgresDsn:
        user = self.user.get_secret_value()
        password = self.password.get_secret_value()
        host = self.host.get_secret_value()
        port = self.port.get_secret_value()
        database = self.database.get_secret_value()

        return f"postgresql://{user}:{password}@{host}:{port}/{database}"
