"""Módulo que registra as rotas dos usuários"""
from flask import Blueprint, request, jsonify
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
