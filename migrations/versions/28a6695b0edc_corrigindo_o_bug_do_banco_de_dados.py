"""Corrigindo o bug do banco de dados

Revision ID: 28a6695b0edc
Revises: 551dc9bf1805
Create Date: 2025-02-23 01:57:22.898134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28a6695b0edc'
down_revision = '551dc9bf1805'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Event_categories',
    sa.Column('event_category_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('is_default', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('event_category_id'),
    sa.UniqueConstraint('event_category_id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Event_categories')
    # ### end Alembic commands ###
