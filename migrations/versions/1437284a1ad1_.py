"""empty message

Revision ID: 1437284a1ad1
Revises: 8860fa8d55de
Create Date: 2020-05-03 16:08:43.201876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1437284a1ad1'
down_revision = '8860fa8d55de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('baseinfo', sa.Column('boolcheck', sa.Boolean(), nullable=True))
    op.add_column('domaininfo', sa.Column('baseinfoid', sa.Integer(), nullable=False))
    op.add_column('ipinfo', sa.Column('baseinfoid', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ipinfo', 'baseinfoid')
    op.drop_column('domaininfo', 'baseinfoid')
    op.drop_column('baseinfo', 'boolcheck')
    # ### end Alembic commands ###
