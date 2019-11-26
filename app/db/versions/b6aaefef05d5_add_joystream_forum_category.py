"""Add joystream forum category

Revision ID: b6aaefef05d5
Revises: a2fc0a403498
Create Date: 2019-11-26 16:38:00.681574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6aaefef05d5'
down_revision = 'a2fc0a403498'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('joystream_forum_category',
    sa.Column('id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('parent_id', sa.BigInteger(), nullable=True),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('num_direct_subcategories', sa.Integer(), nullable=True),
    sa.Column('num_direct_unmoderated_threads', sa.Integer(), nullable=True),
    sa.Column('num_direct_moderated_threads', sa.Integer(), nullable=True),
    sa.Column('position_in_parent_category', sa.Integer(), nullable=True),
    sa.Column('account_id', sa.String(length=64), nullable=True),
    sa.Column('block_id', sa.Integer(), nullable=False),
    sa.Column('extrinsic_idx', sa.Integer(), nullable=True),
    sa.Column('event_idx', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'block_id')
    )
    op.create_index(op.f('ix_joystream_forum_category_block_id'), 'joystream_forum_category', ['block_id'], unique=False)
    op.create_index(op.f('ix_joystream_forum_category_created_at'), 'joystream_forum_category', ['created_at'], unique=False)
    op.create_index(op.f('ix_joystream_forum_category_description'), 'joystream_forum_category', ['description'], unique=False)
    op.create_index(op.f('ix_joystream_forum_category_id'), 'joystream_forum_category', ['id'], unique=False)
    op.create_index(op.f('ix_joystream_forum_category_parent_id'), 'joystream_forum_category', ['parent_id'], unique=False)
    op.create_index(op.f('ix_joystream_forum_category_title'), 'joystream_forum_category', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_joystream_forum_category_title'), table_name='joystream_forum_category')
    op.drop_index(op.f('ix_joystream_forum_category_parent_id'), table_name='joystream_forum_category')
    op.drop_index(op.f('ix_joystream_forum_category_id'), table_name='joystream_forum_category')
    op.drop_index(op.f('ix_joystream_forum_category_description'), table_name='joystream_forum_category')
    op.drop_index(op.f('ix_joystream_forum_category_created_at'), table_name='joystream_forum_category')
    op.drop_index(op.f('ix_joystream_forum_category_block_id'), table_name='joystream_forum_category')
    op.drop_table('joystream_forum_category')
    # ### end Alembic commands ###