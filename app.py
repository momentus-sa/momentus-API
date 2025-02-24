"""Módulo principal do projeto"""
from dotenv import load_dotenv
from src import create_app
from src.extensions import db

if not load_dotenv(override=True):
    raise RuntimeError("Unable to load settings file (.env)")

app = create_app()

if __name__ == '__main__':
    #Remover no deploy
    with app.app_context():
        db.create_all()

    app.run()
