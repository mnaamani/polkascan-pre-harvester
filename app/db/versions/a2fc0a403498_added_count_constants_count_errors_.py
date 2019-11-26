"""Added count_constants count_errors fields

Revision ID: a2fc0a403498
Revises: 0b385b73588e
Create Date: 2019-11-15 10:29:53.214346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2fc0a403498'
down_revision = '0b385b73588e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('runtime', sa.Column('count_constants', sa.Integer(), server_default='0', nullable=False))
    op.add_column('runtime', sa.Column('count_errors', sa.Integer(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('runtime', 'count_errors')
    op.drop_column('runtime', 'count_constants')
    # ### end Alembic commands ###