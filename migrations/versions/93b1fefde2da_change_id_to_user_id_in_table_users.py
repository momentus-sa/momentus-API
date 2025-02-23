"""change id to user_id in table users

Revision ID: 93b1fefde2da
Revises: 
Create Date: 2025-02-21 22:05:34.391729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93b1fefde2da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.UUID(), nullable=False))
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.UUID(), autoincrement=False, nullable=False))
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
