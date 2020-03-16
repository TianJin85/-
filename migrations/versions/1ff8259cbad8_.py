"""empty message

Revision ID: 1ff8259cbad8
Revises: ca5ad134e688
Create Date: 2020-03-09 17:32:10.467127

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1ff8259cbad8'
down_revision = 'ca5ad134e688'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('love_selection', sa.Column('age', sa.String(length=30), nullable=False, comment='年龄'))
    op.drop_column('love_selection', 'age_bracket')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('love_selection', sa.Column('age_bracket', mysql.VARCHAR(length=30), nullable=False, comment='年龄'))
    op.drop_column('love_selection', 'age')
    # ### end Alembic commands ###