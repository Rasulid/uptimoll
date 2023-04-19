"""test table deletes

Revision ID: edd3ff3e2b4c
Revises: 650c2ed14deb
Create Date: 2023-04-15 09:36:56.677743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edd3ff3e2b4c'
down_revision = '650c2ed14deb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'ss')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('ss', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###