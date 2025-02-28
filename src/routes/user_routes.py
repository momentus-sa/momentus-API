"""Módulo que registra as rotas dos usuários"""
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.controller.users_controller import UserController

users_controller = UserController()


user_bp = Blueprint(
    name='users',
    import_name=__name__,
    url_prefix="/users"
)


@user_bp.post("/login")
def login():
    """Autentica o usuário e retorna um token JWT"""
    return users_controller.login()


@user_bp.post("/create")
def register_user():
    """Define a função associada ao url"""
    return users_controller.create_user()


@user_bp.get("/me")
@jwt_required()
def get_current_user():
    """Retorna os dados do usuário autenticado"""
    current_user_id = get_jwt_identity()
    return users_controller.get_user_by_id(current_user_id)


@user_bp.get("/events")
@jwt_required()
def get_user_events():
    """Retorna os eventos do usuário com o id especificado"""
    return users_controller.get_user_events()


@user_bp.put("/update")
@jwt_required()
def update_user():
    """Atualiza os dados do usuário autenticado"""
    current_user_id = get_jwt_identity()
    return users_controller.update_user(current_user_id)

# @user_bp.get("/all")
# def get_all_users():
#     """Define a função associada ao url"""
#     return users_controller.get_all_users()


# @user_bp.get("/email/<string:user_email>")
# def get_user_by_email(user_email):
#     """Define a rota que busca o usuário pelo email"""
#     return users_controller.get_user_by_email(user_email)


# @user_bp.get("/id/<string:user_id>")
# def get_user_by_id(user_id):
#     """Retorna o usuário com o id especificado"""
#     return users_controller.get_user_by_id(user_id)
