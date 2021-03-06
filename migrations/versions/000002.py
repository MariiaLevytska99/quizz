"""empty message

Revision ID: 000002
Revises: 000001
Create Date: 2020-02-13 13:46:30.269883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '000002'
down_revision = '000001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=150), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
