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


#fazer o loggout do user
#Normalizar os retornos (falso/None)
#Padronizar partes do codigo
#Adicionar exeptions específicas
#Retornar os códigos de Erro HTTP no services
#remover funções crud desnecessárias 
#class meta no schema? NO
#formatar a data e hora YES
#Criar classe membro NO
#faz sentido usar esses event repository por ai??? YES
#Nas extensões adicionar as redundantes
#padronizar os find pra get