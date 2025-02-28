"""Módulo destinado ao controller dos fluxos de caixa"""
from flask import request, jsonify, Response
from src.services.cash_flow_services import CashFlowServices

class CashFlowController(object):
    """Classe que representa o controller de fluxos de caixa"""

    def __init__(self):
        self.service = CashFlowServices()

    #Verificar se os campos obrigatórios estao preenchidos
    def create_cash_flow(self) -> tuple[Response, int]:
        """Serviço que cria um novo fluxo de caixa"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            cash_flow = self.service.create_cash_flow(data)
            return jsonify(cash_flow), 201

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_cash_flow_by_id(self, cash_flow_id: int) -> tuple[Response, int]:
        """Retorna o fluxo de caixa com o ID especificado"""
        try:
            cash_flow = self.service.get_cash_flow_by_id(cash_flow_id)
            return jsonify(cash_flow), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    #criar exceçoes personalizadas para diferenciar erros 400 e 404
    #Verificar se os campos obrigatórios estão preenchidos
    def update_cash_flow(self, cash_flow_id: int) -> tuple[Response, int]:

        """Atualiza os dados do fluxo de caixa com o ID especificado"""
        if not request.is_json:
            return jsonify({"error": "O corpo da requisição deve estar no formato JSON"}), 400

        data = request.get_json()

        try:
            updated_cash_flow = self.service.update_cash_flow(cash_flow_id, data)

            return jsonify(updated_cash_flow), 202

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def delete_cash_flow(self, cash_flow_id: int) -> tuple[Response, int]:
        """Deleta o fluxo de caixa com o ID especificado"""
        try:
            self.service.delete_cash_flow(cash_flow_id)
            return jsonify({"message": "Fluxo de caixa deletado com sucesso"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    def get_cash_flows_by_event(self, event_id: int) -> tuple[Response, int]:
        """Retorna todos os fluxos de caixa do evento com o ID especificado"""
        try:
            cash_flows = self.service.get_cash_flows_by_event(event_id)
            return jsonify(cash_flows), 200
        except KeyError:
            return jsonify({"error": "Evento não encontrado"}), 404
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
