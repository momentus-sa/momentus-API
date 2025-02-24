"""Arquivo de configuração do projeto"""
import os

class Config:
    """Classe abstrata de configuração do projeto"""
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_USER = os.getenv("DB_USER", "user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_NAME = os.getenv("DB_NAME", "database")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class DevelopmentConfig(Config):
    """Classe de configuração do projeto no modo desenvolvimento"""
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")

class ProductionConfig(Config):
    """Classe de configuração do projeto em produção"""
    DEBUG = False
    LOGGIN_LEVEL = "INFO"
    SECRET_KEY = os.getenv("SECRET_KEY")
