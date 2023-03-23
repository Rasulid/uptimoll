"""add data v2

Revision ID: faece1efa814
Revises: 13dde1dac02e
Create Date: 2023-03-01 22:40:47.370374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faece1efa814'
down_revision = '13dde1dac02e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('infos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('course', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_infos_id'), 'infos', ['id'], unique=False)
    op.drop_index('ix_info_id', table_name='info')
    op.drop_table('info')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('info',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('course', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='info_pkey')
    )
    op.create_index('ix_info_id', 'info', ['id'], unique=False)
    op.drop_index(op.f('ix_infos_id'), table_name='infos')
    op.drop_table('infos')
    # ### end Alembic commands ###
