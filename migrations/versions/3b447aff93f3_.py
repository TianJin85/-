"""empty message

Revision ID: 3b447aff93f3
Revises: 
Create Date: 2020-03-10 15:27:56.745129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b447aff93f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('love_user', sa.Column('search_wx', sa.String(length=500), nullable=True, comment='查看过我微信的人'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('love_user', 'search_wx')
    # ### end Alembic commands ###
