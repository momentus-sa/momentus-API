"""Módulo de camada intermediária entre o banco de dados dos fluxos de caixa e o sistema"""
from datetime import datetime
from src.extensions import db
from src.models.cash_flow import CashFlow

#Adicionar o evento que está associado
class CashFlowRepository():
    """Classe interliga o banco de dados das categorias de evento e o sistema"""

    def create(self, data: dict) -> CashFlow:
        """Cria um novo fluxo de caixa de acordo com os campos do dicionário"""
        new_cash_flow = CashFlow(
            title=data["title"],
            description=data.get("description"),
            flow_type=data["flow_type"],
            value=data["value"],
            answerable=data["answerable"],
            spent_at=data.get("spent_at", datetime.utcnow()),
        )

        db.session.add(new_cash_flow)
        db.session.commit()

        return new_cash_flow

    def find_by_id(self, cash_flow_id: int) -> CashFlow:
        """
        Retorna um fluxo de caixa que possui o id especificado no parâmetro |
        caso não encontre nenhum fluxo de caixa com o id especificado, retorna None
        """
        cash_flow = CashFlow.query.filter_by(cash_flow_id=cash_flow_id).first()
        return cash_flow

    def update(self, cash_flow_id: int, **kwargs) -> CashFlow:
        """Atualiza os campos do fluxo de caixa de acordo com os campos do dicionário
        Caso nao encontre nenhum fluxo de caixa com o id especificado, retorna False"""
        cash_flow = self.find_by_id(cash_flow_id)

        if not cash_flow:
            return False

        for key, value in kwargs.items():
            if hasattr(cash_flow, key):
                setattr(cash_flow, key, value)

        cash_flow.updated_at = datetime.utcnow()
        db.session.commit()

        return cash_flow

    def delete(self, cash_flow_id: int) -> CashFlow:
        """
        Deleta o fluxo de caixa com o id especificado e o retorna |
        Caso nao encontre nenhum fluxo de caixa com o id especificado retorna False
        """
        cash_flow = self.find_by_id(cash_flow_id)
        if not cash_flow:
            return False

        db.session.delete(cash_flow)
        db.session.commit()

        return cash_flow
