"""Módulo de camada intermediária entre o banco de dados dos ingressos e o sistema"""
from src.extensions import db
from src.models.ticket import Ticket


class TicketRepository:
    """Classe que interliga o banco de dados de ingressos e o sistema"""

    def create(self, data: dict) -> Ticket:
        """Cria um novo ingresso de acordo com os campos do dicionário"""
        new_ticket = Ticket(
            ticket_type=data["ticket_type"],
            price=data["price"],
            total_available_quantity=data.get("total_available_quantity", 0),
            sold_quantity=data.get("sold_quantity", 0),
        )

        db.session.add(new_ticket)
        db.session.commit()

        return new_ticket

    def find_by_id(self, ticket_id: int) -> Ticket:
        """
        Retorna um ingresso que possui o id especificado no parâmetro |
        Caso não encontre nenhum ingresso com o id especificado, retorna None
        """
        return Ticket.query.filter_by(ticket_id=ticket_id).first()

    def find_by_type(self, ticket_type: str):
        """Retorna um ingresso que possui o nome especificado no parâmetro |
        Caso não encontre nenhum ingresso com o id especificado, retorna None"""
        return Ticket.query.filter_by(ticket_type= ticket_type).first()

    def update(self, ticket_id: int, **kwargs) -> Ticket:
        """Atualiza os campos do ingresso de acordo com os campos do dicionário
        Caso não encontre nenhum ingresso com o id especificado, retorna False"""
        ticket = self.find_by_id(ticket_id)

        if not ticket:
            return None

        for key, value in kwargs.items():
            if hasattr(ticket, key):
                setattr(ticket, key, value)

        db.session.commit()

        return ticket

    def delete(self, ticket_id: int) -> Ticket:
        """
        Deleta o ingresso com o id especificado e o retorna |
        Caso não encontre nenhum ingresso com o id especificado, retorna False
        """
        ticket = self.find_by_id(ticket_id)
        if not ticket:
            return None

        db.session.delete(ticket)
        db.session.commit()

        return ticket

    def get_available_tickets(self, event_id: int) -> list[Ticket]:
        """Retorna apenas ingressos disponíveis (com quantidade maior que zero)"""
        return Ticket.query.filter(
            Ticket.event_id == event_id,
            (Ticket.total_available_quantity - Ticket.sold_quantity) > 0
        ).all()
