"""Changed datatype block dates

Revision ID: 3abfab7edea8
Revises: 7fbc3f613fa9
Create Date: 2019-06-05 16:50:51.451663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3abfab7edea8'
down_revision = '7fbc3f613fa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data_block', sa.Column('full_day', sa.Integer(), nullable=True))
    op.add_column('data_block', sa.Column('full_hour', sa.Integer(), nullable=True))
    op.add_column('data_block', sa.Column('full_month', sa.Integer(), nullable=True))
    op.add_column('data_block', sa.Column('full_week', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('data_block', 'full_week')
    op.drop_column('data_block', 'full_month')
    op.drop_column('data_block', 'full_hour')
    op.drop_column('data_block', 'full_day')
    # ### end Alembic commands ###
