"""Módulo que registra as rotas dos usuários"""
from flask import Blueprint
from src.controller.users_controller import UserController

users_controller = UserController()


user_bp = Blueprint(
    name='users',
    import_name=__name__,
    url_prefix="/users"
)


@user_bp.post("/create")
def register_user():
    """Define a função associada ao url"""
    return users_controller.create_user()


@user_bp.get("/all")
def get_all_users():
    """Define a função associada ao url"""
    return users_controller.get_all_users()


@user_bp.get("/email/<string:user_email>")
def get_user_by_email(user_email):
    """Define a rota que busca o usuário pelo email"""
    return users_controller.get_user_by_email(user_email)


@user_bp.get("/id/<string:user_id>")
def get_user_by_id(user_id):
    """Retorna o usuário com o id especificado"""
    return users_controller.get_user_by_id(user_id)

@user_bp.put("/update/<string:user_id>")
def update_user(user_id):
    """Define a rota que atualiza o usuário com o id especificado"""
    return users_controller.update_user(user_id)
