"""Alterei os nomes das tabelas para o padrao em lowcase

Revision ID: 9a1d02691ea7
Revises: 28a6695b0edc
Create Date: 2025-02-24 11:51:16.824105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a1d02691ea7'
down_revision = '28a6695b0edc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_categories',
    sa.Column('event_category_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('is_default', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('event_category_id'),
    sa.UniqueConstraint('event_category_id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('Event_categories')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Event_categories',
    sa.Column('event_category_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('is_default', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('event_category_id', name='Event_categories_pkey'),
    sa.UniqueConstraint('name', name='Event_categories_name_key')
    )
    op.drop_table('event_categories')
    # ### end Alembic commands ###
