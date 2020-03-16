"""empty message

Revision ID: 4f3a0e15f055
Revises: 1ff8259cbad8
Create Date: 2020-03-09 17:39:04.923345

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4f3a0e15f055'
down_revision = '1ff8259cbad8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('love_selection', 'weight')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('love_selection', sa.Column('weight', mysql.VARCHAR(length=4), nullable=False, comment='体重'))
    # ### end Alembic commands ###
