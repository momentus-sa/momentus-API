"""change id to event_category_id in table Event_categories

Revision ID: 0eaf77c5d5ed
Revises: 93b1fefde2da
Create Date: 2025-02-21 22:09:03.856695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eaf77c5d5ed'
down_revision = '93b1fefde2da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Event_categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Event_category_id', sa.Integer(), nullable=False))
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Event_categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_column('Event_category_id')

    # ### end Alembic commands ###
