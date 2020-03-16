"""empty message

Revision ID: 9424a97a7dfb
Revises: 7a9d1cc49a96
Create Date: 2020-03-13 16:57:32.121724

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9424a97a7dfb'
down_revision = '7a9d1cc49a96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('love_user', 'search_wx')
    op.drop_column('love_user', 'search_phone')
    op.drop_column('love_user', 'search_qq')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('love_user', sa.Column('search_qq', mysql.VARCHAR(length=500), nullable=True, comment='查看过我QQ的人'))
    op.add_column('love_user', sa.Column('search_phone', mysql.VARCHAR(length=500), nullable=True, comment='查看过我电话号码的人'))
    op.add_column('love_user', sa.Column('search_wx', mysql.VARCHAR(length=500), nullable=True, comment='查看过我微信的人'))
    # ### end Alembic commands ###
