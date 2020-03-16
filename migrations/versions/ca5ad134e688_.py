"""empty message

Revision ID: ca5ad134e688
Revises: 89311980ce03
Create Date: 2020-03-09 17:27:31.530890

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca5ad134e688'
down_revision = '89311980ce03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('love_message', sa.Column('monthly', sa.String(length=30), nullable=True, comment='月薪范围'))
    op.drop_column('love_message', 'monthly1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('love_message', sa.Column('monthly1', mysql.FLOAT(), nullable=True, comment='月薪'))
    op.drop_column('love_message', 'monthly')
    # ### end Alembic commands ###
