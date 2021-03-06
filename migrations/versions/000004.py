"""empty message

Revision ID: 000004
Revises: 000003
Create Date: 2020-02-13 14:44:41.842609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '000004'
down_revision = '000003'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('level',
    sa.Column('level_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('level_number', sa.Integer(), nullable=False),
    sa.Column('points_to_unlock', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.category_id'], name='fk_level_category'),
    sa.PrimaryKeyConstraint('level_id')
    )
    op.create_table('user_levels',
    sa.Column('user_level_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('level_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['level_id'], ['level.level_id'], name='fk_level_user'),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='fk_user_level'),
    sa.PrimaryKeyConstraint('user_level_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_levels')
    op.drop_table('level')
    # ### end Alembic commands ###
